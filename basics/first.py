import streamlit as st

# default state of a button is False, once pressed it becomes and remains True, if refresed returns to False

first_button = st.button("press me")
print(first_button)

# incase of multiple buttons , regardless of whether a button was pressed or not, if (n-1)th button was pressed and later now nth button is pressed
# it would still indicate that the nth button is True and (n-1)th button is False.

second_button = st.button("now press me instead")
print(second_button)