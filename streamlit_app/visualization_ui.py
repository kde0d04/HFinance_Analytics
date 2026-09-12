import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def visualization_page(compact: bool = False):
    st.title("📊 Visualization")
    st.markdown("Explore your dataset with multiple chart options.")

    df = st.session_state.get("uploaded_df")
    if df is None:
        st.warning("⚠️ No dataset uploaded yet.")
        return

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${df['Revenue'].sum():,.0f}")
    col2.metric("Total Profit", f"${df['NetIncome'].sum():,.0f}")
    col3.metric("Avg Assets", f"${df['Assets'].mean():,.0f}")

    st.subheader("📈 Select Charts")
    options = st.multiselect(
        "Choose charts:",
        ["Revenue Trend", "Profit Distribution", "Assets vs Liabilities",
         "Correlation Heatmap", "Revenue vs Employees", "Sector Revenue Share",
         "3D Revenue-Profit-Assets"]
    )

    if "Revenue Trend" in options:
        fig = px.line(df, x="Year", y="Revenue", color="Company", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    if "Profit Distribution" in options:
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x="Sector", y="NetIncome", ax=ax)
        st.pyplot(fig)

    if "Assets vs Liabilities" in options:
        fig = px.scatter(df, x="Assets", y="Liabilities", color="Sector",
                         hover_name="Company", size="Revenue")
        st.plotly_chart(fig, use_container_width=True)

    if "Correlation Heatmap" in options:
        corr = df[["Assets","Liabilities","Revenue","NetIncome","Employees"]].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    if "Revenue vs Employees" in options:
        fig = px.scatter(df, x="Employees", y="Revenue", color="Sector",
                         size="NetIncome", hover_name="Company")
        st.plotly_chart(fig, use_container_width=True)

    if "Sector Revenue Share" in options:
        sector_share = df.groupby("Sector")["Revenue"].sum().reset_index()
        fig = px.pie(sector_share, names="Sector", values="Revenue", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)

    if "3D Revenue-Profit-Assets" in options:
        fig = px.scatter_3d(df, x="Revenue", y="NetIncome", z="Assets",
                            color="Sector", size="Employees", hover_name="Company")
        st.plotly_chart(fig, use_container_width=True)
