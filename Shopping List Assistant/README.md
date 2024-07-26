
---

# Shopping List Recommendation System

![Instacart Treemap](https://imageio.forbes.com/blogs-images/brittainladd/files/2019/01/instacart_homeland_1-1-e1546733543757.jpg?format=jpg&width=1440)

This project implements a collaborative recommendation system for Instacart, built using PCA, K-Means clustering, and item2vec. The system is deployed using FastAPI and provides a demo interface with Streamlit.

## Project Overview

The goal of this project is to recommend products to users based on their purchase history. The steps involved are:

1. **Data Preprocessing and EDA**: Merging data and performing exploratory data analysis.
2. **Dimensionality Reduction**: Applying PCA to reduce the dimensionality of the data.
3. **Clustering**: Using K-Means clustering to segment users into different clusters.
4. **Recommendation Model**: Implementing item2vec for generating recommendations.
5. **Deployment**: Deploying the recommendation system using FastAPI and creating a demo interface with Streamlit.

## Project Structure
- `Download Data`: Download it from [Kaggle](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis).
- `EDA`: Done EDA for all datasets to get insights.
- `Clustering`: Used PCA (Dimensionality Reductuion) & K-Means( Clustering).
- `item2vec`: use it for collaborative Filtering for our Recommendation System.
- `Recommendation Testing`: Test our recommendations results.
- `recommend.py`: The main script that generates product recommendations.
- `app.py`: The FastAPI application script.
- `streamlit.py`: The Streamlit demo interface.
- `requirements.txt`: The dependencies required to run the project.
- `README.md`: Project documentation.


## Usage

### Running the Recommendation System


1. **Start the FastAPI Server**:
    ```sh
    uvicorn app:app --reload
    ```

    The server will start at `http://127.0.0.1:8000`.

2. **API Request**:
    You can make a POST request to the `/recommendations/` endpoint with the user's last purchase history to get recommendations. For example:
    ```sh
    curl -X POST "http://127.0.0.1:8000/recommendations/" -H "Content-Type: application/json" -d 
    {"last_purchase_history":"milk, bread, eggs"}
    ```

### Running the Streamlit Demo

1. **Start the Streamlit App**:
    ```sh
    streamlit run streamlit.py
    ```

    The Streamlit interface will start at `http://localhost:8501`.

## Scripts

### recommend.py

The `recommend.py` script contains the logic for generating product recommendations. The `recommend_product` function takes the number of products to recommend, the cluster number, and the user's current basket as inputs.

### app.py

The `app.py` script sets up a FastAPI server with an endpoint for fetching product recommendations. It uses the `recommend_product` function from `recommend.py` to generate recommendations.

### streamlit.py

The `streamlit.py` script provides a user-friendly interface for demonstrating the recommendation system. Users can input their last purchase history and receive product recommendations.

## Example

To run the example provided:

1. Start the FastAPI server:
    ```sh
    uvicorn app:app --reload
    ```

2. Start the Streamlit app:
    ```sh
    streamlit run streamlit.py
    ```

3. Enter your last purchase history in the Streamlit interface to get recommendations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


## Acknowledgements

- in app.py i have choose cluster 4 as our test case
---
