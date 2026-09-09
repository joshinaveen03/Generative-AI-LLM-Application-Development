# Install the Library : pip install langchain

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
 
load_dotenv()
 
# Create the chat model
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)
# Send a simple text question
response = model.invoke("Explain LangChain in simple terms.").content
 
# Print just the text of the reply
print(response)
