"""
temperature_converter.py
a simple module that converts temperature between celcius and farenheit.
"""
# --- Function: Celsius to Fahrenheit ---
# Formula: (°C × 9/5) + 32
# This takes a temperature in Celsius and returns its Fahrenheit equivalent.
def c_to_f(celcius):
    """
    convert celcius to farenheit.

    parameters:
        celcius (float): temperature in degrees celcius.
    returns:
        float: Equivalent temperature in degrees farenheit.
    """
    return (celcius * 9/5) +32

# --- Function: Fahrenheit to Celsius ---
# Formula: (°F − 32) × 5/9
# This takes a temperature in Fahrenheit and returns its Celsius equivalent.
def f_to_c(farenheit):
    """
    convert farenheit to celcius.

    parameters:
        farenheit (float): temperature in degrees farenheit.
    returns:
        float: Equivalent temperature in degrees celcius.
    """
    return (farenheit - 32) * 5/9

# Example usage (runs only when this file is executed directly)
if __name__ == "_main_":
    # Convert Celsius to Fahrenheit
    print("25°C =", c_to_f(25), "°F")

    # Convert Fahrenheit to Celsius
    print("77°F =", round(f_to_c(77), 2),"°C")