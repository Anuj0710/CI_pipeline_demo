import streamlit as st

#streamlit ui
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fifth power")

#Input 
n = st.number_input("enter a number", value = 1, step = 1)
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#display
st.write(f"The Square of {n} is : {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"The fifth power of {n} is : {fifth_power}")