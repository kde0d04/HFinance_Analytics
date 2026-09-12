import pandas as pd
import numpy as np

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Clean financial dataframe: handle NaN, normalize columns, convert types"""
    # Drop completely empty rows/columns
    df = df.dropna(how="all")
    
    # Fill missing numeric values with 0
    df = df.fillna(0)
    
    # Standardize column names (remove spaces, lowercase)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Convert object columns to numeric if possible
    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = pd.to_numeric(df[col], errors="ignore")
            except:
                pass
    
    return df
