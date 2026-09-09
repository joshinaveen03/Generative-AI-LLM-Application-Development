# Create a basic LangGraph application that takes a user's name from the State,
# passes it to a greeting node, generates a personalized welcome message, stores 
# the message in state["message"], displays the final message, and saves a visual 
# representation of the LangGraph workflow as a PNG image.



from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. Create the State
class State(TypedDict):
    name: str
    message: str

# 2. Create one node
def greet_user(state: State):
    return {
        "message": f"Hello, {state['name']}! Welcome to LangGraph."
    }

# 3. Create the graph
graph = StateGraph(State)

# Add the single node
graph.add_node("greet_user", greet_user)

# 4. Connect START → node → END
graph.add_edge(START, "greet_user")
graph.add_edge("greet_user", END)

# Compile the graph
app = graph.compile()

# print("\n--- Mermaid Graph ---")
# print(app.get_graph().draw_mermaid())

png_bytes = app.get_graph().draw_mermaid_png()

with open("graph1.png", "wb") as f:
    f.write(png_bytes)

print("Graph saved as graph.png")

# 5. Pass the name through the State
result = app.invoke({
    "name": "Naveen",
    "message": ""
})


# Output
print(result["message"])