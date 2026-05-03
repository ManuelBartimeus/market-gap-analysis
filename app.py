import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("data_sample.csv")

st.title("Market Gap Analysis: Healthy Snacks Opportunity")

# Sidebar Filter
categories = st.sidebar.multiselect(
    "Select Categories",
    options=df['primary_category'].unique(),
    default=df['primary_category'].unique()
)

filtered_df = df[df['primary_category'].isin(categories)]

# Scatter Plot
st.subheader("Sugar vs Protein Distribution")

fig = px.scatter(
    filtered_df.sample(3000),
    x='sugars_100g',
    y='proteins_100g',
    color='primary_category',
    hover_data=['product_name']
)

st.plotly_chart(fig)

# Gap Definition
gap_df = filtered_df[
    (filtered_df['proteins_100g'] > 10) &
    (filtered_df['sugars_100g'] < 5)
]

st.subheader("Identified Market Gap")

st.write(f"Number of products in gap: {len(gap_df)}")

# Recommendation
st.subheader("Key Insight")

st.markdown("""
**Based on the data, the biggest market opportunity is in the Snacks category, 
specifically targeting products with more than 10g of protein and less than 5g of sugar, 
where current offerings are limited.**
""")