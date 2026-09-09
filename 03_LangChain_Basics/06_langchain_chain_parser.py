from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
 
load_dotenv()
 
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
 
prompt = ChatPromptTemplate.from_template(
    "Write a one sentence fun fact about {topic}."
)
 
parser = StrOutputParser() #can be removed if you want the raw model output instead of a string
 
# Connect the three steps: prompt, then model, then parser
chain = prompt | model | parser
 
# Run the whole chain with one call
result = chain.invoke({"topic": "the ocean"})
 
print(result)
 