import streamlit as st

st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")
st.title("🌡️ Temperature Converter")


option = st.radio("Select your option:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))


if option == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
    if st.button("Convert"):
        fahrenheit = (celsius * 9/5) + 32
        st.success(f"{celsius}°C = {fahrenheit}°F")

elif option == "Fahrenheit to Celsius":
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
    if st.button("Convert"):
        celsius = (fahrenheit - 32) * 5/9
        st.success(f"{fahrenheit}°F = {celsius}°C")