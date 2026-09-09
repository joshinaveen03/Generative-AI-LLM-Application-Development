from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

class State(TypedDict):
    a: int
    b: int
    result: int

def addition(state: State):
    return {"result": state["a"] + state["b"]}

def multiplication(state: State):
    return {"result": state["result"] * 2}

builder = StateGraph(State)

builder.add_node("addition", addition)
builder.add_node("multiplication", multiplication)

builder.add_edge(START, "addition")
builder.add_edge("addition", "multiplication")
builder.add_edge("multiplication", END)

app = builder.compile()

result = app.invoke({
    "a": 10,
    "b": 5,
    "result": 0
})

print(result["result"])