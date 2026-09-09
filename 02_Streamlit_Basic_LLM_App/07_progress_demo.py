import streamlit as st
import time

with st.spinner("Thinking..."):
    time.sleep(2)
    st.success("Done")

progress = st.progress(0)

for i in range(100):
    time.sleep(0.02)
    progress.progress(i + 1)