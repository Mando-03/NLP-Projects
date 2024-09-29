import pickle
from gensim.models import Word2Vec
from difflib import get_close_matches
import numpy as np


def load_models_and_data():
    cluster_item_models = [Word2Vec.load(
        f"Models Clusters/model_cluster_{id}.model") for id in range(18)]
    with open('Savings/product_lookup.pkl', 'rb') as file:
        product_lookup = pickle.load(file)
    product_id_lookup = {v: k for k, v in product_lookup.items()}
    return cluster_item_models, product_lookup, product_id_lookup


# matches the products in the user’s current basket to products in the product lookup dictionary using fuzzy matching (for misspelling )
def get_product_matches(current_basket, product_lookup, product_id_lookup):
    # The matched product names are then converted to their corresponding product IDs using the product_id_lookup dictionary
    matches = [match for item in current_basket for match in get_close_matches(item, product_lookup.values())]
    return [product_id_lookup[item] for item in matches]


# filters out product IDs that are not present in the Item2Vec model's vocabulary.
def filter_matches(model, product_ids):
    return [product_id for product_id in product_ids if product_id in model.wv]

# calculate the weighted average of the vectors of the products in the user's basket using softmax weight
def average_item_vectors(model, product_ids):
    if not product_ids:
        return np.zeros(model.vector_size)
    embeddings = [model.wv[product_id] for product_id in product_ids]
    weights = np.exp(range(1, len(embeddings) + 1))
    weights /= weights.sum()
    return np.average(embeddings, axis=0, weights=weights)

# retrieves the products that are most similar to the current basket vector using the Item2Vec model.
def get_similar_products(model, product_lookup, basket_vector, n_matches):
    similar_products = model.wv.similar_by_vector(basket_vector, topn=n_matches + 1)[1:]
    return [product_lookup[item[0]] for item in similar_products]


def recommend_product(product_count, cluster_number, current_basket):
    cluster_item_models, product_lookup, product_id_lookup = load_models_and_data()
    model = cluster_item_models[cluster_number - 1]

    product_ids_matches = get_product_matches(current_basket, product_lookup, product_id_lookup)
    filtered_matches = filter_matches(model, product_ids_matches)

    if not filtered_matches:
        print("None of the last purchase history items in corpus.")
        return {'recommendations': []}

    basket_vector = average_item_vectors(model, filtered_matches[:1])
    recommendations = get_similar_products(model, product_lookup, basket_vector, product_count)
    return {'recommendations': [r for r in recommendations if r not in current_basket][:product_count]}


def retrieve_recommendations(last_purchase_history):
    cluster_number = 4
    history = last_purchase_history.split(',')
    recommendations = recommend_product(10, cluster_number, history)

    print('Recommended Products:')
    for product in recommendations['recommendations']:
        print(product)


if __name__ == '__main__':
    last_purchase_history = input('Enter Current Basket (comma-separated): ')
    retrieve_recommendations(last_purchase_history)
