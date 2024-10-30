import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt 

st.write("Hello world")
st.button("Click")

st.write("Step 1: create '.streamlit/config.toml'")
st.write("Step 2: submit to github")
st.write("Step 3: connect to Render.com and make sure your application will be run on it")
st.write("Step 4: Finish the coding job")


# Specify the path to the CSV file
file_path = 'vehicles_us.csv'  # Ensure this file is in your current working directory

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    
    # Display the first few rows of the DataFrame
    print(df.head())
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")






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