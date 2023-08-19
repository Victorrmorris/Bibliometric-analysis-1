import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file containing publication data (replace with your file path)
csv_file_path = "scopus.csv"
df = pd.read_csv(csv_file_path)

# Replace 'Journal' with the actual column name containing journal names
journal_column_name = 'Journal'
# Replace 'Citations' with the actual column name containing citation metrics
citation_column_name = 'Citations'

# Group data by journal and calculate total publications and total citations
journal_data = df.groupby(journal_column_name)[citation_column_name].agg(['count', 'sum']).reset_index()

# Sort data by total publications in descending order
journal_data = journal_data.sort_values(by='count', ascending=False)

# Streamlit App
st.title("Journal Analysis")
st.write("Visualizing publications across different journals")

# Display top journals by total publications
st.write("Top Journals by Total Publications:")
st.dataframe(journal_data, height=300)

# Visualize the distribution of publications across journals using Plotly
st.write("Distribution of Publications across Journals:")
fig = px.bar(journal_data, x=journal_column_name, y='count', title="Distribution of Publications across Journals")
st.plotly_chart(fig)

# Display impact factor or citation metrics (example)
st.write("Impact Factor or Citation Metrics:")
st.write("Please provide actual impact factor or citation metrics data.")
