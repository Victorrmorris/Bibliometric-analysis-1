import streamlit as st
import pandas as pd
from collections import defaultdict

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('publications.csv')

# ... Rest of the keyword co-occurrence analysis code ...

# Streamlit App
st.title("Keyword Co-occurrence Analysis")
st.write("Analyzing co-occurrence of keywords in publications")

# Display co-occurrence results using Streamlit components
st.write("Keyword Co-occurrence Frequencies:")
for pair, count in keyword_cooccurrence.items():
    kw1, kw2 = pair
    st.write(f"Keywords: {kw1}, {kw2} | Co-occurrence Count: {count}")
