import streamlit as st

st.title("Broken Counter")

count = 0

if st.button("Add one"):
    count = count + 1

st.write("Count is", count)

