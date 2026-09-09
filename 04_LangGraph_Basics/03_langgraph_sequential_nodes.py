from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict


# Step 1: Create State
class State(TypedDict):
    text: str
    message: str


# Step 2: Create Nodes
def process_text(state: State):
    return {
        "text": state["text"].upper()
    }


def create_message(state: State):
    return {
        "message": f"Final Text: {state['text']}"
    }


# Step 3: Create Graph
graph = StateGraph(State)


# Step 4: Add Nodes
graph.add_node("process_text", process_text)
graph.add_node("create_message", create_message)





# Step 6: Compile
app = graph.compile()


# Run
result = app.invoke({
    "text": "langgraph is easy to learn"
})

print(result)