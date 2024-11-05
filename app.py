import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt 

st.write("""
 # Car Sales Advertisements
 
Shown is a break down of the Car Sales data including the ***Vehicle Types*** by ***Manufacturer***, as well as the ***Model_year***, ***manufacturer***, and ***volume of advertisements****""")




st.button("Click")

st.df.describe()

# Load the CSV file
df = pd.read_csv('vehicles_us.csv')


#Check Data Types
st.write("Data Types:", df.dtypes)

#Make Scatter Plot
# Create a scatter plot
fig = px.scatter(
    df,
    x='odometer',  # X-axis
    y='price',     # Y-axis
    color='model_year',  # Optional: color by model year
    title='Price vs Odometer',
    labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
)

# Update layout
fig.update_layout(title_text='Price vs Odometer Scatter Plot')

# Show the plot
fig.show()


st.df.describe()

# Load the CSV file
df = pd.read_csv('vehicles_us.csv')


#Check Data Types
st.write("Data Types:", df.dtypes)

#Scatter plot example:
fig = px.scatter(...)
fig.update_layout(title_text='..')
st.plotly_chart(fig)