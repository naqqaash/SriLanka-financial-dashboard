import streamlit as st
import pandas as pd

st.title("🏆 Top Years by Value")

df = pd.read_csv("cleaned_financial_data.csv")

indicator = st.selectbox("Select an Indicator", df['Indicator Name'].unique())
top_n = st.slider("Number of Top Years to Display", 3, 20, 5)

filtered = df[df['Indicator Name'] == indicator]
top_years = filtered.sort_values(by='Value', ascending=False).head(top_n)

st.write(f"Top {top_n} Years for {indicator}")
st.dataframe(top_years[['Year', 'Value']])
