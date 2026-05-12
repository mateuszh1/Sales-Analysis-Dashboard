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
        options=sorted(df["category"].dropna().unique()),
        default=sorted(df["category"].dropna().unique())
    )
    filtered_df = filtered_df[filtered_df["category"].isin(selected_categories)]

if "region" in df.columns:
        selected_regions = st.sidebar.multiselect(
            "Select Regions",
            options=sorted(df["region"].dropna().unique()),
            default=sorted(df["region"].dropna().unique())

        )
        filtered_df = filtered_df[filtered_df["region"].isin(selected_regions)]

if "city" in df.columns:
     selected_cities = st.sidebar.multiselect(
          "Select Cities",
          options=sorted(df["city"].dropna().unique()),
          default=sorted(df["city"].dropna().unique())
     )
     filtered_df = filtered_df[filtered_df["city"].isin(selected_cities)]