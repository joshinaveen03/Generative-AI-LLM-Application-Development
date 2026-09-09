# Load environment variables
# 1. Define the tool
# 2. Create the model
# 3. Test tool binding directly
# 4. Create the agent
# 5. Invoke the agent
# 6. Print the final response

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
# Load environment variables
load_dotenv()
# result=load_dotenv()
# print(result)

# 1. Define the tool
@tool
def calculator(a=int,b=int)->int:
    """Add two numbers"""
    return a+b

# 2. Create the model
model=ChatOpenAI( model="gpt-4o-mini",temperature=0)

# 3. Test tool binding directly
model_with_tools=model.bind_tools([calculator])

response=model_with_tools.invoke("what is 12 pluse 10")
print("Tool_calls")
print(response.tool_calls)

# 4. Create the agent
agent=create_agent(model=model,tools=[calculator])

# 5. Invoke the agent
result=agent.invoke({
    "messages":[
        {
            "role":"user",
            "content":"what is 12 pluse 10"

        }
    ]
})

# 6. Print the final response

print("\n Agent Response:")
for message in result["messages"]:
       #if hasattr(message, "content") and message.content:
            print(message.content)
      