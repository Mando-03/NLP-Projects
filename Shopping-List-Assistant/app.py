from flask import Flask, request, jsonify
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import numpy as np

app = Flask(__name__)

# Load the dataset
all_orders_subset = pd.read_csv('Data/all_orders_subset.csv')

# Extract unique product_id and product_name mapping
product_id_to_name = all_orders_subset[['product_id', 'product_name']].drop_duplicates().set_index('product_id')['product_name']

# Create the user-item matrix
unique_users = all_orders_subset['user_id'].unique()
unique_products = all_orders_subset['product_id'].unique()

# Create mappings from user_id and product_id to integer indices
user_id_to_index = {user_id: idx for idx, user_id in enumerate(unique_users)}
product_id_to_index = {product_id: idx for idx, product_id in enumerate(unique_products)}

# Map user_id and product_id to their respective indices
row_indices = all_orders_subset['user_id'].map(user_id_to_index)
col_indices = all_orders_subset['product_id'].map(product_id_to_index)

# Create the sparse user-item matrix
user_item_matrix_sparse = csr_matrix(
    (all_orders_subset['reordered'], (row_indices, col_indices)),
    shape=(len(unique_users), len(unique_products))
)

def recommend_products_hybrid(user_id, product_names, all_orders_subset, user_item_matrix_sparse, product_id_to_name, user_id_to_index, top_n=5):
    """
    Recommends products for a given user using a hybrid approach.
    """
    # Step 1: Map product names to product IDs
    product_ids = []
    for name in product_names:
        product_id = all_orders_subset[all_orders_subset['product_name'] == name]['product_id'].values
        if len(product_id) > 0:
            product_ids.append(product_id[0])
        else:
            print(f"Product '{name}' not found in the dataset.")
    
    if not product_ids:
        print("No valid products found. Please check your input.")
        return []
    
    # Step 2: Check if the user exists in the subset
    if user_id not in user_id_to_index:
        print(f"User ID {user_id} not found in the subset.")
        return []
    
    # Step 3: Get the cluster of the target user
    target_user_cluster = all_orders_subset[all_orders_subset['user_id'] == user_id]['cluster'].values[0]
    print(f"Target user belongs to cluster: {target_user_cluster}")
    
    # Step 4: Filter the dataset to include only users in the same cluster
    cluster_users = all_orders_subset[all_orders_subset['cluster'] == target_user_cluster]['user_id'].unique()
    
    # Filter the user-item matrix to include only users in the same cluster
    cluster_user_indices = [user_id_to_index[user] for user in cluster_users if user in user_id_to_index]
    cluster_user_item_matrix = user_item_matrix_sparse[cluster_user_indices]
    
    # Step 5: Find similar users within the cluster using KNN
    knn = NearestNeighbors(n_neighbors=50, metric='cosine', algorithm='brute')  # Increased n_neighbors
    knn.fit(cluster_user_item_matrix)
    
    # Find similar users for the target user
    user_index = user_id_to_index[user_id]
    distances, indices = knn.kneighbors(user_item_matrix_sparse[user_index])
    similar_users = [cluster_users[idx] for idx in indices[0][1:]]  # Exclude the user itself
    
    # Step 6: Get products purchased by similar users but not by the target user
    similar_user_indices = [user_id_to_index[user] for user in similar_users]
    similar_user_products = user_item_matrix_sparse[similar_user_indices].sum(axis=0)  # Sum across similar users
    target_user_products = user_item_matrix_sparse[user_index].nonzero()[1]  # Products purchased by the target user
    
    # Find new products
    new_products = set(similar_user_products.nonzero()[1]) - set(target_user_products)
    print(f"Number of new products: {len(new_products)}")  # Debugging
    
    # Step 7: Get top N recommended products
    recommended_products = list(new_products)[:top_n]
    
    # Filter out invalid product IDs
    valid_recommended_products = [product_id for product_id in recommended_products if product_id in product_id_to_name]
    print(f"Number of valid recommended products: {len(valid_recommended_products)}")  # Debugging
    
    # Fallback: Recommend popular products in the cluster if new products are insufficient
    if len(valid_recommended_products) < top_n:
        print("Insufficient new products. Falling back to popular products in the cluster.")
        cluster_products = all_orders_subset[all_orders_subset['cluster'] == target_user_cluster]['product_id'].value_counts().index.tolist()
        popular_products = [product_id for product_id in cluster_products if product_id in product_id_to_name]
        valid_recommended_products.extend(popular_products[:top_n - len(valid_recommended_products)])
    
    # Map product IDs to product names
    recommended_product_names = [product_id_to_name[product_id] for product_id in valid_recommended_products]
    
    return recommended_product_names

# Define the API endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get JSON data from the request
        data = request.get_json()
        user_id = data.get('user_id')
        product_names = data.get('product_names')
        top_n = data.get('top_n', 5)  # Default to 5 if top_n is not provided
        
        # Clean up product names (remove leading/trailing spaces)
        product_names = [name.strip() for name in product_names]
        
        # Get recommendations
        recommended_products = recommend_products_hybrid(
            user_id=user_id,
            product_names=product_names,
            all_orders_subset=all_orders_subset,
            user_item_matrix_sparse=user_item_matrix_sparse,
            product_id_to_name=product_id_to_name,
            user_id_to_index=user_id_to_index,
            top_n=top_n  # Pass the user-specified top_n
        )
        
        if recommended_products:
            return jsonify({"user_id": user_id, "recommended_products": recommended_products})
        else:
            return jsonify({"user_id": user_id, "message": "No recommendations available."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)