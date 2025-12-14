import streamlit as st
import os
import pandas as pd

DATA_FILE = "feedback_data.csv"

st.title("🛠 Admin Dashboard")

if not os.path.exists(DATA_FILE):
    st.warning("No feedback data available yet.")
else:
    df = pd.read_csv(DATA_FILE)

    st.subheader("📋 All Customer Feedback")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Basic Analytics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Submissions", len(df))

    with col2:
        st.metric("Average Rating", round(df["rating"].mean(), 2))
