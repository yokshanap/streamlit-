import streamlit as st
import pandas as pd

st.title("📊 CSV Data Explorer")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

    if st.checkbox("Show Summary"):
        st.write(df.describe())
