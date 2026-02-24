import streamlit as st
import pandas as pd 
import numpy as np

st.title("BLING BLING")

name = st.text_input("Enter your name:")
st.write("hey", name, "y")

age = st.slider("select your age", 0, 100, 25)

st.write(f"your age is {age}.")
options = ["10", "11", "12"]
choice = st.selectbox("select your date", options)
st.write(f"you are getting {choice} interview")

