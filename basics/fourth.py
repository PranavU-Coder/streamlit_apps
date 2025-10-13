import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('title')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.subheader('area chart')
st.area_chart(chart_data)

st.subheader('bar chart')
st.bar_chart(chart_data)

st.subheader('line chart')
st.line_chart(chart_data)

st.subheader('scatter chart')
scatter_data = pd.DataFrame({
    'x' : np.random.randn(100),
    'y' : np.random.randn(100)
})
st.scatter_chart(scatter_data)

st.subheader('map')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50,50] + [37.76, -122.4], # CO-ORDINATES AROUND SF
    columns=['lat','lon']
)
st.map(map_data)

st.subheader('pyplot chart')
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title('pyplot line chart')
ax.legend()
st.pyplot(fig)