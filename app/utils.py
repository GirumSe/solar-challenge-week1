import pandas as pd
import streamlit as st

@st.cache_data
def load_clean_data(countries):
    df_list = []
    for country in countries:
        file_path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(file_path, parse_dates=['Timestamp'])
        df["Country"] = country
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)
