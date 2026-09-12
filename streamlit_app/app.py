import os
import sys
import streamlit as st
import pandas as pd

# Ensure root path is added
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# Import all UI pages
from home_ui import home_page
from visualization_ui import visualization_page
from processing_ui import processing_page
from export_ui import export_page
from ReACT_Agent_Layer.agent_ui import react_page

# Global page configuration
st.set_page_config(
    page_title="HFinance",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_dataset(file):
    try:
        df = pd.read_csv(file)

        # 🔹 Fix mixed-type columns automatically
        for col in df.columns:
            if df[col].dtype == "object":
                try:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
                except Exception:
                    df[col] = df[col].astype(str)

        return df
    except Exception as e:
        st.error(f"❌ Error loading dataset: {e}")
        return None

def main():
    # Sidebar navigation
    with st.sidebar:
        st.markdown("## 💼 HFinance Dashboard")
        st.caption("Developed with ❤️ using Streamlit")
        st.markdown("---")

        # Compact layout toggle
        compact = st.checkbox("Compact layout", value=False)

        # File uploader
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
        if uploaded_file is not None:
            df = load_dataset(uploaded_file)
            if df is not None:
                st.session_state["uploaded_df"] = df
                st.success("✅ Dataset loaded successfully!")

        # Navigation radio
        page = st.radio(
            "Select a page:",
            ["Home", "Visualization", "Processing", "Export", "ReAct Brain"],
            index=0,
            label_visibility="visible"
        )

    # Routing logic
    if page == "Home":
        home_page(compact=compact)
    elif page == "Visualization":
        visualization_page(compact=compact)
    elif page == "Processing":
        processing_page(compact=compact)
    elif page == "Export":
        export_page(compact=compact)
    elif page == "ReAct Brain":
        react_page(compact=compact)

if __name__ == "__main__":
    main()
