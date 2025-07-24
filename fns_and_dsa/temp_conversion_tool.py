# This script will define functions to convert temperatures 
# between Celsius and Fahrenheit, demonstrating the use of 
# global variables to store conversion factors 
# that are accessible within functions.


global FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
global CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = input("Enter the temperature to convert: ")
try:
   temperature = float(temperature)
except:
    print("nvalid temperature. Please enter a numeric value.")
format = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if format == "F":
    print(f"{temperature}°F is {convert_to_fahrenheit(temperature)}°C")
else:
    print(f"{temperature}°C is {convert_to_celsius(temperature)}°F")
