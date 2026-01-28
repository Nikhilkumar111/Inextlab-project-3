import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # loads .env

API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini(prompt: str):
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
