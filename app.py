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


st.button("Click")



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
