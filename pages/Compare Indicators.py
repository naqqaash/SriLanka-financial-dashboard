import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Compare Two Indicators")

df = pd.read_csv("cleaned_financial_data.csv")

indicators = df['Indicator Name'].unique()
col1, col2 = st.columns(2)

ind1 = col1.selectbox("Indicator 1", indicators)
ind2 = col2.selectbox("Indicator 2", indicators, index=1)

filtered = df[df['Indicator Name'].isin([ind1, ind2])]

chart = alt.Chart(filtered).mark_line().encode(
    x='Year:O',
    y='Value:Q',
    color='Indicator Name:N',
    tooltip=['Year', 'Value', 'Indicator Name']
).interactive()

st.altair_chart(chart, use_container_width=True)
