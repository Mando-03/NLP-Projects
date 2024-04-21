from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
import requests
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import streamlit as st


df = pd.read_csv('cleaned_food.csv')

df['cleaned_ingredients'] = df['cleaned_ingredients'].apply(
    lambda x: x.replace('[', '').replace(']', '').replace("'", '').split(', '))

vectorizer = TfidfVectorizer()
tfid_vectorizer = vectorizer.fit_transform(df['cleaned_ingredients'].apply(lambda x: ', '.join(x)))

st.title('Recipe Recommender')

user_input = st.text_input('Enter the ingredients separated by commas:')

if st.button('Recommend'):
    user_input = user_input.lower().split(', ')
    user_input_vector = vectorizer.transform([', '.join(user_input)])
    cosine_similarities = cosine_similarity(
        tfid_vectorizer, user_input_vector).flatten()

    top_5_indices = cosine_similarities.argsort()[-5:][::-1]
    recommended_recipes = df.iloc[top_5_indices]

    for index, recipe in recommended_recipes.iterrows():
        image_url = recipe['thumbnail_url']
        image = Image.open(BytesIO(requests.get(image_url).content))
        st.image(image, caption=recipe['name'], width=800,use_column_width=True, output_format='JPEG')

        st.write(f"Protein: {int(recipe['protein'])}")
        st.write(f"Fat: {int(recipe['fat'])}") 
        st.write(f"Calories: {int(recipe['calories'])}")
        st.write(f"Sugar: {int(recipe['sugar'])}") 
        st.write(f"Carbohydrates: {int(recipe['carbohydrates'])}")

        ingredients_list = ", ".join(recipe['cleaned_ingredients'])
        ingredients_list = ingredients_list.replace(",", ", ")
        st.write(f"Ingredients:  {ingredients_list}")

        instructions_text = recipe['cleaned_instructions'].strip()
        instructions_text = instructions_text.replace('[', '')
        instructions_text = instructions_text.replace(']', '')
        instructions_text = instructions_text.replace("'", '')
        instructions_text = instructions_text.replace(",", '')

        for instruction in instructions_text.splitlines():
            st.write(instruction)

        st.video(recipe['video_url'])
        st.write("--------------------")
