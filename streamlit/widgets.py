import streamlit as st
import pandas as pd 
import numpy as np

st.title("Manifestation!!!!! BLING BLING")

name = st.text_input("Enter your name:")
st.write("hey", name,"you are going to get selected for the job !!!!")

age = st.slider("select your age", 0, 100, 25)

st.write(f"your age is {age}.")
options = ["100k", "110k","120K"]
choice = st.selectbox("select your salary", options)
st.write(f"you are getting {choice} salary")

