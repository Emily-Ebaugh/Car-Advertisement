import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt  

st.write("""
 # Car Sales Advertisements
 
Shown is a break down of the Car Sales data including the ***Vehicle Types*** by ***Manufacturer***, as well as the ***Model_year***, ***manufacturer***, and ***volume of advertisements****""")


# Step 1: Load the DataFrame from the CSV file
# Make sure to provide the correct path to the CSV file
df = pd.read_csv('vehicles_us.csv')

# Display the DataFrame
st.write("Here is the DataFrame:")
st.dataframe(df)

# Step 2: Create a download button
csv = df.to_csv(index=False)  # Convert DataFrame to CSV format
st.download_button(
    label="Download vehicles_us.csv",
    data=csv,
    file_name='vehicles_us.csv',
    mime='text/csv'
)



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

# Show the plot in Streamlit
st.plotly_chart(fig)



# Title of the app
st.title("Vehicle Data Histogram")

# Load the DataFrame from the CSV file
df = pd.read_csv('vehicles_us.csv')  # Ensure the correct path to your CSV file

# Display the DataFrame
st.write("Here is the DataFrame:")
st.dataframe(df)

# Checkbox options for selecting columns
show_price = st.checkbox('Show Price Histogram', value=True)
show_odometer = st.checkbox('Show Odometer Histogram', value=True)
show_model_year = st.checkbox('Show Model Year Histogram', value=True)

# Create histograms based on selected checkboxes
if show_price:
    fig_price = px.histogram(df, x='price', nbins=30, title='Price Histogram', color_discrete_sequence=['blue'])
    st.plotly_chart(fig_price, use_container_width=True)

if show_odometer:
    fig_odometer = px.histogram(df, x='odometer', nbins=30, title='Odometer Histogram', color_discrete_sequence=['orange'])
    st.plotly_chart(fig_odometer, use_container_width=True)

if show_model_year:
    fig_model_year = px.histogram(df, x='model_year', nbins=30, title='Model Year Histogram', color_discrete_sequence=['green'])
    st.plotly_chart(fig_model_year, use_container_width=True)