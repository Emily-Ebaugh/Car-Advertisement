import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt 

st.write("Hello world")
st.button("Click")

# Load the CSV file
df = pd.read_csv('vehicles_us.csv')

# Display the first few rows of the dataframe
st.write("Data Preview:", df.head())

# Sort the DataFrame by model_year, price, and days_listed
sorted_df = df.sort_values(by=['model_year', 'price', 'days_listed'])

# Create a line chart for price over model_year
line_chart = alt.Chart(sorted_df).mark_line().encode(
    x='model_year:O',
    y='price:Q',
    tooltip=['model_year', 'price', 'days_listed']
).properties(
    title='Price Over Model Year'
)

# Create a scatter plot for price vs days_listed
scatter_plot = alt.Chart(sorted_df).mark_circle(size=60).encode(
    x='days_listed:Q',
    y='price:Q',
    color='model_year:N',
    tooltip=['model_year', 'price', 'days_listed']
).properties(
    title='Price vs Days Listed'
)

# Display the charts
st.altair_chart(line_chart, use_container_width=True)
st.altair_chart(scatter_plot, use_container_width=True)





# Display the first few rows of the dataframe
st.write("Data Preview:", df.head())

# Sort the DataFrame by model_year, price, and days_listed
sorted_df = df.sort_values(by=['model_year', 'price', 'days_listed'])

# Create a line chart for price over model_year
line_chart = alt.Chart(sorted_df).mark_line().encode(
    x='model_year:O',
    y='price:Q',
    tooltip=['model_year', 'price', 'days_listed']
).properties(
    title='Price Over Model Year'
)

# Create a scatter plot for price vs days_listed
scatter_plot = alt.Chart(sorted_df).mark_circle(size=60).encode(
    x='days_listed:Q',
    y='price:Q',
    color='model_year:N',
    tooltip=['model_year', 'price', 'days_listed']
).properties(
    title='Price vs Days Listed'
)

# Display the charts
st.altair_chart(line_chart, use_container_width=True)
st.altair_chart(scatter_plot, use_container_width=True)