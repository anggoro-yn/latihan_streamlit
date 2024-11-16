import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Latiham Membuat Webapp Streamlit")

st.write("Di malam Minggu belajar membuat webapp streamlit menghabiskan malam Minggu dengan produktif.")

df = pd.read_csv("titanic.csv")
st.write(df)

df_cleaned = df.dropna(subset=['Age'])
st.write(df_cleaned)

# Membuat pie chart persentasi kelas penumpang
st.markdown("## Perbandingan Kelas Penumpang")
class_count = df_cleaned['Pclass'].value_counts()

fig, ax = plt.subplots()
ax.pie(class_count, labels = class_count.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')

st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(df_cleaned['Age'], bins = 10)
ax.set_xlabel('Age')
ax.set_ylabel('Number of passengers')
ax.set_title('Histrogram Usia Penumpang')
st.pyplot(fig)

df_male = df_cleaned[df_cleaned['Sex']== 'male']
fig, ax = plt.subplots()
ax.hist(df_male['Age'], bins = 10)
st.pyplot(fig)
