import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt 

st.write("""
 # Car Sales Advertisements
 
Shown is a break down of the Car Sales data including the ***Vehicle Types*** by ***Manufacturer***, as well as the ***Model_year***, ***manufacturer***, and ***volume of advertisements****""")




st.button("Click")
# Load the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

# Load the data
df = load_data()

# Display the first few rows of the dataframe
st.write("Data Preview:", df.head())

# Check for necessary columns
if 'model_year' in df.columns and 'price' in df.columns:
    # Create a line chart for price over model_year
    line_chart = alt.Chart(df).mark_line().encode(
        x='model_year:O',
        y='price:Q',
        tooltip=['model_year', 'price']
    ).properties(
        title='Price Over Model Year'
    )

    # Display the line chart
    st.altair_chart(line_chart, use_container_width=True)

    # Create a scatter plot for price vs. model_year
    scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
        x='model_year:O',
        y='price:Q',
        tooltip=['model_year', 'price']
    ).properties(
        title='Price vs Model Year'
    )

    # Display the scatter plot
    st.altair_chart(scatter_plot, use_container_width=True)
else:
    st.write("The required columns 'model_year' and 'price' are not in the dataset.")