import streamlit as st
import io
import pandas as pd

def export_page(compact: bool = False):
    st.title("📤 Export")
    st.markdown("Download your processed results in multiple formats.")

    df = st.session_state.get("uploaded_df")
    if df is None:
        st.warning("⚠️ No dataset uploaded yet. Please upload on Home page.")
        return

    st.subheader("📊 Data Preview")
    st.dataframe(df.head(20))

    # CSV Export
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="⬇️ Download CSV",
        data=csv_buffer.getvalue(),
        file_name="financial_report.csv",
        mime="text/csv"
    )

    # Excel Export
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Report", index=False)
    st.download_button(
        label="⬇️ Download Excel",
        data=excel_buffer.getvalue(),
        file_name="financial_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # JSON Export
    json_data = df.to_json(orient="records", indent=2)
    st.download_button(
        label="⬇️ Download JSON",
        data=json_data,
        file_name="financial_report.json",
        mime="application/json"
    )

    # Summary Stats Export
    summary = df.describe().to_csv()
    st.download_button(
        label="⬇️ Download Summary Stats",
        data=summary,
        file_name="summary_stats.csv",
        mime="text/csv"
    )
