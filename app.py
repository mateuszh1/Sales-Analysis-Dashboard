import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA_PATH = Path("Data/PROCCESSED/cleaned_data.csv")

st.set_page_config(
    page_title="Sales Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"

)

@st.cache_data
def load_Data():
    df = pd.read_csv(DATA_PATH)
    return df

st.title("Sales Analysis Dashboard")
st.write("Interactive dashboard for supermarket sales analysis.")

st.subheader("Data Overview")
df = load_Data()
st.dataframe(df.head())
st.sidebar.header("Filters")
filtered_df = df.copy()

if "category" in df.columns:
    selected_categories = st.sidebar.multiselect(
        "Select Categories",
        options=df["category"].dropna().unique(),
        default=df["category"].dropna().unique()
    )
    filtered_df = filtered_df[filtered_df["category"].isin(selected_categories)]