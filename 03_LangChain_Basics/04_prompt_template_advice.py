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
        "You are a {role}. Give {style} and practical advice to students."
    ),
    (
        "human",
        "Student wants advice about: {question}"
    ),
])

messages = prompt.invoke({
    "role": "college academic advisor",
    "style": "simple and clear",
    "question": "Which subjects should I focus on to improve my semester performance?"
})

response = model.invoke(messages)

print(response.content)