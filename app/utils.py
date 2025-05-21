import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_clean_data(countries, name_map=None):
    df_list = []
    for country_id in countries:
        file_path = f"data/{country_id.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(file_path, parse_dates=['Timestamp'])
        # Use readable name if mapping is provided
        country_display_name = name_map[country_id] if name_map else country_id
        df["Country"] = country_display_name
        df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

def plot_boxplot(df, column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="Country", y=column, ax=ax)
    st.pyplot(fig)
