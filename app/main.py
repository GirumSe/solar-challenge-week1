# Solar Data Dashboard
# This is a Streamlit app for visualizing solar radiation data
# It allows users to select countries and metrics for comparison.
# Import necessary libraries

import streamlit as st



st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("☀️ Solar Radiation Comparison Dashboard")

st.sidebar.header("Filter Options")
st.write("Welcome to the solar data comparison dashboard!")

selected_countries = st.sidebar.multiselect(
    "Select countries to compare:",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

selected_metric = st.sidebar.selectbox(
    "Select solar metric to visualize:",
    options=["GHI", "DNI", "DHI"]
)


