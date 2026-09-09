import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


st.title("🤖 AI Chatbot")

st.caption(
    "Chat with an OpenAI model using Streamlit"
)


st.sidebar.title("⚙️ Settings")


model = st.sidebar.selectbox(
    "Select Model",
    [
        "gpt-4o-mini"
    ]
)


temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)


if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


prompt = st.chat_input(
    "Ask me anything..."
)


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(

                    model=model,

                    messages=st.session_state.messages,

                    temperature=temperature,

                    max_tokens=500
                )


                answer = response.choices[0].message.content

                st.markdown(answer)


                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


                if response.usage:

                    st.caption(
                        f"Tokens used: "
                        f"{response.usage.total_tokens}"
                    )


            except Exception as e:

                st.error(
                    f"Error: {e}"
                )