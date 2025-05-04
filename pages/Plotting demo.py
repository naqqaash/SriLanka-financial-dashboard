import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Plotting Demo")

df = pd.read_csv("cleaned_financial_data.csv")

indicator = st.selectbox("Select an Indicator", df['Indicator Name'].unique())
filtered = df[df['Indicator Name'] == indicator]

fig, ax = plt.subplots()
ax.plot(filtered["Year"], filtered["Value"], marker='o')
ax.set_title(f"{indicator} over Years")
ax.set_xlabel("Year")
ax.set_ylabel("Value")

st.pyplot(fig)
