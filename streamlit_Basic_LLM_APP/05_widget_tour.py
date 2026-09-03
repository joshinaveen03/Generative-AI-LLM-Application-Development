import streamlit as st
import pandas as pd

st.title("Widget Tour")

st.subheader("Display commands")

st.write("**bold**, *italic*, or literally any Python object")

st.markdown("- bullet one\n- bullet two")

st.code("print('hello')", language="python")

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 92, 78]
})

st.dataframe(df)

st.metric("Tokens used", 1420, "+120")

st.json({"role": "user", "content": "hi"})

st.success("Done")

st.warning("Slow")

st.error("Failed")

st.divider()

st.subheader("Input widgets")

test = st.text_input("Small Text Area")

essay = st.text_area("Larger Text Area")

temp = st.slider("Temperature", 0.0, 1.0)

model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o"])

tags = st.multiselect("Tags", ["code", "chat", "summary"])

fast = st.toggle("Stream the answer")

go = st.button("Generate", type="primary")