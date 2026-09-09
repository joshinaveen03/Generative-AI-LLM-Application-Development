from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

load_dotenv()


class State(TypedDict):
    email: str
    message: str
    approved: bool


llm = ChatOpenAI(model="gpt-4o-mini")


# Node 1: Create email
def create_email(state: State):
    response = llm.invoke(
        f"Write a short professional email to {state['email']} "
        f"about confirming an appointment."
    )

    return {
        "message": response.content
    }


# Node 2: Check email ID
def check_email(state: State):
    print("\nChecking email ID...")
    print("Email ID:", state["email"])

    if "@" in state["email"]:
        print("Email ID is valid.")
    else:
        print("Invalid email ID.")

    return {}


# Node 3: Send email with approval
def send_email(state: State):
    print("\nGenerated email:")
    print("----------------------")
    print("To:", state["email"])
    print("----------------------")
    print(state["message"])
    print("----------------------")

    approved = interrupt("Approve this email?")

    if approved:
        print("\nEmail sent!")
        return {"approved": True}

    print("\nEmail cancelled.")
    return {"approved": False}


# Build graph
builder = StateGraph(State)

builder.add_node("create_email", create_email)
builder.add_node("check_email", check_email)
builder.add_node("send_email", send_email)


# Flow
builder.add_edge(START, "create_email")
builder.add_edge("create_email", "check_email")
builder.add_edge("check_email", "send_email")
builder.add_edge("send_email", END)


# Compile
graph = builder.compile(
    checkpointer=InMemorySaver()
)


# Thread configuration
config = {
    "configurable": {
        "thread_id": "email-1"
    }
}


# First run
graph.invoke(
    {
        "email": "user@example.com",
        "message": "",
        "approved": False
    },
    config
)


# Human approval
answer = input("\nApprove? yes/no: ")


# Resume graph
result = graph.invoke(
    Command(resume=answer.lower() == "yes"),
    config
)


print("\nApproved:", result["approved"])

graph = builder.compile(
    checkpointer=InMemorySaver()
)

# Visualize the graph
print("\n--- Mermaid Graph ---")
print(graph.get_graph().draw_mermaid())

# Save graph as PNG
png_bytes = graph.get_graph().draw_mermaid_png()

with open("email_graph.png", "wb") as f:
    f.write(png_bytes)

print("\nGraph saved to email_graph.png")
 