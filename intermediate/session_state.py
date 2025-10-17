import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Press Me"):
    st.session_state.counter+=1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write("The counter didn't reset")

st.write(f"Counter value : {st.session_state.counter}")