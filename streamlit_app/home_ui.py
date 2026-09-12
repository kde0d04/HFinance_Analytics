import streamlit as st
import pandas as pd
from utils import clean_dataframe   # ✅ helper function from utils.py

def home_page(compact: bool = False):
    """
    Home Page UI for HFinance.
    Upload financial files and ask queries.
    """

    # Page title and intro
    st.title("🏠 Home")
    st.markdown("Welcome to **HFinance** — your financial data companion.")

    # Layout: left for upload, right for query
    left, right = st.columns([2, 1]) if not compact else st.columns([1, 1])

    # File upload section
    with left:
        st.subheader("📂 Upload Data")
        uploaded = st.file_uploader(
            "Upload CSV or Excel file",
            type=["csv", "xlsx"],
            help="Upload your financial dataset to start analysis."
        )

        if uploaded:
            try:
                # Read file safely
                if uploaded.name.endswith(".csv"):
                    df = pd.read_csv(uploaded)
                else:
                    df = pd.read_excel(uploaded)

                # ✅ Clean dataframe before saving
                df = clean_dataframe(df)
                st.session_state["uploaded_df"] = df

                # Success message
                st.success(f"File {uploaded.name} uploaded successfully.")

                # Preview
                st.markdown("### Preview of Data")
                st.dataframe(df.head(10))

                # Extra: show shape and columns
                st.markdown(f"**Rows:** {df.shape[0]} • **Columns:** {df.shape[1]}")
                st.write("Available columns:", list(df.columns))

                # Extra: summary statistics
                st.markdown("### Summary Statistics")
                st.write(df.describe(include="all"))

            except Exception as e:
                st.error(f"Could not read file: {e}")
        else:
            st.info("No file uploaded yet. Please upload a CSV or Excel file.")

    # Query section
    with right:
        st.subheader("💬 Ask a Query")
        query = st.text_area("Enter your financial query", height=150)
        if query:
            st.info(f"Query received: **{query}**")
            # ✅ Future integration with ReAct Agent
            st.write("👉 Connected dataset will be passed to ReAct Agent for reasoning + answers.")
        else:
            st.warning("No query entered yet.")

    # Footer
    st.markdown("---")
    st.caption("HFinance • Powered by Streamlit")
