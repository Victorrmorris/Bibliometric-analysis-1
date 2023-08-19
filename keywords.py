import streamlit as st
import pandas as pd
from collections import defaultdict

# Load the CSV file into a pandas DataFrame
csv_file_path = "/Users/your-username/Desktop/publications.csv"
df = pd.read_csv(csv_file_path)

# Create a dictionary to store keyword co-occurrence frequencies
keyword_cooccurrence = defaultdict(int)

# Iterate through each row of the DataFrame
for index, row in df.iterrows():
    keywords = row['Keywords'].split(';')
    keywords = [kw.strip().lower() for kw in keywords]  # Convert to lowercase
    for kw1 in keywords:
        for kw2 in keywords:
            if kw1 != kw2:
                keyword_pair = tuple(sorted([kw1, kw2]))
                keyword_cooccurrence[keyword_pair] += 1

# Streamlit App
st.title("Keyword Co-occurrence Analysis")
st.write("Analyzing co-occurrence of keywords in publications")

# Display co-occurrence results using Streamlit components
st.write("Keyword Co-occurrence Frequencies:")
for pair, count in keyword_cooccurrence.items():
    kw1, kw2 = pair
    st.write(f"Keywords: {kw1}, {kw2} | Co-occurrence Count: {count}")
