import streamlit as st
import pandas as pd
import numpy as np

st.title("🗺️ Mapping Demo")


data = pd.DataFrame({
    'lat': np.random.uniform(6.5, 9.5, 100),
    'lon': np.random.uniform(79.5, 81.5, 100),
})

st.map(data)
