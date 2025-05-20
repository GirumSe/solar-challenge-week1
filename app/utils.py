import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

#function to plot a line chart
def plot_boxplot(df, column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="Country", y=column, ax=ax)
    st.pyplot(fig)
