"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor. 
"""

# Creating list emptys values
list_numbers_a = []
sum_numbers = 0

# Loop iteration for manipulation data
for x in range(0, 5):
    number = int(input("Input your number: "))
    list_numbers_a.append(number)

for x in list_numbers_a:
    sum_numbers += x**2

print("sum of numbers elevate of value 2: ", sum_numbers)
