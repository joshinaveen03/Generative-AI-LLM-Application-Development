import operator
from typing import Annotated, TypedDict, Literal
from langgraph.graph import StateGraph, START, END, add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Shared state
class State(TypedDict):
    topic: str
    answer: str

# Agent 1: Researcher
def researcher(state: State):
    response = llm.invoke(
        f"You are a researcher. Give 3 facts about {state['topic']}."
    )
    return {"answer": response.content}

# Agent 2: Writer
def writer(state: State):
    response = llm.invoke(
        f"You are a writer. Turn these facts into one sentence:\n"
        f"{state['answer']}"
    )
    return {"answer": response.content}

# Agent 3: Reviewer
def reviewer(state: State):
    response = llm.invoke(
        f"You are a reviewer. Check this answer and improve it:\n"
        f"{state['answer']}"
    )

    return {"answer": response.content}

# Build graph
graph = StateGraph(State)
graph.add_node("researcher", researcher)
graph.add_node("writer", writer)
graph.add_node("reviewer", reviewer)

graph.add_edge(START, "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", "reviewer")
graph.add_edge("reviewer", END)
app = graph.compile()

# Run
result = app.invoke({
    "topic": "tidal energy",
    "answer": ""
})

print(result["answer"])
