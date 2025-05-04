import streamlit as st
import pandas as pd

st.title("📋 Sri Lanka Economic Snapshot")

df = pd.read_csv("cleaned_financial_data.csv")

st.write("### 🧭 Browse Key Indicators")

years = sorted(df['Year'].unique())
selected_year = st.selectbox("Select Year", years, index=len(years)-1)


filtered = df[df['Year'] == selected_year]


st.dataframe(filtered[['Indicator Name', 'Value']].sort_values(by='Value', ascending=False))

st.write("Tip: You can sort and search the table above.")
