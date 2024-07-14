import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/code/027e657f961692e685aff038f73122e68dc9ad1c/streamlit/part3/penguins_cleaned.csv")

c = (
   alt.Chart(df)
   .mark_circle()
   .encode(x="bill_length_mm", y="body_mass_g", color="species")
)

st.title("🦆 My Scatter Plot")
st.altair_chart(c, use_container_width=True)
