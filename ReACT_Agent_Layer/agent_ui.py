import streamlit as st
import pandas as pd
from ReACT_Agent_Layer.orchestrator import orchestrate_agent

def react_page(compact: bool = False):
    st.title("🧠 ReAct Brain")
    st.markdown("Ask questions and let the agent reason with your dataset.")

    # Dataset check
    df = st.session_state.get("uploaded_df")
    if df is None or df.empty:
        st.error("❌ Sorry, no dataset connected. Please upload a file on Home page.")
        return

    # Query input
    user_query = st.text_input("Enter your query for the agent", key="react_query")
    if not user_query:
        st.info("Type a question and press Enter to run the agent.")
        return

    # Special case: max revenue row
    if "most revenue" in user_query.lower():
        try:
            max_row = df.loc[df["Revenue"].idxmax()]
            st.subheader("Row with Maximum Revenue")
            st.write(max_row)
            return
        except Exception as e:
            st.error(f"❌ Sorry, could not compute max revenue row: {e}")
            return

    # Run agent normally
    with st.spinner("Orchestrating agent..."):
        try:
            # ✅ Remove unsupported 'context' argument
            result = orchestrate_agent(user_query)

            reasoning, answer = [], None
            if isinstance(result, tuple) and len(result) == 2:
                reasoning, answer = result
            elif isinstance(result, dict):
                reasoning = result.get("reasoning", [])
                answer = result.get("answer", result.get("final_answer", None))
            else:
                answer = str(result)

        except Exception as e:
            st.warning("⚠️ Sorry, agent could not process this query.")
            st.error(f"Details: {e}")
            return

    # Show reasoning
    if reasoning:
        st.subheader("Reasoning Steps")
        for i, step in enumerate(reasoning, start=1):
            st.write(f"{i}. {step}")

    # Show answer
    if answer:
        st.subheader("Final Answer")
        st.success(answer)
    else:
        st.warning("⚠️ Sorry, agent could not provide an answer.")

    # Dataset preview
    st.subheader("📊 Connected Dataset Preview")
    st.dataframe(df.head(10))
