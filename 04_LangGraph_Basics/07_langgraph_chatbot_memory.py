# Create a LangGraph chatbot application that maintains a conversation history using a 
# message-based State. The application should take user messages, store them in 
# state["messages"], send the complete conversation history to an OpenAI LLM, append 
# the AI response to the message history, display the latest response, and continue
# the conversation until the user types exit.

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, BaseMessage

load_dotenv()


class MessageState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def chat_node(state: MessageState) -> dict:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


graph = StateGraph(MessageState)

graph.add_node("chat", chat_node)

graph.add_edge(START, "chat")
graph.add_edge("chat", END)

app = graph.compile()


messages = []

print("Chatbot started. Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append(HumanMessage(content=user_input))

    result = app.invoke({
        "messages": messages
    })

    messages = result["messages"]

    print("Bot:", messages[-1].content)