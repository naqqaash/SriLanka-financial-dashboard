import streamlit as st
import pandas as pd

st.title("📈 Overview Dashboard")

df = pd.read_csv("cleaned_financial_data.csv")

indicator = st.selectbox("Select an Indicator", df['Indicator Name'].unique())

filtered = df[df['Indicator Name'] == indicator]

st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Min Value", f"{filtered['Value'].min():,.2f}")
col2.metric("Max Value", f"{filtered['Value'].max():,.2f}")
col3.metric("Average", f"{filtered['Value'].mean():,.2f}")

st.line_chart(filtered.set_index("Year")["Value"])
