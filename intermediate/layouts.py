import streamlit as st

st.sidebar.title("this is a sidebar")
st.sidebar.write("it is possible to place elements like buttons, sliders and text here")
sidebar_input = st.sidebar.text_input("Enter anything you want here")

tab1, tab2, tab3 = st.tabs(["Tab1","Tab2","Tab3"])

with tab1:
    st.write("you are in tab 1")

with tab2:
    st.write("you are in tab 2")
    
with tab3:
    st.write("you are in tab 3")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("content for column 1")

with col2:
    st.header("Column 2")
    st.write("content for column 2")

with st.container(border=True):
    st.write("This is inside a container")
    st.write("You can think of a container as a grouping of elements")
    st.write("Containers help manage contents of a page")

placeholder = st.empty()
placeholder.write("This is a placeholder, useful for empty content")

if st.button("updating placeholder"):
    placeholder.write("Content to be updated")

with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default")
    st.write("expanders are useful for keeping interface clean")

st.write("Hover over this button for tooltip")
st.button("Button with tooltip", help="This is a tooltip or popover on hover")

if sidebar_input:
    st.write(f"You entered in sidebar : {sidebar_input}")