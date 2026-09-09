from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an experienced {interviewer}. "
        "Generate interview questions for a {experience} candidate."
    ),
    (
        "human",
        "Create 5 interview questions about {topic}."
    ),
])

messages = prompt.invoke({
    "interviewer": "technical interviewer",
    "experience": "senior",
    "topic": "RAG and LangChain"
})

response = model.invoke(messages)

print(response.content)