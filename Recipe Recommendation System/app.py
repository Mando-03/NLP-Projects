# # from fastapi import FastAPI, Query
# # from pydantic import BaseModel
# # import pandas as pd
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.metrics.pairwise import cosine_similarity
# # from PIL import Image
# # from io import BytesIO
# # import requests

# # app = FastAPI()


# # class UserInput(BaseModel):
# #     ingredients: str


# # @app.post("/recommend/")
# # def recommend_recipes(user_input: UserInput):
# #     try:
# #         # Import and clean data (ensure the correct file path)
# #         df = pd.read_csv('food_Dataset.csv')
# #         df['cleaned_ingredients'] = df['cleaned_ingredients'].apply(
# #             lambda x: x.replace('[', '').replace(
# #                 ']', '').replace("'", '').split(', ')
# #         )

# #         # Vectorize ingredients
# #         vectorizer = TfidfVectorizer()
# #         tfidf_vectorizer = vectorizer.fit_transform(
# #             df['cleaned_ingredients'].apply(lambda x: ', '.join(x)))

# #         # Process user input
# #         user_input_list = user_input.ingredients.lower().split(', ')
# #         user_input_vector = vectorizer.transform([', '.join(user_input_list)])

# #         # Calculate similarities and recommend recipes
# #         cosine_similarities = cosine_similarity(
# #             tfidf_vectorizer, user_input_vector).flatten()
# #         # Change this to your desired number of recommendations
# #         top_5_indices = cosine_similarities.argsort()[-5:][::-1]
# #         recommended_recipes = df.iloc[top_5_indices]

# #         # Prepare response
# #         response_data = []
# #         for index, recipe in recommended_recipes.iterrows():
# #             try:
# #                 image_url = recipe['thumbnail_url']
# #                 response = requests.get(image_url)
# #                 response.raise_for_status()  # Raise an exception if the request fails
# #                 image = Image.open(BytesIO(response.content))
# #             except requests.exceptions.RequestException as e:
# #                 image = None  # Handle image fetching errors

# #             recipe_data = {
# #                 "name": recipe['name'],
# #                 "ingredients": ", ".join(recipe['cleaned_ingredients']),
# #                 "protein": int(recipe['protein']),
# #                 "fat": int(recipe['fat']),
# #                 "calories": int(recipe['calories']),
# #                 "sugar": int(recipe['sugar']),
# #                 "carbohydrates": int(recipe['carbohydrates']),
# #                 "fiber": int(recipe['fiber']),
# #                 "instructions": recipe['cleaned_instructions'].strip().replace('[', '').replace(']', '').replace("'", '').replace(",", ''),
# #                 "thumbnail_url": recipe['thumbnail_url'],
# #                 "image": image  # You can return the image data or URL here
# #             }
# #             response_data.append(recipe_data)

# #         return {"recommendations": response_data}

# #     except Exception as e:
# #         return {"error": str(e)}  # Return error message for debugging

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from io import BytesIO
# import requests
# from PIL import Image

# app = FastAPI()


# class IngredientsInput(BaseModel):
#     ingredients: str


# @app.post("/recommend/")
# def recommend_recipes(ingredients_input: IngredientsInput):
#     """Performs recipe recommendation based on user-provided ingredients."""

#     try:
#         # Import and clean data
#         df = pd.read_csv('food_Dataset.csv')
#         df['cleaned_ingredients'] = df['cleaned_ingredients'].apply(
#             lambda x: x.replace('[', '').replace(
#                 ']', '').replace("'", '').split(', ')
#         )

#         # Vectorize ingredients
#         vectorizer = TfidfVectorizer()
#         tfidf_vectorizer = vectorizer.fit_transform(
#             df['cleaned_ingredients'].apply(lambda x: ', '.join(x))
#         )

#         # Get user input
#         user_input = ingredients_input.ingredients.lower().split(', ')
#         user_input_vector = vectorizer.transform([', '.join(user_input)])

#         # Calculate similarities and recommend recipes
#         cosine_similarities = cosine_similarity(
#             tfidf_vectorizer, user_input_vector).flatten()
#         top_5_indices = cosine_similarities.argsort()[-5:][::-1]
#         recommended_recipes = df.iloc[top_5_indices].to_dict(orient='records')

#         # Prioritize recipes with exact ingredient matches
#         first_recipe = recommended_recipes[0]
#         first_recipe_ingredients = set(first_recipe['cleaned_ingredients'])
#         user_ingredients_set = set(user_input)
#         if first_recipe_ingredients.intersection(user_ingredients_set):
#             recommended_recipes = [first_recipe] + recommended_recipes[1:]

#         # Fetch thumbnail images for recipes
#         for recipe in recommended_recipes:
#             try:
#                 image_url = recipe['thumbnail_url']
#                 response = requests.get(image_url)
#                 response.raise_for_status()  # Raise an exception if the request fails
#                 image = Image.open(BytesIO(response.content))
#                 recipe['thumbnail_image'] = image
#             except requests.exceptions.RequestException as e:
#                 print(f"Error fetching image: {e}")
#                 recipe['thumbnail_image'] = None

#         return {"recommendations": recommended_recipes}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
import requests
from PIL import Image

app = FastAPI()


class RecommendationRequest(BaseModel):
    ingredients: str


@app.post("/recommend-recipes/")
def recommend_recipes(request: RecommendationRequest):
    # Extract ingredients from the request
    user_input = request.ingredients.lower().split(', ')

    # Import and clean data (replace 'food_Dataset.csv' with your dataset path)
    df = pd.read_csv('food_Dataset.csv')
    df['cleaned_ingredients'] = df['cleaned_ingredients'].apply(
        lambda x: x.replace('[', '').replace(
            ']', '').replace("'", '').split(', ')
    )

    # Vectorize ingredients using TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_vectorizer = vectorizer.fit_transform(
        df['cleaned_ingredients'].apply(lambda x: ', '.join(x))
    )

    # Transform user input into TF-IDF vector
    user_input_vector = vectorizer.transform([', '.join(user_input)])

    # Calculate cosine similarities
    cosine_similarities = cosine_similarity(
        tfidf_vectorizer, user_input_vector).flatten()
    top_5_indices = cosine_similarities.argsort()[-15:][::-1]
    recommended_recipes = df.iloc[top_5_indices]

    # Prepare response data
    info = []
    for index, recipe in recommended_recipes.iterrows():
        # Retrieve and display recipe information (handle potential errors)
        try:
            image_url = recipe['thumbnail_url']
            response = requests.get(image_url)
            response.raise_for_status()  # Raise an exception if the request fails
            image = Image.open(BytesIO(response.content))
            # Do something with the image, e.g., save it locally or return its URL

        except requests.exceptions.RequestException as e:
            print(f"Error fetching image: {e}")

        # Collect recipe info for response
        recipe_info = {
            "Recipe Name": recipe['name'],
            "Ingredients": ", ".join(recipe['cleaned_ingredients']),
            "Protein": recipe['protein'],
            "Fat": recipe['fat'],
            "Calories": recipe['calories'],
            "Sugar": recipe['sugar'],
            "Carbohydrates": recipe['carbohydrates'],
            "Fiber": recipe['fiber'],
            "Instructions": recipe['cleaned_instructions'].strip().replace('[', '').replace(']', '').replace("'", ''),
            "Video URL": recipe['video_url'],
            "Thumbnail URL": recipe['thumbnail_url']
        }
        info.append(recipe_info)

    return info
