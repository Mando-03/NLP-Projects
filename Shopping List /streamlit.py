import streamlit as st
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Load the dataset
@st.cache_data  # Cache the dataset for faster loading
def load_data():
    return pd.read_csv('Data/all_orders_subset.csv')

all_orders_subset = load_data()

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
            st.warning(f"Product '{name}' not found in the dataset.")
    
    if not product_ids:
        st.error("No valid products found. Please check your input.")
        return []
    
    # Step 2: Check if the user exists in the subset
    if user_id not in user_id_to_index:
        st.error(f"User ID {user_id} not found in the subset.")
        return []
    
    # Step 3: Get the cluster of the target user
    target_user_cluster = all_orders_subset[all_orders_subset['user_id'] == user_id]['cluster'].values[0]
    st.write(f"Target user belongs to cluster: {target_user_cluster}")
    
    # Step 4: Filter the dataset to include only users in the same cluster
    cluster_users = all_orders_subset[all_orders_subset['cluster'] == target_user_cluster]['user_id'].unique()
    
    # Filter the user-item matrix to include only users in the same cluster
    cluster_user_indices = [user_id_to_index[user] for user in cluster_users if user in user_id_to_index]
    cluster_user_item_matrix = user_item_matrix_sparse[cluster_user_indices]
    
    # Step 5: Find similar users within the cluster using KNN
    knn = NearestNeighbors(n_neighbors=10, metric='cosine', algorithm='brute')  # Find 10 most similar users
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
    
    # Step 7: Get top N recommended products from similar users
    recommended_products = list(new_products)[:top_n]
    
    # Filter out invalid product IDs
    valid_recommended_products = [product_id for product_id in recommended_products if product_id in product_id_to_name]
    
    # Step 8: If not enough recommendations, fall back to top popular products in the cluster
    if len(valid_recommended_products) < top_n:
        cluster_products = all_orders_subset[all_orders_subset['cluster'] == target_user_cluster]['product_id'].value_counts().index.tolist()
        
        # Exclude products already purchased by the target user
        popular_products = [product_id for product_id in cluster_products 
                            if product_id in product_id_to_name and product_id not in target_user_products]
        
        # Add only the required number of popular products
        required = top_n - len(valid_recommended_products)
        valid_recommended_products.extend(popular_products[:required])
    
    # Step 9: Map product IDs to product names
    recommended_product_names = [product_id_to_name[product_id] for product_id in valid_recommended_products]
    
    # Step 10: Exclude products already in the user input (if possible)
    user_input_products = [name.strip() for name in product_names]  # Get user input product names
    final_recommendations = [product for product in recommended_product_names if product not in user_input_products]
    
    # If still not enough recommendations, allow some overlap with user input
    if len(final_recommendations) < top_n:
        remaining = top_n - len(final_recommendations)
        final_recommendations.extend(recommended_product_names[:remaining])
    
    # Debug: Print the number of recommendations
    st.write(f"Total recommendations before filtering: {len(recommended_product_names)}")
    st.write(f"Final recommendations after filtering: {len(final_recommendations)}")
    
    # Ensure exactly top_n recommendations are returned
    if len(final_recommendations) < top_n:
        st.warning(f"Only {len(final_recommendations)} unique recommendations available.")
    
    return final_recommendations[:top_n]  # Ensure only top_n recommendations are returned

# Streamlit App
st.title("Smart Shopping List Recommendation System 🛒")
st.write("Get personalized product recommendations based on your shopping history!")

# Input fields
user_id = st.number_input("Enter your User ID:", min_value=1, value=127645)
product_names = st.text_input("Enter product names (comma-separated):", value="Wint-O-Green, Sea Salt Brown Rice Crackers, Soda, Popcorn")

# Slider for number of recommendations
top_n = st.slider("Number of recommendations:", min_value=3, max_value=10, value=5)

# Convert input to list
product_names = [name.strip() for name in product_names.split(",")]

# Button to trigger recommendations
if st.button("Get Recommendations"):
    st.write("Fetching recommendations...")
    recommendations = recommend_products_hybrid(
        user_id=user_id,
        product_names=product_names,
        all_orders_subset=all_orders_subset,
        user_item_matrix_sparse=user_item_matrix_sparse,
        product_id_to_name=product_id_to_name,
        user_id_to_index=user_id_to_index,
        top_n=top_n  # Use the slider value
    )
    
    if recommendations:
        st.success(f"Recommended products (Top {top_n}):")
        for product in recommendations:
            st.write(f"- {product}")
    else:
        st.error("No recommendations available. Please check your input.")