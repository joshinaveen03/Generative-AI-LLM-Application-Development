import streamlit as st
from openai import OpenAI

st.title("Ask the model")

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

q = st.text_area("Your question")

temp = st.slider(
    "Temperature",
    0.0,
    1.0,
    0.7
)

if st.button("Ask") and q:

    with st.spinner("Thinking..."):

        try:
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": q
                    }
                ],
                temperature=temp,
                max_tokens=300
            )

            st.write(
                resp.choices[0].message.content
            )

            st.caption(
                f"Tokens used: {resp.usage.total_tokens}"
            )

        except Exception as e:
            st.error(f"Error: {e}")