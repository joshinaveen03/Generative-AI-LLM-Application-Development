# Create a LangGraph application that takes a topic from the State,
# uses an OpenAI LLM to generate exactly three questions about that topic, 
# stores them in state["questions"], then takes the first generated question, 
# sends it to the OpenAI LLM, stores the generated response in state["answer"],
# and displays the topic, all three questions, and the final answer.


from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="gpt-4o-mini",
    temperature=0.0
)


class TopicState(TypedDict):
    topic: str
    questions: list[str]
    answer: str


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


def answer_question(state: TopicState) -> dict:
    question = state["questions"][0]

    response = llm.invoke(
        f"Answer this question clearly:\n{question}"
    )

    return {
        "answer": response.content
    }


graph = StateGraph(TopicState)

graph.add_node("generate_questions", generate_questions)
graph.add_node("answer_question", answer_question)

graph.add_edge(START, "generate_questions")
graph.add_edge("generate_questions", "answer_question")
graph.add_edge("answer_question", END)

app = graph.compile()


result = app.invoke({
    "topic": "Artificial Intelligence",
    "questions": [],
    "answer": ""
})

print("Topic:", result["topic"])
print("\nQuestions:")

for question in result["questions"]:
    print("-", question)

print("\nAnswer:")
print(result["answer"])