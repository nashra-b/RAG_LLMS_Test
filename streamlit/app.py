import streamlit as st
import pandas as pd 
import numpy as np


#title of the application 
st.title("can we go for a walk ? boo boo ")

##display 
st.write("simple text")

##create simple dataframe 
df = pd.DataFrame({
    "first column":['yes','no'],
    "second column":['cookie it is','no study']
})

#display the dataframe
st.write("here is the dataframe we created : ")
st.write(df)    

#create a line chart
chart_data = pd.DataFrame(
    df
)
st.line_chart(chart_data)