import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("cleaned_financial_data.csv")


indicator = st.selectbox("Select Indicator", df['Indicator Name'].unique())


filtered = df[df['Indicator Name'] == indicator]
years = filtered['Year'].unique()


st.title(f"🎞️ Animated Time-Series for {indicator}")


fig, ax = plt.subplots()
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.set_title(f"{indicator} Over Time")

line, = ax.plot([], [], marker='o', color='b', label=indicator)
ax.legend(loc="upper left")

ax.set_xlim(min(years), max(years))
ax.set_ylim(filtered['Value'].min(), filtered['Value'].max())


progress_bar = st.progress(0)


for i in range(len(years)):
    
    current_year_data = filtered[filtered['Year'] <= years[i]]
    
    
    line.set_data(current_year_data['Year'], current_year_data['Value'])
    
    
    st.pyplot(fig)

    
    progress_bar.progress((i + 1) / len(years))
    
    
    time.sleep(0.1)

st.success(f"Animation Complete for {indicator}!")
