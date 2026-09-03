import streamlit as st

print("SCRIPT STARTED")

n = st.slider("How Many", 1, 10, 2)

st.write("You Picked", n)

print("SCRIPT FINISHED")