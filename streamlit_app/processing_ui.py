import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def processing_page(compact: bool = False):
    st.title("⚙️ Processing")
    st.markdown("Advanced metrics and full account analysis.")

    df = st.session_state.get("uploaded_df")
    if df is None:
        st.warning("⚠️ No dataset uploaded yet.")
        return

    # 🔹 Safe metric calculations
    df["LiquidityRatio"] = (df["Assets"] / df["Liabilities"].replace(0, np.nan)).round(2)
    df["ProfitMargin"] = (df["NetIncome"] / df["Revenue"].replace(0, np.nan)).round(2)
    df["RevenuePerEmployee"] = (df["Revenue"] / df["Employees"].replace(0, np.nan)).round(2)

    st.subheader("📊 Processed Data")
    st.dataframe(df.head(20))

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Liquidity", f"{df['LiquidityRatio'].mean():.2f}")
    col2.metric("Avg Profit Margin", f"{df['ProfitMargin'].mean():.2%}")
    col3.metric("Revenue/Employee", f"${df['RevenuePerEmployee'].mean():,.0f}")

    st.subheader("📈 Select Analysis Charts")
    options = st.multiselect(
        "Choose charts:",
        ["Revenue by Sector", "Profit Margin Distribution", "Liquidity Ratio Trend",
         "Revenue vs Profit Scatter", "Sector Liquidity", "Yearly Revenue Growth",
         "3D Liquidity-Revenue-Profit"]
    )

    if "Revenue by Sector" in options:
        fig = px.bar(df, x="Sector", y="Revenue", color="Sector")
        st.plotly_chart(fig, use_container_width=True)

    if "Profit Margin Distribution" in options:
        fig, ax = plt.subplots()
        sns.histplot(df["ProfitMargin"].dropna(), bins=10, kde=True, ax=ax, color="green")
        st.pyplot(fig)

    if "Liquidity Ratio Trend" in options:
        fig = px.line(df.groupby("Year")["LiquidityRatio"].mean().reset_index(),
                      x="Year", y="LiquidityRatio", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    if "Revenue vs Profit Scatter" in options:
        fig = px.scatter(df, x="Revenue", y="NetIncome", color="Sector",
                         size="Assets", hover_name="Company")
        st.plotly_chart(fig, use_container_width=True)

    if "Sector Liquidity" in options:
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x="Sector", y="LiquidityRatio", ax=ax)
        st.pyplot(fig)

    if "Yearly Revenue Growth" in options:
        yearly = df.groupby("Year")["Revenue"].sum().reset_index()
        fig = px.line(yearly, x="Year", y="Revenue", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    if "3D Liquidity-Revenue-Profit" in options:
        fig = px.scatter_3d(df, x="LiquidityRatio", y="Revenue", z="NetIncome",
                            color="Sector", size="Employees", hover_name="Company")
        st.plotly_chart(fig, use_container_width=True)
