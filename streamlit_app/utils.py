import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataframe to avoid Arrow serialization errors in Streamlit.
    - Converts all object columns to string
    - Converts numeric-like columns safely to float/int
    - Handles None/NaN values consistently
    """
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str)

        if col.lower() == "employees":
            df[col] = pd.to_numeric(df[col], errors="coerce")

        if col.lower() == "year":
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    return df
