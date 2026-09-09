from typing import TypedDict
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

class State(TypedDict):
    amount: int
    approved: bool

@tool
def payment(amount: int):
    """Make a payment after human approval."""
    approved = interrupt(f"")
    if approved:
        return "Payment approved!"
    return "Payment rejected!"

def payment_node(state: State):
    result = payment.invoke({
        "amount": state["amount"]
    })
    return {"approved": result}

builder = StateGraph(State)
builder.add_node("payment", payment_node)
builder.add_edge(START, "payment")
builder.add_edge("payment", END)
graph = builder.compile(
    checkpointer=InMemorySaver()
)

config = {
    "configurable": {
        "thread_id": "payment-1"
    }
}

graph.invoke(
    {
        "amount": 5000,
        "approved": True
    },
    config
)

answer = input("Approve? yes/no: ")

result = graph.invoke(
    Command(resume=answer.lower() == "yes"),
    config
)

print(result["approved"])