import pandas as pd

def aggregate_by_column(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Aggregate financial data by a given column (e.g., company, year, sector)"""
    if group_col in df.columns:
        grouped = df.groupby(group_col).sum(numeric_only=True).reset_index()
        return grouped
    else:
        raise ValueError(f"Column '{group_col}' not found in dataframe")
