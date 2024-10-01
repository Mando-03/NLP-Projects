# Smart Shopping List Collaborative Recommendation System

![image](images/mb.jpeg)  
Credits: [Grocery Doppio](https://www.grocerydoppio.com/articles/the-transformative-power-of-ai-in-personalizing-the-grocery-shopping-experience)

## 🚀 Project Overview

The **Smart Shopping List Collaborative Recommendation System** is a machine learning project designed to suggest personalized shopping items based on users' past purchases and similarities with other users. This project uses advanced techniques such as collaborative filtering, Item2Vec, and clustering to provide users with tailored product recommendations.

## 🌟 Key Features

- **Collaborative Filtering**: Recommends products based on clusters of users who share similar purchasing behaviors.
- **Aisle Share Feature**: Captures user preferences based on the proportion of their purchases from different aisles.
- **Dimensionality Reduction with PCA**: Reduces feature complexity to enhance clustering accuracy and speed.
- **Real-Time Recommendations**: Generates on-the-spot recommendations based on a user’s current shopping basket.
- **Interactive Demo**: Built using Streamlit for a user-friendly experience.

## 📊 Dataset

The dataset used for this project is from the **Instacart Market Basket Analysis** competition on Kaggle. You can find the dataset here: [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/data).

## 🛠 Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mando-03/NLP-Projects.git
   cd NLP-Projects
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

Replace `app.py` with the name of your main application file if it's different.

## 🌐 API Endpoint

The recommendation system is hosted on Render. You can access the API at:

- **API Endpoint**: [https://shopping-list-tetx.onrender.com](https://shopping-list-tetx.onrender.com)
