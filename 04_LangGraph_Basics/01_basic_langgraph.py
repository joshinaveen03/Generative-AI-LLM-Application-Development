from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. Create State
class State(TypedDict):
    input: str
    output: str


# 2. Create Node
def process(state: State):
    return {
        "output": state["input"].upper()
    }


# 3. Create Graph
graph = StateGraph(State)


# 4. Add Node
graph.add_node("process", process)


# 5. Add Edges
graph.add_edge(START, "process")
graph.add_edge("process", END)


# 6. Compile
app = graph.compile()


# 7. Run Graph
result = app.invoke({
    "input": "hello langgraph",
    "output": ""
})


# 8. Display Result
print(result)