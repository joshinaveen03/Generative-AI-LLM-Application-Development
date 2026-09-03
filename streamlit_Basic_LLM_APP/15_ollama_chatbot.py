import streamlit as st
import ollama

st.set_page_config(
    page_title="Ollama Chatbot",
    page_icon="🤖"
)

st.title("🤖 Ollama Chatbot")
st.caption("Powered by Qwen 3 1.7b")

MODEL = "qwen3:1.7b"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask something..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        try:
            response = ollama.chat(
                model=MODEL,
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]

            st.write(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.error(f"Ollama Error: {e}")