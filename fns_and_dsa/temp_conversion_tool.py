FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius *CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature_value = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temperature_type == "F":
    result = convert_to_celsius(temperature_value)
    print(f"{temperature_value}°F is {result}°C")
elif temperature_type == "C":
    result = convert_to_fahrenheit(temperature_value)
    print(f"{temperature_value}°C is {result}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")

