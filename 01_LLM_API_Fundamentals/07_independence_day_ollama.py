import ollama

stream = ollama.chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": "Write about India's Independence Day on 15 August 2026, including the chief guest."
        }
    ],
    stream=True
)

for i in stream:
    print(i["message"]["content"], end="", flush=True)