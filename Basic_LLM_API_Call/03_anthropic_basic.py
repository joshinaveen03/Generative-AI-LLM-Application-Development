# Install Library: pip install anthropic

from anthropic import Anthropic

# 1. Create the client
client = Anthropic()

# 2. Send a request to Claude
msg = client.messages.create(
    model="claude-sonnet-4-...",
    max_tokens=1024,
    system="Be concise.",
    messages=[
        {
            "role": "user",
            "content": "What is a token?"
        }
    ]
)

# 3. Print Claude's response
print(msg.content[0].text)