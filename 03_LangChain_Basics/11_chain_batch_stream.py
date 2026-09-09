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
 

result2 = chain.batch([
    {"topic": "RAG"},
    {"topic": "gravity"}
])

for item in result2:
    print(item)
    print()


# -----------------------------
# 3. STREAM
# -----------------------------
for chunk in chain.stream({"topic": "gravity"}):
    print(chunk, end="", flush=True)