from typing import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()


class State(TypedDict):
    email: str
    message: str
    approved: bool


llm = ChatOpenAI(model="gpt-4o-mini")


def check_email(state: State):
    print("\nEmail ID:", state["email"])

    if "@" not in state["email"]:
        print("Invalid email ID.")
        return {"approved": False}

    answer = interrupt(
        f"Approve this email ID: {state['email']}? (yes/no)"
    )

    if answer.lower() == "yes":
        return {"approved": True}

    return {"approved": False}


def draft_email(state: State):
    response = llm.invoke(
        f"Write a short professional email to {state['email']} "
        f"about confirming an appointment."
    )

    print("\nDraft Email:")
    print(response.content)

    return {
        "message": response.content
    }


def forward_email(state: State):
    print("\nForwarding email...")
    print("To:", state["email"])
    print("Message:", state["message"])
    print("\nEmail forwarded successfully!")

    return {}


def route_email(state: State):
    if state["approved"]:
        return "draft_email"

    return END


builder = StateGraph(State)

builder.add_node("check_email", check_email)
builder.add_node("draft_email", draft_email)
builder.add_node("forward_email", forward_email)

builder.add_edge(START, "check_email")

builder.add_conditional_edges(
    "check_email",
    route_email,
    {
        "draft_email": "draft_email",
        END: END
    }
)

builder.add_edge("draft_email", "forward_email")
builder.add_edge("forward_email", END)

graph = builder.compile(
    checkpointer=InMemorySaver()
)

config = {
    "configurable": {
        "thread_id": "email-1"
    }
}

graph.invoke(
    {
        "email": "user@example.com",
        "message": "",
        "approved": False
    },
    config
)

answer = input("\nApprove? yes/no: ")

result = graph.invoke(
    Command(resume=answer),
    config
)

print("\nApproved:", result["approved"])

# print("\n--- Mermaid Graph ---")
# print(graph.get_graph().draw_mermaid())

png_bytes = graph.get_graph().draw_mermaid_png()

with open("email_graph.png", "wb") as f:
    f.write(png_bytes)

print("\nGraph saved to email_graph.png")