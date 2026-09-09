from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
 
load_dotenv()
 
@tool
def calculate_sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

tool=[calculate_sum]
 
model= ChatOpenAI(model="gpt-4o-mini", temperature=0)
 
model_with_tools = model.bind_tools([tool])
 
response = model_with_tools.invoke("What is 12 plus 30?")
 
print(response)