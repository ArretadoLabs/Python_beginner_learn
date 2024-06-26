"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 
"""

# Creating empty lists
list_one = []
list_two = []
list_one_two = []

for x in range(0, 5):
    number_one = int(input("Number in list one: "))
    list_one.append(number_one)
    list_one_two.append(number_one)
    number_two = int(input("Number in list two: "))
    list_two.append(number_two)
    list_one_two.append(number_two)

# Printing lists with values
print("List with values number one: ", list_one)
print("List with values number two: ", list_two)
print("List with values number one and two: ", list_one_two)
