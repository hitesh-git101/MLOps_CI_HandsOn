import streamlit as st

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its squre, cube and fifth power")

# ENTER USER INPUT
n = st.number_input("Enter an integer", value=1, step=1)

# calculate results
square = n**2
cube = n**3
fifth = n**5

# Displaying results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth of {n} is: {fifth}")