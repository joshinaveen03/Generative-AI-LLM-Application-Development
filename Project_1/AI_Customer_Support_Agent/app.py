import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# Get the directory where app.py is located
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

# Data folder inside the project
DATA_DIR = BASE_DIR / "Data"

# Make the data path available to other Python files
os.environ["DATA_DIR"] = str(DATA_DIR)

# OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# --------------------------------------------------
# Import assistant AFTER setting DATA_DIR
# --------------------------------------------------
from assistant import run_assistant


# --------------------------------------------------
# Verify Data folder
# --------------------------------------------------
if not DATA_DIR.exists():
    st.error(f"Data folder not found: {DATA_DIR}")
else:
    st.sidebar.success("✅ Data folder found")

    # Optional: show number of files
    data_files = list(DATA_DIR.rglob("*"))
    file_count = sum(1 for f in data_files if f.is_file())

    st.sidebar.write(f"📁 Data files: {file_count}")


# --------------------------------------------------
# Streamlit configuration
# --------------------------------------------------
st.set_page_config(
    page_title="ShopAssist AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 ShopAssist AI")
st.caption("Tool-powered customer support assistant")


# --------------------------------------------------
# Sidebar
# --------------------------------------------------
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


# --------------------------------------------------
# Chat history
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I am ShopAssist. "
                "I can help with orders, products and policies."
            )
        }
    ]


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# User input
# --------------------------------------------------
user_prompt = st.chat_input(
    "Ask about an order, product or policy..."
)


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
