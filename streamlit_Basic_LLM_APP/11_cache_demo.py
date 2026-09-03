import streamlit as st
import time


@st.cache_data(ttl=3600)
def slow_square(n: int) -> int:
    time.sleep(3)
    return n * n


@st.cache_resource
def get_counter():
    return {"calls": 0}


st.title("Cache Demo")

n = st.number_input(
    "Pick a number",
    1,
    100,
    5
)

if st.button("Calculate"):

    start = time.time()

    result = slow_square(n)

    elapsed = time.time() - start

    counter = get_counter()
    counter["calls"] += 1

    st.write("Result:", result)
    st.write("Time:", round(elapsed, 2), "seconds")
    st.write("Cache calls:", counter["calls"])