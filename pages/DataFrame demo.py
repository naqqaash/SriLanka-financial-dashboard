import streamlit as st
import pandas as pd

st.title("📄 DataFrame Demo")

df = pd.read_csv("cleaned_financial_data.csv")
st.write("Here is a preview of the data:")
st.dataframe(df.head())
