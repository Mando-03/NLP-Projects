
# Smart Hybrid Shopping List Recommendation System (User-Based & Clustering-Based Filtering)

![Instacart Jobs](https://parade.com/.image/t_share/MTkwNTgxMjU3NTk4ODA1MTE3/instacart-jobs.png)

---

## 🚀 Project Overview

The **Smart Hybrid Shopping List Recommendation System** is a machine learning project designed to suggest personalized shopping items based on users' past purchases and similarities with other users who purchase similarly. This project uses advanced techniques such as **User-Based Collaborative Filtering**, **Clustering-Based Filtering using KNN**, **K-Means**, and **dimensionality reduction (PCA)** to provide users with tailored product recommendations.

<div align="center">
    <img src="https://drive.google.com/uc?export=view&id=1cz5Vtxa5j3g-MqqcKRE3ToSW4ceo_5Nc" alt="Demo of App" width="600"/>
</div>

---

## 🌟 Key Features

- **User-Based Collaborative Filtering**: Recommends products based on users who share similar purchasing behaviors.
- **Clustering-Based Filtering with KNN**: Recommends products based on users who exist in the same cluster as the user and finds the top similar ones using KNN.
- **Aisle Share Feature**: Captures user preferences based on the proportion of their purchases from different aisles.
- **Dimensionality Reduction with PCA**: Reduces feature complexity to enhance clustering accuracy and speed.
- **K-Means Clustering**: Separates similar users into the same clusters based on their past purchases and similarities.
- **Streamlit App**: Provides an interactive web interface for users to get recommendations.
- **Flask API**: Exposes the recommendation system as a REST API for easy integration.
- **Docker Support**: Simplifies deployment and ensures consistency across environments.

---

## 📊 Dataset

The dataset used for this project is from the **Instacart Market Basket Analysis** competition on Kaggle. You can find the dataset here: [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/data).

Key files include:
- **`orders.csv`**: Information about orders (e.g., user ID, order number, order time).
- **`products.csv`**: Details about products (e.g., product ID, product name, aisle ID, department ID).
- **`aisles.csv`**: Mapping of aisle IDs to aisle names.
- **`departments.csv`**: Mapping of department IDs to department names.
- **`order_products__prior.csv`**: Products in prior orders.
- **`order_products__train.csv`**: Products in training orders.

---

## 📁 Project Structure

```
shopping-list/
├── Data/
│   ├── aisles.csv
│   ├── all_orders_cluster.csv
│   ├── all_orders_subset.csv
│   ├── all_orders.csv
│   ├── departments.csv
│   ├── order_products__prior.csv
│   ├── order_products__train.csv
│   ├── orders.csv
│   └── products.csv
├── 1- EDA.ipynb
├── 2- Clustering.ipynb
├── 3- Recommendation.ipynb
├── app.py
├── streamlit.py
├── Dockerfile
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

## 📚 Notebooks

1. **`1- EDA.ipynb`**:
   - Perform exploratory data analysis to understand the dataset.
   - Visualize trends and patterns in user behavior and product purchases.

2. **`2- Clustering.ipynb`**:
   - Cluster users based on their purchasing behavior using K-Means clustering.
   - Analyze clusters to understand user segments.

3. **`3- Recommendation.ipynb`**:
   - Build a hybrid recommendation system using clustering and collaborative filtering.
   - Test the recommendation system with sample inputs.

---

## 🛠️ Flask API

The recommendation system is exposed as a REST API using Flask. The API accepts a user ID and a list of product names and returns personalized product recommendations.

### API Endpoint

- **URL**: `/recommend`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "user_id": 127645,
    "product_names": ["Wint-O-Green", "Popcorn", "Soda", "Sea Salt Brown Rice Crackers"],
    "top_n": 7
  }
  ```
  
- **Response**:
  ```json
  {
    "recommended_products": [
      "Grape Soda",
      "Medium Square Containers & Lids",
      "Soda",
      "Wint-O-Green",
      "Wrigley's Orbit Wintermint Sugar Free Gum- 3 PK",
      "Popcorn",
      "Banana"
    ],
    "user_id": 127645
  }
  ```

---

## 🐳 Docker Setup

This project includes a Docker setup to simplify development and deployment. Follow the steps below to build and run the Flask API using Docker.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed (usually comes with Docker Desktop).

### Steps to Run the Flask API

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mando_03/shopping-list.git
   cd shopping-list
   ```

2. **Build the Docker Image**:
   Build the Docker image for the Flask API:
   ```bash
   docker-compose build
   ```

3. **Run the Flask API**:
   Start the Flask API container:
   ```bash
   docker-compose up
   ```

   The API will be available at:
   ```
   http://localhost:8000
   ```

4. **Test the API**:
   Send a POST request to the `/recommend` endpoint using `curl` or Postman:
   ```bash
   curl -X POST http://localhost:8000/recommend \
   -H "Content-Type: application/json" \
   -d '{
       "user_id": 127645,
       "product_names": ["Wint-O-Green", "Sea Salt Brown Rice Crackers", "Soda", "Popcorn"],
       "top_n": 5
   }'
   ```

   **Example Response**:
   ```json
   {
       "recommended_products": [
           "Organic Ground Flaxseed",
           "Honey Roasted Peanuts",
           "To Go Creamy Peanut Butter Cups",
           "Wrigley's Orbit Wintermint Sugar Free Gum- 3 PK",
           "Organic Blueberries"
       ],
       "user_id": 127645
   }
   ```

5. **Stop the Container**:
   To stop the container, press `Ctrl+C` or run:
   ```bash
   docker-compose down
   ```

### Docker Compose Configuration
The `docker-compose.yml` file defines the Flask API service with the following configuration:
- **Ports**: Maps port `8000` on the host to port `8000` in the container.
- **Volumes**: Mounts the current directory to `/app` in the container for live code updates.
- **Environment**: Sets the Flask environment to `development`.
- **Networks**: Connects the service to a custom `backend` network.
- **Restart Policy**: Ensures the container restarts automatically if it stops.

### Dockerfile
The `Dockerfile` builds the Flask API image using Python 3.10 and installs the required dependencies from `requirements.txt`.

```Dockerfile
# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 8000 for the Flask API
EXPOSE 8000

# Run the Flask API
CMD ["python", "app.py"]
```

### Notes
- The `shoppingList` named volume is used to persist data (if needed).
- The `backend` network isolates the Flask API service for better security and scalability.

---

## 🎨 Streamlit App

The **Streamlit App** provides an interactive web interface for users to get personalized product recommendations. It allows users to input their `user_id`, a list of product names, and the number of recommendations they want (`top_n`).

### Running the Streamlit App

1. Install Streamlit (if not already installed):
   ```bash
   pip install streamlit
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run streamlit.py
   ```

3. The app will open in your browser at `http://localhost:8501`.

### App Features

- **User Input**:
  - Enter your `user_id`.
  - Input a list of product names (comma-separated).
  - Specify the number of recommendations (`top_n`) using a slider.

- **Output**:
  - Displays the top `n` recommended products based on the user’s input and past purchases.

### Example Usage

1. Enter `user_id = 127645`.
2. Input product names: `Wint-O-Green, Sea Salt Brown Rice Crackers, Soda, Popcorn`.
3. Set `top_n = 5`.
4. Click **Get Recommendations**.

### Output Example

```
Recommended products (Top 5):
- Organic Ground Flaxseed
- Honey Roasted Peanuts
- To Go Creamy Peanut Butter Cups
- Wrigley's Orbit Wintermint Sugar Free Gum- 3 PK
- Organic Blueberries
```

---

## ⚙️ Requirements

The project requires the following Python libraries:

```
flask==3.1.0
numpy==2.2.1
pandas==2.2.3
scikit-learn==1.6.0
scipy==1.15.0
matplotlib==3.10.0
seaborn==0.13.2
plotly==5.24.1
streamlit==1.41.1
```

You can install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🧩 How It Works

1. **Clustering**:
   - Users are grouped into clusters based on their purchasing behavior using K-Means clustering.
   - This helps in narrowing down recommendations to users with similar behavior.

2. **User-Based Filtering**:
   - Within a cluster, the system finds similar users using K-Nearest Neighbors (KNN).
   - Products purchased by similar users (but not by the target user) are recommended.

3. **Hybrid Approach**:
   - Combines cluster-based filtering and user-based collaborative filtering to provide personalized recommendations.

---

## 📝 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Mando_03/shopping-list.git
   ```

2. Navigate to the project directory:
   ```bash
   cd shopping-list
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Test the API using tools like Postman or cURL.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
