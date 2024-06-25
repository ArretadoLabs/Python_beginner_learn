"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 
"""

# Creating list empty
numbers_list = []

for x in range(0, 5):
    number = int(input("What a your number: "))
    numbers_list.append(number)

print("The list of numbers is: ", numbers_list)
