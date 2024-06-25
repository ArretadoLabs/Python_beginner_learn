"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida. 
"""

# Creating lists
list_ages = []
list_height = []

# Loop iteration for manipulating data
for x in range(0, 5):
    age_people = int(input("What you age: "))
    list_ages.append(age_people)
    height_people = float(input("What you height: "))
    list_height.append(height_people)

print("========== lists of values in order original ========== ")
print("ages:", list_ages)
print("heights:", list_height)

# Reversing list
ages_list_reverse = list_ages[::-1]
height_list_reverse = list_height[::-1]

print("========== lists of values in order reverse ========== ")
print(ages_list_reverse)
print(height_list_reverse)
