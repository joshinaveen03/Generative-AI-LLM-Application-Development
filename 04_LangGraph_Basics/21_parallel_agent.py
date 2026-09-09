import operator
from typing import Annotated, TypedDict, Literal
from langgraph.graph import StateGraph, START, END, add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class State(TypedDict):
    topic: str
    results: Annotated[list[str], operator.add]


def researcher(state):
    response = llm.invoke(
        f"Research {state['topic']} and give 2 important facts."
    )

    return {
        "results": [f"Researcher: {response.content}"]
    }


def analyst(state):
    response = llm.invoke(
        f"Analyze {state['topic']} and give 2 key insights."
    )

    return {
        "results": [f"Analyst: {response.content}"]
    }


def writer(state):
    response = llm.invoke(
        f"Write one short sentence about {state['topic']}."
    )

    return {
        "results": [f"Writer: {response.content}"]
    }

def synthesize(state):
    findings = "\n".join(state["results"])

    response = llm.invoke(
        f"""
Combine these results into one clear final answer:

{findings}
"""
    )

    return {
        "results": [f"Synthesizer: {response.content}"]
    }


graph = StateGraph(State)

graph.add_node("researcher", researcher)
graph.add_node("analyst", analyst)
graph.add_node("writer", writer)
graph.add_node("synthesize", synthesize)

graph.add_edge(START, "researcher")
graph.add_edge(START, "analyst")
graph.add_edge(START, "writer")

graph.add_edge("researcher", "synthesize")
graph.add_edge("analyst", "synthesize")
graph.add_edge("writer", "synthesize")

graph.add_edge("synthesize", END)

app = graph.compile()

result = app.invoke({
    "topic": "electric vehicles",
    "results": []
})


print("\nFINAL RESULT:")
print(result["results"][-1])