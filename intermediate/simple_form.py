import streamlit as st
import pandas as pd

st.title("Good Morning!")

with st.form(key="sample form"):

    st.subheader("Inputs")
    name = st.text_input("enter your name")
    feedback = st.text_area("provide your feedback")

    st.subheader("date and time")
    dob = st.date_input("select your date of birth")
    time = st.time_input("select your preferred time")

    st.subheader("selections")
    choice = st.selectbox("select your gender", ['Male', 'Female'])
    rating = st.select_slider("give your ratings please", [1,2,3,4,5])

    st.subheader("toggles and checkboxes")
    notif = st.checkbox('Recieve Notifications aye ?')
    toggle_value = st.checkbox('Enable dark mode sire!')

    submit_button = st.form_submit_button(label='submit')