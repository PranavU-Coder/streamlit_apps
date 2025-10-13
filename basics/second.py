import streamlit as st
import os

st.title("This is a Title")
st.header("Hello")
st.subheader("World")
st.markdown("_readme.md_")
st.caption("Fuck this world")

code_example = """
def greet(name):
    print("Hello",name)
"""
st.code(code_example, language='python')

st.divider()

st.image(os.path.join(os.getcwd(), 'static', 'wallpaper.jpg'))