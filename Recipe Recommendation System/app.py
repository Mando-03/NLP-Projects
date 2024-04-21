import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI
from pydantic import BaseModel
from io import BytesIO
import requests
from PIL import Image

app = FastAPI()


class IngredientsInput(BaseModel):
    ingredients: str


@app.post("/recommend_recipes")
def recommend_recipes(ingredients_input: IngredientsInput):

    df = pd.read_csv('food_Dataset.csv')
    df['cleaned_ingredients'] = df['cleaned_ingredients'].apply(
        lambda x: [ingredient.strip()for ingredient in x.strip('[]').split(',')])

    vectorizer = TfidfVectorizer()
    tfidf_vectorizer = vectorizer.fit_transform(df['cleaned_ingredients'].apply(lambda x: ', '.join(x)))

    user_input = ingredients_input.ingredients.lower().split(', ')
    user_input_vector = vectorizer.transform([', '.join(user_input)])

    cosine_similarities = cosine_similarity(tfidf_vectorizer, user_input_vector).flatten()
    top_25_indices = cosine_similarities.argsort()[-26:][::-1]  
    recommended_recipes = df.iloc[top_25_indices]

    response_data = []
    for index, recipe in recommended_recipes.iterrows():
        try:
            image_url = recipe['thumbnail_url']
            response = requests.get(image_url)
            response.raise_for_status()  # Raise an exception if the request fails
            image = Image.open(BytesIO(response.content))

            recipe_data = {
                "recipe_name": recipe['name'],
                "ingredients": recipe['cleaned_ingredients'],
                "protein": recipe['protein'],
                "fat": recipe['fat'],
                "calories": recipe['calories'],
                "sugar": recipe['sugar'],
                "carbohydrates": recipe['carbohydrates'],
                "fiber": recipe['fiber'],
                "instructions": recipe['cleaned_instructions']
            }

            response_data.append(recipe_data)

        except requests.exceptions.RequestException as e:
            # Handling image fetching errors
            print(f"Error fetching image: {e}")
            continue

    return response_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
