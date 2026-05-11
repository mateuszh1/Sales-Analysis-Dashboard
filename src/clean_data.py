import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/SampleSuperstore.csv")
PROCCESSED_DATA_PATH = Path("data/cleaned/cleaned_data.csv")


def clean_column_name(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df

df = pd.read_csv(RAW_DATA_PATH)
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df = clean_column_name(df)
df = df.drop_duplicates(df)

important_columns = ["quantity", "sales", "profit"]
existing_columns = [col for col in important_columns if col in df.columns]
df.dropna(subset=["sales", "profit", "quantity"])

PROCCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(PROCCESSED_DATA_PATH, index=False)
