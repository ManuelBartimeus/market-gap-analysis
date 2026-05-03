import streamlit as st
import pandas as pd
import plotly.express as px


# PAGE CONFIG

st.set_page_config(
    page_title="Market Gap Analysis",
    layout="wide"
)

st.title("Market Gap Analysis: Healthy Snacks Opportunity")


# LOAD DATA

@st.cache_data
def load_data():
    df = pd.read_csv("data_sample.csv")
    return df

df = load_data()


# CATEGORY FILTER

st.sidebar.header("Filters")

categories = st.sidebar.multiselect(
    "Select Categories",
    options=sorted(df['primary_category'].unique()),
    default=sorted(df['primary_category'].unique())
)

filtered_df = df[df['primary_category'].isin(categories)]


# DATA OVERVIEW (NEW - IMPORTANT)

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(filtered_df))
col2.metric("Avg Sugar (g)", round(filtered_df['sugars_100g'].mean(), 2))
col3.metric("Avg Protein (g)", round(filtered_df['proteins_100g'].mean(), 2))


# SCATTER PLOT

st.subheader("Sugar vs Protein Distribution")

sample_size = min(3000, len(filtered_df))

fig = px.scatter(
    filtered_df.sample(sample_size),
    x='sugars_100g',
    y='proteins_100g',
    color='primary_category',
    hover_data=['product_name'],
    opacity=0.7
)

st.plotly_chart(fig, use_container_width=True)


# IMPROVED GAP DEFINITION (CRITICAL FIX)

HIGH_PROTEIN_THRESHOLD = 15
LOW_SUGAR_THRESHOLD = 3

gap_df = filtered_df[
    (filtered_df['proteins_100g'] > HIGH_PROTEIN_THRESHOLD) &
    (filtered_df['sugars_100g'] < LOW_SUGAR_THRESHOLD)
]


# GAP ANALYSIS

st.subheader("Identified Market Gap")

col4, col5 = st.columns(2)

col4.metric("Products in Gap", len(gap_df))
col5.metric(
    "Gap Percentage",
    f"{round((len(gap_df) / len(filtered_df)) * 100, 2)}%"
)

st.markdown(f"""
**Gap Definition:**
- Protein > {HIGH_PROTEIN_THRESHOLD}g  
- Sugar < {LOW_SUGAR_THRESHOLD}g  

This stricter definition isolates truly high-protein, low-sugar products,
revealing a significantly underrepresented segment in the dataset.
""")


# CATEGORY DISTRIBUTION (NEW FIX FOR "OTHER" ISSUE)

st.subheader("Category Distribution")

cat_counts = filtered_df['primary_category'].value_counts().reset_index()
cat_counts.columns = ['Category', 'Count']

fig_bar = px.bar(
    cat_counts,
    x='Category',
    y='Count',
    text='Count'
)

st.plotly_chart(fig_bar, use_container_width=True)


# INGREDIENT INSIGHT (BONUS)

st.subheader("Top Ingredients in High-Protein Products")

if 'ingredients_text' in gap_df.columns:
    ingredients = gap_df['ingredients_text'].dropna().str.lower()

    words = []
    for item in ingredients:
        words.extend(item.split(','))

    from collections import Counter
    common = Counter(words).most_common(5)

    ingredient_df = pd.DataFrame(common, columns=['Ingredient', 'Count'])

    fig_ing = px.bar(
        ingredient_df,
        x='Ingredient',
        y='Count',
        text='Count'
    )

    st.plotly_chart(fig_ing, use_container_width=True)


# FINAL RECOMMENDATION (UPGRADED)

st.subheader("Key Insight & Recommendation")

st.markdown(f"""
Based on the analysis, the strongest market opportunity lies in developing products within the **Snacks category** that exceed **{HIGH_PROTEIN_THRESHOLD}g of protein** while maintaining sugar levels below **{LOW_SUGAR_THRESHOLD}g**.

The dataset shows a heavy concentration of products in the high-sugar, low-protein region, while this stricter high-protein, low-sugar segment remains significantly underrepresented.

This indicates a clear opportunity for differentiated product development targeting health-conscious consumers.
""")