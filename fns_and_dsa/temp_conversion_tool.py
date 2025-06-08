"""
creating a script that converts temperatures between Celsius and Fahrenheit,
using global variables to store conversion factors.
Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
Inside each function, use the respective global conversion factor to perform the conversion.
"""



# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR =( 5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main logic
if __name__ == "__main__":
    try:
        # Step 1: Ask for the temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # ✅ Validate it's numeric

        # Step 2: Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Step 3: Perform conversion based on unit
        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")




