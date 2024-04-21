
# Recipe Recommendation System

This project implements a recipe recommendation system based on user-provided ingredients. The system utilizes cosine similarity and TF-IDF (Term Frequency-Inverse Document Frequency) to suggest recipes similar to the user's input.

## Overview

The recipe recommendation system allows users to input a list of ingredients, and it recommends recipes from a dataset that match or are similar to the provided ingredients. The recommendations include details such as recipe names, ingredients, nutritional information, and links to images and videos.

## Features

- **Content-Based Filtering:** Recommendations are based on the similarity between user-input ingredients and recipes in the dataset.
- **Cosine Similarity:** Calculates similarity scores using cosine similarity metric.
- **TF-IDF Vectorization:** Vectorizes ingredients using TF-IDF for text representation.
- **Data Source:** Utilizes a dataset (`food_Dataset.csv`) containing recipes and their respective ingredients, nutritional information, and multimedia links.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/recipe-recommendation-system.git
   cd recipe-recommendation-system
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn api:app --reload
   ```

## Usage

1. Send a POST request to `http://localhost:8000/recommend_recipes` with the following JSON payload:
   ```json
   {
     "ingredients": "chicken, cheese, tomato"
   }
   ```

2. View the recipe recommendations in the response.

## API Endpoints

- **POST /recommend_recipes:**  
  Endpoint for recipe recommendation based on user-provided ingredients.

## Dependencies

- `pandas`
- `scikit-learn`
- `requests`
- `PIL`
- `fastapi`

## Resources

- Dataset: [food_Dataset.csv](link-to-dataset)
- Example Notebook: [Recipe Recommendation Notebook](link-to-notebook)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace the placeholders (`your-username`, `http://localhost:8000`, `link-to-dataset`, `link-to-notebook`, etc.) with the appropriate URLs, paths, and information relevant to your project.

You can copy and paste the above markdown content into your README.md file on GitHub. This formatted markdown will display correctly on GitHub with code blocks and formatting preserved.
