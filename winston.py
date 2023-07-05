import streamlit as st

def body_temperature_check():
    temperature = st.number_input("Enter your body temperature in Celsius:", min_value=0, max_value=42)
    if temperature > 36:
        st.write("FEVER.")
    else:
        st.write("NO FEVER.")

if __name__ == "__main__":
    body_temperature_check()
