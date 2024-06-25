"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 
"""

# Creating empty list
numbers = []

# Loop iteration for input data
for x in range(0, 5):
    numbers = int(input("What you number: "))


sum_numbers = 0
multi = 1

for x in numbers:
    sum_numbers += x
    multi *= x

# Printing values of list and results
print("List original with values: ", numbers)
print("Sum of numbers in list is: ", sum_numbers)
print("Multiplication of numbers in list is: ", multi)
