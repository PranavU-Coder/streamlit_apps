import streamlit as st

def next(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2
def back():
    st.session_state.step = 1

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

if st.session_state.step == 1:
    st.header("Part 1: Info")

    name = st.text_input("Name", value=st.session_state.info.get("name",""))

    st.button("Next", on_click=next,args=(name,))

elif st.session_state.step == 2:
    st.header("Part 2: Review")

    st.subheader("Please review this")
    st.write(f"**Name** : {st.session_state.info.get('name','')}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info["name"]

    st.button("Back", on_click=back)