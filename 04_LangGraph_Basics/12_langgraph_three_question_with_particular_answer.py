from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


# -----------------------------------
# LLM
# -----------------------------------

llm = init_chat_model(
    model="gpt-4o-mini",
    temperature=0.0
)


# -----------------------------------
# State
# -----------------------------------

class TopicState(TypedDict):
    topic: str
    questions: list[str]
    answers: list[str]


# -----------------------------------
# Generate Questions
# -----------------------------------

def generate_questions(state: TopicState) -> dict:

    response = llm.invoke(
        f"Generate exactly 3 questions about {state['topic']}. "
        "Return only the 3 questions, one per line."
    )

    questions = [
        line.strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    return {
        "questions": questions[:3]
    }


# -----------------------------------
# Answer Questions
# -----------------------------------

def answer_questions(state: TopicState) -> dict:

    answers = []

    for question in state["questions"]:

        response = llm.invoke(
            f"Answer this question clearly:\n{question}"
        )

        answers.append(response.content)

    return {
        "answers": answers
    }


# -----------------------------------
# Create Graph
# -----------------------------------

graph = StateGraph(TopicState)

graph.add_node("generate_questions", generate_questions)
graph.add_node("answer_questions", answer_questions)

graph.add_edge(START, "generate_questions")
graph.add_edge("generate_questions", "answer_questions")
graph.add_edge("answer_questions", END)


# -----------------------------------
# Compile
# -----------------------------------

app = graph.compile()


# -----------------------------------
# Run
# -----------------------------------

result = app.invoke({
    "topic": "Artificial Intelligence",
    "questions": [],
    "answers": []
})


# -----------------------------------
# Display
# -----------------------------------

print("Topic:", result["topic"])

print("\nQuestions and Answers:")

for i, (question, answer) in enumerate(
    zip(result["questions"], result["answers"]), 1
):
    print(f"\nQuestion {i}:")
    print(question)

    print("\nAnswer:")
    print(answer)