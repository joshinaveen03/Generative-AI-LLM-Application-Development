import streamlit as st
from dotenv import load_dotenv
from assistant import run_assistant
import os

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="ShopAssist AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ShopAssist AI")
st.caption("Tool-powered customer support assistant")

with st.sidebar:
    st.header("Available Tools")
    st.write("📦 Order lookup")
    st.write("🛍️ Product lookup")
    st.write("🔎 Product search")
    st.write("📄 Policy lookup")

    st.divider()
    st.subheader("Example Questions")
    st.write("Where is order ORD-1001?")
    st.write("Tell me about product P102")
    st.write("Show computer accessories")
    st.write("What is your return policy?")
    st.write("How long does a refund take?")

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "Hello! I am ShopAssist. "
            "I can help with orders, products and policies."
        )
    }]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Ask about an order, product or policy...")

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    conversation_history = st.session_state.messages.copy()

    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    with st.chat_message("assistant"):
        with st.spinner("Checking..."):
            try:
                response = run_assistant(
                    user_prompt,
                    conversation_history
                )
            except Exception as error:
                response = f"Something went wrong: {error}"

        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
