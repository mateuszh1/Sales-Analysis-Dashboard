import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/SampleSuperstore.csv")
PROCCESSED_DATA_PATH = Path("data/PROCCESSED/cleaned_data.csv")


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


df = clean_column_name(df)

df = df.drop_duplicates()

important_columns = ["quantity", "sales", "profit"]
existing_columns = [col for col in important_columns if col in df.columns]
df = df.dropna(subset=["sales", "profit", "quantity"])

PROCCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(PROCCESSED_DATA_PATH, index=False)

print("File load successfully")
print(f"{len(df)}")
print(f"Clean data saved to {PROCCESSED_DATA_PATH}")
