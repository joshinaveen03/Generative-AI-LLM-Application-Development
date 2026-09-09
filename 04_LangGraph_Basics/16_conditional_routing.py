# Create an OpenAI agent with the following tools:
    # add()
    # multiply()
# The agent should decide which tool to use based on the user's prompt.
# Test with:
    # "What is 20 + 30?"
    # "What is 12 * 8?"
    # "What is 12 + 8 and 12 * 8"

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()


# -------------------------
# 1. Create your own State
# -------------------------

class State(TypedDict):
    messages: Annotated[list, add_messages]
    a: int
    b: int
    result: int


# -------------------------
# 2. Create Tools
# -------------------------

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


tools = [add, multiply]


# -------------------------
# 3. Create Model
# -------------------------

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

model_with_tools = model.bind_tools(tools)


# -------------------------
# 4. Chatbot Node
# -------------------------

def chatbot(state: State):

    response = model_with_tools.invoke(state["messages"])

    return {
        "messages": [response]
    }


# -------------------------
# 5. Conditional Routing
# -------------------------

def route(state: State):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END


# -------------------------
# 6. Tool Node
# -------------------------

tool_node = ToolNode(tools)


# -------------------------
# 7. Create Graph
# -------------------------

graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chatbot")


# Conditional routing
graph.add_conditional_edges(
    "chatbot",
    route,
    {
        "tools": "tools",
        END: END
    }
)

graph.add_edge("tools", "chatbot")
# -------------------------
# 8. Compile
# -------------------------

app = graph.compile()
 # visualize the graph
print("\n--- Mermaid Graph ---")
print(app.get_graph().draw_mermaid())
 
    # save as PNG
png_bytes = app.get_graph().draw_mermaid_png()
with open("graph_14.png", "wb") as f:
    f.write(png_bytes)
print("\nGraph saved to graph.png")

# -------------------------
# 9. Test
# -------------------------

questions = [
    "What is 20 + 30?",
    "What is 12 * 8?",
    "What is 12 + 8 and 12 * 8?"
]


for question in questions:

    result = app.invoke({
        "messages": [
            ("user", question)
        ],
        "a": 0,
        "b": 0,
        "result": 0
    })

    print("\nQuestion:", question)
    print("Answer:", result["messages"][-1].content)