# Solar Data Dashboard
# This is a Streamlit app for visualizing solar radiation data
# It allows users to select countries and metrics for comparison.
# Import necessary libraries

import streamlit as st
from utils import load_clean_data, plot_boxplot

# --- Title and Sidebar ---
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("☀️ Solar Radiation Comparison Dashboard")

# --- Sidebar ---
st.sidebar.header("Filter Options")
st.write("Welcome to the solar data comparison dashboard!")

# Country name -> ID mapping
country_id_map = {
    "Benin": "benin-malanville",
    "Sierra Leone": "sierraleone-bumbuna",
    "Togo": "togo-dapaong_qc"
}

# Show user-friendly names in the multiselect
selected_country_names = st.sidebar.multiselect(
    "Select countries to compare:",
    options=list(country_id_map.keys()),
    default=["Benin", "Sierra Leone", "Togo"]
)

# Convert selected names to IDs
selected_country_ids = [country_id_map[name] for name in selected_country_names]

# Metric selection
selected_metric = st.sidebar.selectbox(
    "Select solar metric to visualize:",
    options=["GHI", "DNI", "DHI"]
)

# --- Load and Visualize Data ---
df = load_clean_data(selected_country_ids)

st.subheader(f"Distribution of {selected_metric} Across Selected Countries")
plot_boxplot(df, selected_metric)