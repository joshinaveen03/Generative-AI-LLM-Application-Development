import streamlit as st
import pandas as pd

st.title("Report")
st.subheader("Details")

st.write("**bold text**,or any object")

st.markdown("-item one\n -item two")

st.code("print('Hi')",language="Python")

df=pd.DataFrame({
    "Name": ["Naveen","Joshi","Ravi"],
    "Score":[85,92,78]
    })
st.dataframe(df)

st.metric("Tokens Used",1420,"+120")

st.json({"role":"user"})

st.success("Done")
st.warning("slow")
st.error("Failed")