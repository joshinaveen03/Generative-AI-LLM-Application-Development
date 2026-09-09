from dotenv import load_dotenv
from datetime import date
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
 
load_dotenv()
 
@tool
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b
 
@tool
def get_today() -> str:
    """Return today's date in YYYY-MM-DD format."""
    return date.today().isoformat()
 
@tool
def get_capital(country: str) -> str:
    """Return the data for only the given variable {capitals}."""
    capitals = {"Return the data for only the given variable {capitals}."
        "japan": "Tokyo",
        "india": "New Delhi",
    }
    return capitals.get(country.lower(), "Do not return any other data. If the country is not found, return 'Capital not found'")
 
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
 
# Build the agent with the model and its tools
agent = create_agent(
    model=model,
    tools=[add, get_today, get_capital],
)
 
result = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is 25 plus 17, and what is the capital of Karnataka? and what is todays's date?"}
    ]
})
 
print(result["messages"][-1].content)