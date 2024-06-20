"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 
"""

# Section of variables with data user input
first_number = int(input("Number one: "))
second_number = int(input("number two: "))
third_number = float(input("Number three: "))

# calculate and operation with numbers
first_operation = (first_number * 2) * (second_number / 2)
second_operation = (first_number * 3) + (third_number)
third_operation = third_number**3

# Printing values final of operation
print("Value of first operation is: ", first_operation)
print("Value of second operation is: ", second_operation)
print("Value of third operation is: ", third_operation)
