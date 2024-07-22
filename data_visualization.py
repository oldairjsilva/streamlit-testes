import streamlit as st
import pandas as pd
import altair as alt

data = pd.read_csv("https://github.com/mitmath/6S083/blob/master/problem_sets/some_data.csv", sep=",")

chart = alt.Chart(data).mark_line().encode(
    x = 'X_axis_column_name',
    y = 'Y_axis_column_name',
    color = 'Category_column_name'
)

st.altair_chart(chart, use_container_width=True)
