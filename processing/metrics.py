import pandas as pd
import numpy as np

def calculate_liquidity_ratio(df: pd.DataFrame) -> float:
    """Liquidity ratio = Current Assets / Current Liabilities"""
    if "currentassets" in df.columns and "currentliabilities" in df.columns:
        return df["currentassets"].sum() / max(df["currentliabilities"].sum(), 1)
    return None

def calculate_cagr(start_value: float, end_value: float, years: int) -> float:
    """Compound Annual Growth Rate"""
    if start_value > 0 and years > 0:
        return ((end_value / start_value) ** (1/years)) - 1
    return None

def calculate_profit_margin(df: pd.DataFrame) -> float:
    """Profit Margin = Net Income / Revenue"""
    if "netincome" in df.columns and "revenue" in df.columns:
        return df["netincome"].sum() / max(df["revenue"].sum(), 1)
    return None
