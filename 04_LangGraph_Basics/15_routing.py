from typing import TypedDict, Literal

from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv


load_dotenv()

# -----------------------------------
# State
# -----------------------------------

class RouterState(TypedDict):
    query: str
    query_type: str
    response: str


# -----------------------------------
# Main Function
# -----------------------------------

def demo_basic_routing():

    # -----------------------------------
    # Initialize LLM
    # -----------------------------------

    llm = init_chat_model(
        model="gpt-4o-mini",
        temperature=0.0
    )

    # -----------------------------------
    # Node 1: Classify Query
    # -----------------------------------

    def classify_query(state: RouterState) -> dict:

        response = llm.invoke(
            f"""
Classify this query as 'question', 'command', or 'statement'.

Reply with just the word.

{state['query']}
"""
        )

        return {
            "query_type": response.content.lower().strip()
        }

    # -----------------------------------
    # Node 2: Handle Question
    # -----------------------------------

    def handle_question(state: RouterState) -> dict:

        response = llm.invoke(
            f"Answer this question: {state['query']}"
        )

        return {
            "response": f"[Answer] {response.content}"
        }

    # -----------------------------------
    # Node 3: Handle Command
    # -----------------------------------

    def handle_command(state: RouterState) -> dict:

        return {
            "response": (
                f"[Executing] I'll help you with: "
                f"{state['query']}"
            )
        }

    # -----------------------------------
    # Node 4: Handle Statement
    # -----------------------------------

    def handle_statement(state: RouterState) -> dict:

        return {
            "response": (
                f"[Acknowledged] Thanks for sharing: "
                f"{state['query']}"
            )
        }

    # -----------------------------------
    # Conditional Routing Function
    # -----------------------------------

    def route_by_type(
        state: RouterState,
    ) -> Literal["question", "command", "statement"]:

        qt = state["query_type"]

        if "question" in qt:
            return "question"

        elif "command" in qt:
            return "command"

        else:
            return "statement"

    # -----------------------------------
    # Create Graph
    # -----------------------------------

    graph = StateGraph(RouterState)

    # -----------------------------------
    # Add Nodes
    # -----------------------------------

    graph.add_node(
        "classify_query",
        classify_query
    )

    graph.add_node(
        "handle_question",
        handle_question
    )

    graph.add_node(
        "handle_command",
        handle_command
    )

    graph.add_node(
        "handle_statement",
        handle_statement
    )

    graph.add_edge(
        START,
        "classify_query"
    )

    # -----------------------------------
    # Conditional Edge
    # -----------------------------------

    graph.add_conditional_edges(
        "classify_query",
        route_by_type,
        {
            "question": "handle_question",
            "command": "handle_command",
            "statement": "handle_statement",
        }
    )

    # -----------------------------------
    # Connect Nodes to END
    # -----------------------------------

    graph.add_edge(
        "handle_question",
        END
    )

    graph.add_edge(
        "handle_command",
        END
    )

    graph.add_edge(
        "handle_statement",
        END
    )

    # -----------------------------------
    # Compile Graph
    # -----------------------------------

    app = graph.compile()


    png_bytes = app.get_graph().draw_mermaid_png()

    with open("graph3.png", "wb") as f:
        f.write(png_bytes)

    print("Graph saved as graph.png")


    # -----------------------------------
    # Test Queries
    # -----------------------------------

    queries = [
        "What is Artificial Intelligence?",
        "Explain how APIs work.",
        "Start the application.",
        "Artificial Intelligence is changing the world."
    ]

    # -----------------------------------
    # Run Graph
    # -----------------------------------

    for query in queries:

        result = app.invoke(
            {
                "query": query,
                "query_type": "",
                "response": ""
            }
        )

        print("\n" + "=" * 60)
        print("Query:", result["query"])
        print("Query Type:", result["query_type"])
        print("Response:", result["response"])


# -----------------------------------
# Main
# -----------------------------------

if __name__ == "__main__":
    demo_basic_routing()