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

st.subheader("Key Metrics")
col1,col2,col3, col4 = st.columns(4)

total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_quantity = filtered_df["quantity"].sum()
total_records = len(filtered_df)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Quantity", f"{total_quantity}")
col4.metric("Total Records", f"{total_records}")

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.subheader("Charts")

if "category" in filtered_df.columns and "sales" in filtered_df.columns:
     sales_by_category = (
          filtered_df
          .groupby("category")["sales"]
          .sum()
          .sort_values(ascending=False)
     )

fig, ax = plt.subplots()
sales_by_category.plot(kind="barh",ax=ax) 
ax.set_title("Total Sales by Category")
ax.set_xlabel("Sales")    
ax.set_ylabel("Category")
st.pyplot(fig)