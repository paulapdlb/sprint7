import streamlit as st
import pandas as pd

st.title("Explorador de Vehículos")

df = pd.read_csv("vehicles_us.csv")
st.dataframe(df)

