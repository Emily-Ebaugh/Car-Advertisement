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



# Checkbox options for selecting columns
show_price = st.checkbox('Show Price Histogram', value=True)
show_odometer = st.checkbox('Show Odometer Histogram', value=True)
show_model_year = st.checkbox('Show Model Year Histogram', value=True)

# Create a histogram based on selected checkboxes
fig, ax = plt.subplots()

if show_price:
    ax.hist(df['price'], bins=30, alpha=0.5, label='Price', color='blue')

if show_odometer:
    ax.hist(df['odometer'], bins=30, alpha=0.5, label='Odometer', color='orange')

if show_model_year:
    ax.hist(df['model_year'], bins=30, alpha=0.5, label='Model Year', color='green')

# Adding labels and title
ax.set_title('Histogram of Selected Columns')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.legend()

# Show the plot in Streamlit
st.pyplot(fig)