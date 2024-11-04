import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt 

st.write("""
 # Car Sales Advertisements
 
Shown is a break down of the Car Sales data including the ***Vehicle Types*** by ***Manufacturer***, as well as the ***Model_year***, ***manufacturer***, and ***volume of advertisements****""")




st.button("Click")


# Load the CSV file
df = pd.read_csv('vehicles_us.csv')


#Check Data Types
st.write("Data Types:", df.dtypes)

#Make Bar Graph
st.bar.graph(df.model_year)