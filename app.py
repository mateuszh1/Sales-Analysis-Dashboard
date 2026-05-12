import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA_PATH = Path("data/PROCCESSED/cleaned_data.csv")

st.set_page_config(
    page_title="Sales Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"

)