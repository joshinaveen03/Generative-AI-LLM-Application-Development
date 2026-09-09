from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
 
load_dotenv()
 
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
 
messages = [
    SystemMessage(content="You are a helpful Python teacher. Keep answers short."),
    HumanMessage(content="Explain decorators."),
]
 
response = model.invoke(messages)
 
print(response.content)