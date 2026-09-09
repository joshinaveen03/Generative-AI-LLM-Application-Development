from langgraph.graph import StateGraph, START,END
from typing_extensions import TypedDict

#create State
class State(TypedDict):
    # text:str
    message:str

#Create Node
def process_text(state:State):
    return{
        "message":state["message"].upper()

    }
def create_message(state: State):
    return {
        "message": f"Final Text: {state['message']}"
    }
# Create Graph
graph = StateGraph(State)

# Add Nodes
graph.add_node("process_text", process_text)
graph.add_node("create_message", create_message)

# Add Edges
graph.add_edge(START, "process_text")
graph.add_edge("process_text", "create_message")
graph.add_edge("create_message", END)

# Compile
app = graph.compile()

png_bytes = app.get_graph().draw_mermaid_png()

with open("graph3.png", "wb") as f:
    f.write(png_bytes)

print("Graph saved as graph.png")

# Run
result = app.invoke({
    "message": "langgraph is easy to learn"
})

print(result)