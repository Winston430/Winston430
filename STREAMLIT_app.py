import streamlit as st

def square(x):
    return x * x

def cube(x):
    return x * x * x

st.title("My first Streamlit app")

st.write("This app calculates the square and cube of a number")

x = st.number_input("Enter a number:")

if x:
    st.write("The square of {} is {}".format(x, square(x)))
    st.write("The cube of {} is {}".format(x, cube(x)))

else:
    st.write("Please enter a number  ")
