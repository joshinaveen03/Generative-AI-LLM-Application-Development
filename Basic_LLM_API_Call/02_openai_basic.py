import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. Create the client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 2. Make the API call
response = client.chat.completions.create(
    model="gpt-4o-mini",

    messages=[
        {
            "role": "system",
            "content": "Explain Python in simple words"
        },
        # {
        #     "role": "user",
        #     "content": "Explain what a token is in an LLM"
        # }
    ],

    # 3. Parameters
    temperature=0.7,
    max_tokens=200
)

# 4. Print the AI response
print(response.choices[0].message.content)

# 5. Print token usage
print(response.usage)