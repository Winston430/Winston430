import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("app with a data table")

st.write("This app shows a data table")

st.dataframe(df)
