import google.generativeai as genai
from dotenv import load_dotenv
import os


def get_model():
    '''
    This function returns the model object that is used to generate the course proposals.
    The default model is "gemini-1.5-flash"
    The model is created using the API key that is stored in the .env file
    '''
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model
