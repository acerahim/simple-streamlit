"""Application to deploy ML to a webapp such as streamlit"""

import streamlit as st
import pandas as pd

df = pd.read_csv("/simple-streamlit/unhrc_offices.csv", delimiter=";")



st.title("Appliation to help provide insights into Office Capacity")
st.write("The folowing a, b, c can provide indicators toward...")

# box title and options to select
offices = st.multiselect("Office City:",
    ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
    )

# Write the selected options
st.write("You selected", len(offices), 'offices')

# Display the DataFrame
st.write(df)

# Radio Button
Urgency = st.radio("Select an Urgency", ("Immediate", "Urgent", "Can Wait"))

# Different displays for success, info, warning, errors, exception 
st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)



