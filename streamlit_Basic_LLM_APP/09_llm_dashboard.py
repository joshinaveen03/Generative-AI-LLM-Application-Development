import streamlit as st

raw = {
    "message": "Hello",
    "status": "success"
}

st.title("LLM Dashboard")

st.write("A simple Streamlit layout example")

with st.sidebar:
    st.header("Model Settings")

    model = st.selectbox(
        "Model",
        ["gpt-4o-mini", "claude", "qwen3.5"]
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

left.metric(
    "Input tokens",
    812
)

right.metric(
    "Output tokens",
    240
)

chat_tab, log_tab = st.tabs(["Chat", "Logs"])

with chat_tab:

    st.subheader("Ask the AI")

    with st.form("ask_form"):

        question = st.text_area(
            "Your question",
            height=100,
            placeholder="Type your question here..."
        )

        submitted = st.form_submit_button(
            "Ask",
            type="primary"
        )

    if submitted:

        if question.strip():

            st.success("Question submitted!")

            st.write("You asked:")
            st.write(question)

            st.write("Model:", model)
            st.write("Temperature:", temperature)

        else:

            st.warning("Please enter a question.")

with log_tab:

    st.subheader("Application Logs")

    st.write("These are the logs.")

    st.json(raw)

with st.expander("Show Raw Response"):

    st.write(raw)

    st.json({
        "message": "Hello",
        "status": "success",
        "model": model,
        "temperature": temperature
    })