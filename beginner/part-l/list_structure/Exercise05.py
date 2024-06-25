"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
"""

# Creating lists with numbers
list_original = []
list_numbers_pair = []
list_numbers_odd = []

# Iteration loop for manipulation data
for x in range(0, 20):
    print("number order: ", x)
    number = int(input("What your number: "))
    list_original.append(number)
    if number % 2 == 0:
        list_numbers_pair.append(number)
    else:
        list_numbers_odd.append(number)

# Printing lists with respectives values
print("List original of numbers: ", list_original)
print("List of numbers pair: ", list_numbers_pair)
print("List of numbers odd: ", list_numbers_odd)
