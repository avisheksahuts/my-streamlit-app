import streamlit as st
import pandas as pd
import numpy as np

st.title("Session 2 · Part C · Streamlit App")
st.write("Welcome to my interactive data visualization app!")

# Interactive slider
slider_val = st.slider("Select a value", 1, 100, 50)
st.write(f"You selected: {slider_val}")

# Generate sample chart data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Display line chart
st.line_chart(chart_data)
