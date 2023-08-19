import streamlit as st
import pandas as pd

# Load the CSV file
csv_file_path = "scopus.csv"
df = pd.read_csv(csv_file_path)

# Streamlit App Layout
st.title("Simple Streamlit App")
st.write("Displaying Basic Information")

# Display DataFrame info
st.write("Number of Rows:", len(df))
st.write("First Few Rows:")
st.write(df.head())
