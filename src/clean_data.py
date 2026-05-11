import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/SampleSuperstore.csv")
CLEANED_DATA_PATH = Path("data/cleaned/cleaned_data.csv")
df = pd.read_csv(RAW_DATA_PATH)
df["Order Date"] = pd.to_datetime(df["Order Date"])

def clean_column_name(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

print(f"\n{df.duplicated().sum()}")
