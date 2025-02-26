import streamlit as st
import streamlit.components.v1 as components
import math

# Page configuration
st.set_page_config(page_title="Unit Converter", layout="wide")

# Custom CSS to match Google's style
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #f0f2f6;
        max-width: 750px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1a1a1a;
    }
    
    /* Type selector styling */
    .type-selector {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Conversion box styling */
    .conversion-box {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        border: none;
        border-radius: 12px;
        padding: 25px;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Input/Output styling */
    .stNumberInput > div > div > input {
        background-color: rgba(255,255,255,0.9) !important;
        border-radius: 8px !important;
        color: #1a1a1a !important;
        font-size: 24px !important;
        padding: 10px !important;
        border: none !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Unit selector styling */
    .stSelectbox > div > div {
        background-color: rgba(255,255,255,0.9) !important;
        border-radius: 8px !important;
    }
    
    /* Formula box styling */
    .formula-box {
        background: rgba(255,255,255,0.9);
        padding: 15px;
        border-radius: 12px;
        margin-top: 20px;
        color: #1a1a1a;
        font-family: 'Google Sans', sans-serif;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Radio button styling */
    .stRadio > div {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Remove default Streamlit padding */
    .stApp {
        margin: 0;
        padding: 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

def get_conversion_factor(unit_type, from_unit, to_unit):
    conversion_factors = {
        'Length': {
            'Nanometer': 1e-9,
            'Micrometer': 1e-6,
            'Millimeter': 1e-3,
            'Centimeter': 1e-2,
            'Meter': 1,
            'Kilometer': 1e3,
            'Inch': 0.0254,
            'Foot': 0.3048,
            'Yard': 0.9144,
            'Mile': 1609.344,
            'Nautical mile': 1852
        },
        'Area': {
            'Square millimeter': 1e-6,
            'Square centimeter': 1e-4,
            'Square meter': 1,
            'Square kilometer': 1e6,
            'Square inch': 0.00064516,
            'Square foot': 0.092903,
            'Square yard': 0.836127,
            'Square mile': 2.59e6,
            'Hectare': 10000,
            'Acre': 4046.86
        },
        'Volume': {
            'Milliliter': 0.001,
            'Cubic centimeter': 0.001,
            'Liter': 1,
            'Cubic meter': 1000,
            'Cubic inch': 0.0163871,
            'Cubic foot': 28.3168,
            'Cubic yard': 764.555,
            'US gallon': 3.78541,
            'Imperial gallon': 4.54609,
            'US quart': 0.946353,
            'Imperial quart': 1.13652,
            'US pint': 0.473176,
            'Imperial pint': 0.568261,
            'US cup': 0.24,
            'US fluid ounce': 0.0295735,
            'Imperial fluid ounce': 0.0284131,
            'US tablespoon': 0.0147868,
            'Imperial tablespoon': 0.0177582,
            'US teaspoon': 0.00492892,
            'Imperial teaspoon': 0.00591939
        },
        'Mass': {
            'Microgram': 1e-9,
            'Milligram': 1e-6,
            'Gram': 1e-3,
            'Kilogram': 1,
            'Metric ton': 1e3,
            'Ounce': 0.028349523125,
            'Pound': 0.45359237,
            'Stone': 6.35029318,
            'US ton': 907.18474,
            'Imperial ton': 1016.047
        },
        'Speed': {
            'Mile per hour': 0.44704,
            'Foot per second': 0.3048,
            'Meter per second': 1,
            'Kilometer per hour': 0.277778,
            'Knot': 0.514444
        },
        'Temperature': {
            'Celsius': 'special',
            'Fahrenheit': 'special',
            'Kelvin': 'special'
        },
        'Time': {
            'Nanosecond': 1e-9,
            'Microsecond': 1e-6,
            'Millisecond': 1e-3,
            'Second': 1,
            'Minute': 60,
            'Hour': 3600,
            'Day': 86400,
            'Week': 604800,
            'Month': 2.628e6,
            'Year': 3.156e7,
            'Decade': 3.156e8,
            'Century': 3.156e9
        },
        'Frequency': {
            'Hertz': 1,
            'Kilohertz': 1e3,
            'Megahertz': 1e6,
            'Gigahertz': 1e9
        },
        'Digital Storage': {
            'Bit': 1,
            'Kilobit': 1e3,
            'Megabit': 1e6,
            'Gigabit': 1e9,
            'Terabit': 1e12,
            'Byte': 8,
            'Kilobyte': 8e3,
            'Megabyte': 8e6,
            'Gigabyte': 8e9,
            'Terabyte': 8e12
        }
    }
    
    if unit_type == 'Temperature':
        return 'special'
    
    try:
        from_factor = conversion_factors[unit_type][from_unit]
        to_factor = conversion_factors[unit_type][to_unit]
        return from_factor / to_factor
    except:
        return 1

def convert_value(value, unit_type, from_unit, to_unit):
    if unit_type == 'Temperature':
        # Temperature conversion logic
        if from_unit == to_unit:
            return value
        elif from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                return (value * 9/5) + 32
            elif to_unit == 'Kelvin':
                return value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                return (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                return (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                return value - 273.15
            elif to_unit == 'Fahrenheit':
                return (value - 273.15) * 9/5 + 32
    else:
        # Other conversions using factors
        factor = get_conversion_factor(unit_type, from_unit, to_unit)
        return value * factor

def get_formula(unit_type, from_unit, to_unit, value):
    if unit_type == 'Temperature':
        if from_unit == to_unit:
            return f"{value} {from_unit}"
        elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return f"({value}°C × 9/5) + 32 = {convert_value(value, unit_type, from_unit, to_unit)}°F"
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return f"({value}°F - 32) × 5/9 = {convert_value(value, unit_type, from_unit, to_unit)}°C"
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return f"{value}°C + 273.15 = {convert_value(value, unit_type, from_unit, to_unit)}K"
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return f"{value}K - 273.15 = {convert_value(value, unit_type, from_unit, to_unit)}°C"
    else:
        factor = get_conversion_factor(unit_type, from_unit, to_unit)
        result = convert_value(value, unit_type, from_unit, to_unit)
        return f"Multiply by {factor:.10g} = {result:.10g}"

def main():
    # Add sidebar
    with st.sidebar:
        st.title("⚙️ Settings")
        st.write("Unit Converter Settings")
        theme = st.selectbox("Select Theme", ["Light", "Dark", "Colorful"])
        precision = st.slider("Decimal Precision", 0, 10, 6)
        st.write("---")
        st.write("Made with ❤️ by Malik")

    # Main title
    st.title("📐 Smart Unit Converter")
    st.write("Convert between different units easily!")

    # Conversion types (exactly as in Google)
    conversion_types = {
        'Length': ['Nanometer', 'Micrometer', 'Millimeter', 'Centimeter', 'Meter', 'Kilometer', 'Inch', 'Foot', 'Yard', 'Mile', 'Nautical mile'],
        'Area': ['Square millimeter', 'Square centimeter', 'Square meter', 'Square kilometer', 'Square inch', 'Square foot', 'Square yard', 'Square mile', 'Hectare', 'Acre'],
        'Volume': ['Milliliter', 'Cubic centimeter', 'Liter', 'Cubic meter', 'Cubic inch', 'Cubic foot', 'Cubic yard', 'US gallon', 'Imperial gallon', 'US quart', 'Imperial quart', 'US pint', 'Imperial pint', 'US cup', 'US fluid ounce', 'Imperial fluid ounce', 'US tablespoon', 'Imperial tablespoon', 'US teaspoon', 'Imperial teaspoon'],
        'Mass': ['Microgram', 'Milligram', 'Gram', 'Kilogram', 'Metric ton', 'Ounce', 'Pound', 'Stone', 'US ton', 'Imperial ton'],
        'Speed': ['Mile per hour', 'Foot per second', 'Meter per second', 'Kilometer per hour', 'Knot'],
        'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
        'Time': ['Nanosecond', 'Microsecond', 'Millisecond', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year', 'Decade', 'Century'],
        'Frequency': ['Hertz', 'Kilohertz', 'Megahertz', 'Gigahertz'],
        'Data Transfer Rate': ['Bit per second', 'Kilobit per second', 'Megabit per second', 'Gigabit per second', 'Terabit per second', 'Byte per second', 'Kilobyte per second', 'Megabyte per second'],
        'Digital Storage': ['Bit', 'Kilobit', 'Megabit', 'Gigabit', 'Terabit', 'Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte'],
        'Energy': ['Joule', 'Kilojoule', 'Gram calorie', 'Kilocalorie', 'Watt hour', 'Kilowatt hour', 'Electron volt', 'British thermal unit', 'US therm', 'Foot-pound'],
        'Plane Angle': ['Degree', 'Radian', 'Gradian', 'Arcminute', 'Arcsecond'],
        'Pressure': ['Pascal', 'Kilopascal', 'Bar', 'Pound per square inch', 'Standard atmosphere', 'Torr'],
        'Fuel Economy': ['Miles per gallon', 'Miles per gallon (Imperial)', 'Kilometer per liter', 'Liter per 100 kilometers']
    }

    # Type selector (expandable)
    with st.expander("⟫ Select Conversion Type", expanded=False):
        conversion_type = st.radio("", list(conversion_types.keys()), horizontal=True)

    # Main conversion interface
    col1, col2, col3 = st.columns([2, 1, 2])

    with col1:
        input_value = st.number_input("", value=1.0, format="%.6f", key="input")
        from_unit = st.selectbox("From", conversion_types[conversion_type], key="from")

    with col2:
        st.markdown("<div style='text-align: center; font-size: 24px; padding: 20px'>=</div>", unsafe_allow_html=True)

    with col3:
        to_unit = st.selectbox("To", conversion_types[conversion_type], key="to")
        result = convert_value(input_value, conversion_type, from_unit, to_unit)
        st.number_input("", value=float(result), format="%.6f", disabled=True, key="result")

    # Show formula
    formula = get_formula(conversion_type, from_unit, to_unit, input_value)
    st.markdown(f"""
        <div class='formula-box'> Formula:
            {formula}
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
