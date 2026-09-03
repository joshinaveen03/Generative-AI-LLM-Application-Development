# Install library: pip install openapi

from openai import OpenAI
from dotenv import load_dotenv
import os

#Load enviroment
load_dotenv()

#Create Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(client)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello, How are YOU?"}
    ]
)

#Final Result
print(response.choices[0].message.content)