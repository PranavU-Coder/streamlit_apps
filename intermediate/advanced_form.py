import streamlit as st
from datetime import datetime

min_date = datetime(2000,1,1)
max_date = datetime.now()

st.title("User Information Form")

with st.form(key="user_info_form", clear_on_submit=True):

    name = st.text_input("Enter Your Name!")
    birth_date = st.date_input("Enter your birthday", min_value=min_date, max_value=max_date)

    if birth_date:
        age = max_date.year - birth_date.year
        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -=1
        st.write(f"Your age is {age} years")
    submit_button = st.form_submit_button(label="Submit Form")

    if submit_button:
        if not name or not birth_date:
            st.warning("Please fill out the details before you submit!")
        else:
            st.success(f"Thank You, Your name is {name} and you are {age} years old!")
            st.balloons()