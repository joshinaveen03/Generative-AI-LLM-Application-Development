# Create a simple LangGraph application that takes an input string and a step counter 
# from the State. The application should process the input by converting it to uppercase,
# store the processed text in state["output"], increment state["step"] by 1, display the 
# final State, and generate a Mermaid diagram of the graph and save it as a PNG image.

from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# LLM
llm = init_chat_model(
    model="gpt-4o-mini",
    temperature=0.0
)


class SimpleState(TypedDict):
    input: str
    output: str
    step: int



def process(state: SimpleState) -> dict:
    return {
        "output": state["input"].upper(),
        "step": state["step"] + 1
    }

graph = StateGraph(SimpleState)

graph.add_node("process", process)

graph.add_edge(START, "process")
graph.add_edge("process", END)

app = graph.compile()

print("\n--- Mermaid Graph ---")
print(app.get_graph().draw_mermaid())

png_bytes = app.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_bytes)

print("Graph saved as graph.png")


result = app.invoke({
    "input": "hello",
    "output": "",
    "step": 0
})

print("\nSimple graph result:", result)