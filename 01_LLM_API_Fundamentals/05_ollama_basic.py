# Download the Qwen model
# ollama pull qwen3:1.7b

# Run the model in your terminal
# ollama run qwen3:1.7b

# list all your local models
# ollama list

# To close ollama: /bye
# To check version: ollama --version
# pip show ollama

# pip install ollama

import ollama

stream = ollama.chat(
    model="qwen3:1.7b",

    messages=[
        {
            "role": "user",
            "content": "Hi"
        }
    ],

    stream=True
)

for i in stream:
    print(i["message"]["content"], end="", flush=True)