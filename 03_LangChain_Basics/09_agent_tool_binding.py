from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

# Load environment variables
load_dotenv()


# -----------------------------
# 1. Define the tool
# -----------------------------
@tool
def calculate_sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# -----------------------------
# 2. Create the model
# -----------------------------
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# -----------------------------
# 3. Test tool binding directly
# -----------------------------
model_with_tools = model.bind_tools([calculate_sum])

response = model_with_tools.invoke("What is 12 plus 30?")

print("Tool calls:")
print(response.tool_calls)


# -----------------------------
# 4. Create the agent
# -----------------------------
agent = create_agent(
    model=model,
    tools=[calculate_sum],
)


# -----------------------------
# 5. Invoke the agent
# -----------------------------
result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is 25 plus 17?"
        }
    ]
})


# -----------------------------
# 6. Print the final response
# -----------------------------
print("\nAgent response:")

for message in result["messages"]:
    if hasattr(message, "content") and message.content:
        print(message.content)