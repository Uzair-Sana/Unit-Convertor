import streamlit as st

# Define unit categories and conversions
unit_data = {
    "Length": {
        "units": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
        "conversion": {
            "Meters": 1,
            "Kilometers": 1000,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Miles": 1609.34,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254
        }
    },
    "Mass": {
        "units": ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"],
        "conversion": {
            "Kilograms": 1,
            "Grams": 0.001,
            "Milligrams": 1e-6,
            "Pounds": 0.453592,
            "Ounces": 0.0283495
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    }
}

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

# General conversion function
def convert(value, category, from_unit, to_unit):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    else:
        base_value = value * unit_data[category]["conversion"][from_unit]
        return base_value / unit_data[category]["conversion"][to_unit]

# Streamlit App
st.set_page_config(page_title="Unit Converter", page_icon="🔁")
st.title("🔁📏🌡️⚖️ Unit Converter")

category = st.selectbox("Select Category", list(unit_data.keys()))
units = unit_data[category]["units"]

from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)
value = st.number_input("Enter value", value=1.0)

if st.button(label="Convert"):
    result = convert(value, category, from_unit, to_unit)
    st.write(f"**{value} {from_unit} = {result:.4f} {to_unit}**")
else:
    result = convert(value, category, from_unit, to_unit)
    st.write(f"**{value} {from_unit} = {result:.4f} {to_unit}**")
