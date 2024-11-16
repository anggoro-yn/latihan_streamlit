import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Latiham Membuat Webapp Streamlit")

st.write("Di malam Minggu belajar membuat webapp streamlit menghabiskan malam Minggu dengan produktif.")

df = pd.read_csv("titanic.csv")
st.write(df)
