"""
Faça um Programa que peça dois números e imprima o maior deles. 
"""

# Section with variables and user data input
number_one = int(input("Number one: "))
number_two = int(input("Number two: "))

# Logical structure
if number_one > number_two:
    print(
        "The number one of value %d is bigger number two as value %d "
        % (number_one, number_two)
    )
else:
    print(
        "The number two of value %d is bigger number one of value %d "
        % (number_two, number_one)
    )
