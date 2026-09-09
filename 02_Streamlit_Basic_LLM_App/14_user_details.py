import streamlit as st

st.title("My First AI App")

name = st.text_input("Your Name")
number = st.number_input("Age")

if name:
    st.write("Hello", name, "!")
    st.write("Age:", number)