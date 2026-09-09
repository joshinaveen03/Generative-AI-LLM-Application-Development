from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

from graphMsgState import QAState


def exercise_QA_langgraph():

    # -----------------------------------
    # Initialize LLM
    # -----------------------------------

    llm = init_chat_model(
        model="gpt-4o-mini",
        temperature=0.0
    )

    # -----------------------------------
    # Node 1: Generate Questions
    # -----------------------------------

    def generate_questions(state: QAState) -> dict:

        prompt = (
            f"Generate 3 questions about the topic: {state['topic']}\n"
            "Format: numbered list"
        )

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return {
            "questions": response.content
        }

    # -----------------------------------
    # Node 2: Answer Questions
    # -----------------------------------

    def answer_questions(state: QAState) -> dict:

        prompt = (
            f"Answer the following questions: "
            f"{state['questions']}"
        )

        response = llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return {
            "answer": response.content
        }

    # -----------------------------------
    # Create LangGraph
    # -----------------------------------

    graph = StateGraph(QAState)

    # Add nodes
    graph.add_node(
        "generate_questions",
        generate_questions
    )

    graph.add_node(
        "answer_questions",
        answer_questions
    )

    # Add edges
    graph.add_edge(
        START,
        "generate_questions"
    )

    graph.add_edge(
        "generate_questions",
        "answer_questions"
    )

    graph.add_edge(
        "answer_questions",
        END
    )

    # -----------------------------------
    # Compile Graph
    # -----------------------------------

    app = graph.compile()

    # -----------------------------------
    # Run Graph
    # -----------------------------------

    result = app.invoke(
        {
            "topic": "Artificial Intelligence",
            "questions": "",
            "answer": ""
        }
    )

    # -----------------------------------
    # Display Result
    # -----------------------------------

    print("QA LangGraph Result:")
    print("--------------------")

    print(f"Topic: {result['topic']}")

    print(f"\nQuestions:\n{result['questions']}")

    print(f"\nAnswer:\n{result['answer']}")


# -----------------------------------
# Main
# -----------------------------------

if __name__ == "__main__":
    exercise_QA_langgraph()