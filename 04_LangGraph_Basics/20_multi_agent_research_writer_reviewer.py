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
    task: str
    result: str
    next: str

def researcher(state: State):
    response = llm.invoke(
        f"You are a researcher. Research this task and give useful facts:\n"
        f"{state['task']}"
    )
    return {"result": response.content}

def coder(state: State):
    response = llm.invoke(
        f"You are a coder. Solve the task with code if appropriate:\n"
        f"{state['task']}"
    )
    return {"result": response.content}

def writer(state: State):
    response = llm.invoke(
        f"You are a writer. Create a clear final answer using this information:\n"
        f"Task: {state['task']}\n"
        f"Information: {state['result']}"
    )
    return {"result": response.content}

def supervisor(state: State):
    response = llm.invoke(
        f"""
You are a supervisor.

Choose which worker should run next.

Workers:
- researcher
- coder
- writer
- finish

Task:
{state['task']}

Current result:
{state['result']}

Reply with ONLY one word:
researcher
coder
writer
finish
"""
    )
    return {"next": response.content.strip().lower()}

def route(state: State):
    return state["next"]

graph = StateGraph(State)

graph.add_node("supervisor", supervisor)
graph.add_node("researcher", researcher)
graph.add_node("coder", coder)
graph.add_node("writer", writer)

graph.add_edge(START, "supervisor")

graph.add_conditional_edges(
    "supervisor",
    route,
    {
        "researcher": "researcher",
        "coder": "coder",
        "writer": "writer",
        "finish": END
    }
)

graph.add_edge("researcher", "supervisor")
graph.add_edge("coder", "supervisor")
graph.add_edge("writer", "supervisor")

app = graph.compile()

result = app.invoke({
    "task":"Write a Python program to calculate factorial",
    "result":"",
    "next": ""
})

print(result["result"])