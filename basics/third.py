import streamlit as st
import pandas as pd

st.title("streamlit elements")

st.divider()

# DATAFRAME SELECTION

st.subheader("dataframe")
df = pd.DataFrame({
    'Name' : ['Pranav', 'Noorit'],
    'Age' : [19,19],
    'Degree' : ['Electronics', 'Computer']
})

st.dataframe(df)

# EDITABLE DATAFRAME

st.subheader("data editor")
editable_df = st.data_editor(df)

# STATIC TABLE SELECTION

st.subheader("static table")
st.table(df)

st.divider()

# METRICS SELECTION

st.subheader('metrics')
st.metric(label='total rows', value=len(df))
st.metric(label='avg age of employees', value=round(df['Age'].mean(),1))

# JSON AND DICTIONARY SECTION

st.subheader('JSON and dictionary section')
sample_dict = {
    'name' : 'Pranav Unni',
    'age' : 19,
    'skills' : ['python', 'data science', 'machine-learning']
}

st.json(sample_dict)

st.write('dictionary view : ', sample_dict)