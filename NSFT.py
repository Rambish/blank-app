import pandas as pd
import plotly.express as px
import streamlit as st
from google.protobuf.service import Service

st.set_page_config(
    page_title="Dashboard", )
# Path to your Excel
file_path = "BI_TDR_Linked.xlsx"
# Load the Excel file
md = pd.read_excel(file_path)
# Verify necessary columns
if not all(col in md.columns for col in ['Mode Split', 'Type', 'Service', 'TEUs']):
    raise ValueError("Required columns ('Mode Split', 'Type', 'Service', 'TEUs' ) are missing.")

    # Create pivot tables
Mode_Split = pd.pivot_table(md, values=['20','40','Moves','TEUs'], index='Mode Split', aggfunc='sum')
Type = pd.pivot_table(md, values=['20','40','Moves','TEUs'], index='Type', aggfunc='sum')
Service1 = pd.pivot_table(md, values=['20','40','Moves','TEUs'], index='Service', aggfunc='sum')

# Display the pivot tables

print("\nMode Split Pivot Table:")
print(Mode_Split)

print("\nType Pivot Table:")
print(Type)

print("\nService1 Pivot Table:")
print(Service1)



# sidebar
st.sidebar.header("Filter")
Services = st.sidebar.multiselect(
    "Select Service:",
    options=md["Service"].unique(),
    default=md["Service"].unique()
)
Agents = st.sidebar.multiselect(
    "Select Agents:",
    options=md["Agent"].unique(),
    default=md["Agent"].unique()
)


df_selection = md.query(
    "Service == @Services & Agent == @Agents"
)

st.dataframe(df_selection)
