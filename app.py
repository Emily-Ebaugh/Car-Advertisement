import streamlit as st
import pandas as pd
import plotly.express as px

st.write("""
 # Car Sales Advertisements
 
Shown is a break down of the Car Sales Advertising data in the US. It begins with a display of the data as well as a downloadable link. The data has been mined and cleaned to make it more functionable and easier to process. """)

# Step 1: Load the DataFrame from the CSV file
df = pd.read_csv('vehicles_us.csv')

# Ensure 'price' is numeric and drop rows with NaN in 'price'
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.dropna(subset=['price'], inplace=True)

# Display the DataFrame
st.header("Vehicles_us.csv Dataframe:")
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
st.header("Vehicle ***Odometer*** vs. ***Price***")
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
st.header("Vehicle ***Price***, ***Odometer***, and ***Model*** year Break Down")

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

# Title of the app
st.header("Vehicle Types by ***Manufacturer***, ***Price***, and ***Model Year***")

# Dropdown for selecting vehicle types
vehicle_types = df['type'].unique()  # Assuming 'type'


