import streamlit as st

def body_temperature_check():
    temperature = st.number_input("Enter your body temperature in Celsius:", min_value=0, max_value=42)
    if temperature > 36:
        st.write("Your body temperature is greater than 36 Celsius.")
    else:
        st.write("Your body temperature is normal.")

if __name__ == "__main__":
    body_temperature_check()
