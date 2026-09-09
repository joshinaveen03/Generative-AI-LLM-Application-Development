from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# -----------------------------------
# State
# -----------------------------------

class State(TypedDict):
    question: str
    answer: str
    improved_answer: str


# -----------------------------------
# LLM
# -----------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# -----------------------------------
# Node 1: Generate Answer
# -----------------------------------

def generate_answer(state: State):
    response = llm.invoke(
        f"Answer this question clearly for a beginner:\n{state['question']}"
    )

    return {
        "answer": response.content
    }


# -----------------------------------
# Node 2: Improve Answer
# -----------------------------------

def improve_answer(state: State):
    response = llm.invoke(
        f"""
Improve the following answer.

Question:
{state['question']}

Original Answer:
{state['answer']}

Make the answer simpler, clearer, and more beginner-friendly.
"""
    )

    return {
        "improved_answer": response.content
    }


# -----------------------------------
# Create Graph
# -----------------------------------

graph = StateGraph(State)

graph.add_node("generate_answer", generate_answer)
graph.add_node("improve_answer", improve_answer)


# -----------------------------------
# Add Edges
# -----------------------------------

graph.add_edge(START, "generate_answer")
graph.add_edge("generate_answer", "improve_answer")
graph.add_edge("improve_answer", END)


# -----------------------------------
# Compile
# -----------------------------------

app = graph.compile()


# -----------------------------------
# Run
# -----------------------------------

result = app.invoke({
    "question": "Explain how APIs work to a beginner.",
    "answer": "",
    "improved_answer": ""
})


# -----------------------------------
# Output
# -----------------------------------

print("Question:")
print(result["question"])

print("\nOriginal Answer:")
print(result["answer"])

print("\nImproved Answer:")
print(result["improved_answer"])