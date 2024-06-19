"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
"""

# Variables with value
number = int(input("What your number: "))

# Logical decision
if number >= 0:
    print("%d Number is positive" % (number))
else:
    print("%d number is negative" % (number))
