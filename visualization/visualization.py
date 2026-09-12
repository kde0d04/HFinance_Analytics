import seaborn as sns
import matplotlib.pyplot as plt

def plot_liquidity(df):
    """Plot liquidity ratio by company"""
    if "company" in df.columns and "currentassets" in df.columns and "currentliabilities" in df.columns:
        df["liquidity_ratio"] = df["currentassets"] / df["currentliabilities"].replace(0, 1)
        sns.barplot(x="company", y="liquidity_ratio", data=df)
        plt.title("Liquidity Ratio by Company")
        return plt.gcf()

def plot_profit_margin(df):
    """Plot profit margin by company"""
    if "company" in df.columns and "netincome" in df.columns and "revenue" in df.columns:
        df["profit_margin"] = df["netincome"] / df["revenue"].replace(0, 1)
        sns.barplot(x="company", y="profit_margin", data=df)
        plt.title("Profit Margin by Company")
        return plt.gcf()

def plot_trend(df, x_col, y_col):
    """Plot trend line for any metric over time"""
    if x_col in df.columns and y_col in df.columns:
        sns.lineplot(x=x_col, y=y_col, data=df, marker="o")
        plt.title(f"Trend of {y_col} over {x_col}")
        return plt.gcf()
