"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9). 
"""

# Section variable with data user input
fahrenheit = float(input("\nWhat value in fahrenheit: "))

# Converting value Fahrenheit in celsius
converter_temperature = 5 * ((fahrenheit - 32) / 9)

# Printing value of temperature converted
print("F° -> C° temperature: ", converter_temperature, " C°")
