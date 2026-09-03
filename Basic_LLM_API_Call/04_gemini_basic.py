# Install Library : pip install google-genai

from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Create Gemini client
gm = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# 2. Send request to Gemini
r3 = gm.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is a token in an LLM?",

    config=types.GenerateContentConfig(
        system_instruction="Explain in simple words.",
        max_output_tokens=200
    )
)

# 3. Print Gemini response
print("GEMINI:", r3.text)