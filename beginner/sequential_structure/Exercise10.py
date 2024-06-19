"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
"""

# Section of variables with data user input
celsius_temperature = float(input("What temperature in celsius: "))

# Calculating temperature converted C° -> F°
celsius_converter = (celsius_temperature * (9 / 5)) + 32

# Printing value of temperature converted
print("Temperature C° -> F° converted is: ", celsius_converter, " F°")
