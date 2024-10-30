import streamlit as st
import pandas as pd
import plotly.express as px

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