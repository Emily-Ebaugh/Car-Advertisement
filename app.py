import streamlit as st
import pandas as pd

st.write("Hello world")
st.button("Click")

st.write("Step 1: create '.streamlit/config.toml'")
st.write("Step 2: submit to github")
st.write("Step 3: connect to Render.com and make sure your application will be run on it")
st.write("Step 4: Finish the coding job")

import pandas as pd

# Load the dataset
data = pd.read_csv('vehicles_us.csv')

# Display the first few rows of the dataset
print(data.head())