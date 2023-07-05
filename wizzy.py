import streamlit as st

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

if __name__ == "__main__":
    celsius = st.number_input("Enter the temperature in Celsius:")
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    st.write("The temperature in Fahrenheit is", fahrenheit)
