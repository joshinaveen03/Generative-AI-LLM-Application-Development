from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
 
load_dotenv()
 
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
 
# {topic} and {audience} are placeholders (variables)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Answer in {style} language."),
    ("human", "{question}"),
])
 
messages = prompt.invoke({
    "role": "friendly science teacher",
    "style": "simple",
    "question": "Why is the sky blue?",
})
 
response = model.invoke(messages)
 
print(response.content)