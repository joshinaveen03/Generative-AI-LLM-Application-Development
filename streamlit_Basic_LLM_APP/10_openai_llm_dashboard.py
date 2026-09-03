import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.title("OpenAI LLM Dashboard")

st.write("A simple Streamlit + OpenAI application")

with st.sidebar:
    st.header("Model Settings")

    model = st.selectbox(
        "Model",
        [
            "gpt-5.4-mini",
            "gpt-5.4",
            "gpt-5.4-nano"
        ]
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.5
    )

    st.write("Selected Model:", model)
    st.write("Temperature:", temperature)


left, right = st.columns(2)

input_metric = left.empty()
output_metric = right.empty()

input_metric.metric("Input tokens", 0)
output_metric.metric("Output tokens", 0)


chat_tab, log_tab = st.tabs(["Chat", "Logs"])


with chat_tab:

    st.subheader("Ask OpenAI")

    with st.form("ask_form"):

        question = st.text_area(
            "Your question",
            height=100,
            placeholder="Ask OpenAI anything..."
        )

        submitted = st.form_submit_button(
            "Ask",
            type="primary"
        )

    if submitted:

        if question.strip():

            try:

                with st.spinner("OpenAI is thinking..."):

                    response = client.responses.create(
                        model=model,
                        input=question,
                        temperature=temperature
                    )

                answer = response.output_text

                st.success("Response received!")

                st.write("### You")
                st.write(question)

                st.write("### OpenAI")
                st.write(answer)

                if response.usage:

                    input_tokens = response.usage.input_tokens
                    output_tokens = response.usage.output_tokens

                    input_metric.metric(
                        "Input tokens",
                        input_tokens
                    )

                    output_metric.metric(
                        "Output tokens",
                        output_tokens
                    )

                st.session_state["last_response"] = response.model_dump()

            except Exception as e:

                st.error(f"Error: {e}")

        else:

            st.warning("Please enter a question.")


with log_tab:

    st.subheader("Application Logs")

    if "last_response" in st.session_state:

        st.json(
            st.session_state["last_response"]
        )

    else:

        st.info("No OpenAI request yet.")


with st.expander("Show Raw OpenAI Response"):

    if "last_response" in st.session_state:

        st.json(
            st.session_state["last_response"]
        )

    else:

        st.write("Submit a question to see the response.")