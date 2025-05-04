import streamlit as st
import pandas as pd

st.title("📊 Sri Lanka Financial Indicators Dashboard")

# Load your data
df = pd.read_csv("cleaned_financial_data.csv")

# Select indicator
indicator = st.selectbox("Choose an Indicator:", df['Indicator Name'].unique())

# Filter by selected indicator
filtered_df = df[df['Indicator Name'] == indicator]

# Year range selection
min_year = int(filtered_df['Year'].min())
max_year = int(filtered_df['Year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Apply filter
filtered_df = filtered_df[(filtered_df['Year'] >= year_range[0]) & (filtered_df['Year'] <= year_range[1])]

# Show line chart
st.line_chart(filtered_df.set_index('Year')['Value'])
