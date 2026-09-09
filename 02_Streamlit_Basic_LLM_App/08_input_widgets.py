import streamlit as st

name = st.text_input("Name", "Naveen Joshi")

essay = st.text_area("Prompt", height=100)

temp = st.slider("Temperature", 0.0, 1.0, 0.7)

model = st.selectbox("Model", ["gpt-4o-mini", "Claude", "qwen3.5"])

tags = st.multiselect("Tags", ["code", "chat"])

fast = st.toggle("Stream the answer", value=True)

top_k = st.number_input("Top_K", 1, 20, 5)

go = st.button("Generate", type="primary")

st.write(model, temp, go)