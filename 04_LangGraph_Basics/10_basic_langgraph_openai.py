# Tell me a funny joke about programming.

from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class JokeState(TypedDict):
    question: str
    answer: str

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

def ask_llm(state: JokeState):
    response = llm.invoke(state["question"])

    return {
        "answer": response.content
    }

graph = StateGraph(JokeState)

graph.add_node("ask_llm", ask_llm)

graph.add_edge(START, "ask_llm")
graph.add_edge("ask_llm", END)

app = graph.compile()

result = app.invoke({
    "question": "Tell me a joke."
})

print(result["answer"])