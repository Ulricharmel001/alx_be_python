"""
creating a script that converts temperatures between Celsius and Fahrenheit,
using global variables to store conversion factors.
Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
Inside each function, use the respective global conversion factor to perform the conversion.
"""
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    fahrenheit = int(input("Enter the temperature to convert:"))
    unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
    unit = "C".lower()
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit - 32) * 5/9
    print(FAHRENHEIT_TO_CELSIUS_FACTOR)
    return FAHRENHEIT_TO_CELSIUS_FACTOR




def convert_to_fahrenheit(celsius):
    celsius = int(input("Enter the temperature to convert:"))
    unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
    unit = "F".lower()
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = (celsius * 9/5) + 32
    print(CELSIUS_TO_FAHRENHEIT_FACTOR)
    return CELSIUS_TO_FAHRENHEIT_FACTOR

if __name__ == "__main__":
    convert_to_celsius("fahrenheit")
    convert_to_fahrenheit("celsius")




        



