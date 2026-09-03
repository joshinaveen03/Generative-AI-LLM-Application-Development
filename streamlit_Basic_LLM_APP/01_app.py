# pip install streamlit
# streamlit --version
# streamlit run app.py

import streamlit as st

st.title("My First AI App")

name = st.text_input("Your Name")

if name:
    st.write("Hello", name, "!")

