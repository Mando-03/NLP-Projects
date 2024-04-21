import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
import requests
from PIL import Image


def recommend_recipes():
    """Performs recipe recommendation based on user-provided ingredients."""

    # Import and clean data
    df = pd.read_csv('food_Dataset.csv')
    df['cleaned_ingredients'] = df['cleaned_ingredients'].apply(
        lambda x: x.replace('[', '').replace(
            ']', '').replace("'", '').split(', ')
    )

    # Vectorize ingredients
    vectorizer = TfidfVectorizer()
    tfidf_vectorizer = vectorizer.fit_transform(
        df['cleaned_ingredients'].apply(lambda x: ', '.join(x))
    )

    # Get user input
    user_input = input("Enter the ingredients separated by commas: ")
    user_input = user_input.lower().split(', ')
    user_input_vector = vectorizer.transform([', '.join(user_input)])

    # Calculate similarities and recommend recipes
    cosine_similarities = cosine_similarity(
        tfidf_vectorizer, user_input_vector).flatten()
    top_5_indices = cosine_similarities.argsort()[-15:][::-1]
    recommended_recipes = df.iloc[top_5_indices]

    first_recipe = recommended_recipes.iloc[0]
    first_recipe_ingredients = set(first_recipe['cleaned_ingredients'])
    user_ingredients_set = set(user_input)
    if first_recipe_ingredients.intersection(user_ingredients_set):
        recommended_recipes = pd.concat(
            [pd.DataFrame(first_recipe).T, recommended_recipes.iloc[1:]]
        )

    # Display recommendations
    for index, recipe in recommended_recipes.iterrows():
        try:
            image_url = recipe['thumbnail_url']
            response = requests.get(image_url)
            response.raise_for_status()  # Raise an exception if the request fails
            image = Image.open(BytesIO(response.content))

            # Choose the appropriate method to display the image based on your environment:
            try:
                # IPython/Jupyter Notebook:
                image.show()  # Uncomment this line if using a notebook environment
            except Exception as e:
                print(f"Error displaying image: {e}")
                # Other environments (e.g., terminal):
                # Use a suitable library like matplotlib or other methods
                # (refer to their documentation for specific instructions)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image: {e}")

        print(f"Image URL: {recipe['thumbnail_url']}")
        print(f"Recipe Name: {recipe['name']}")

        # Print ingredients in desired format
        ingredients_list = ", ".join(recipe['cleaned_ingredients'])
        ingredients_list = ingredients_list.replace(
            ",", ", ")  # Add spaces after commas
        print(f"Ingredients: {ingredients_list}")

        print(f"Protein: {recipe['protein']:.2f}")
        print(f"Fat: {recipe['fat']:.2f}")
        print(f"Calories: {recipe['calories']:.2f}")
        print(f"Sugar: {recipe['sugar']:.2f}")
        print(f"Carbohydrates: {recipe['carbohydrates']:.2f}")
        print(f"Fiber: {recipe['fiber']:.2f}")

        instructions_text = recipe['cleaned_instructions'].strip().replace(
            '[', '').replace(']', '').replace("'", '').replace(",", '')
        print("Instructions:")
        for instruction in instructions_text.splitlines():
            print(instruction)

        print(f"Video URL: {recipe['video_url']}")
        print("--------------------")


if __name__ == "__main__":
    recommend_recipes()