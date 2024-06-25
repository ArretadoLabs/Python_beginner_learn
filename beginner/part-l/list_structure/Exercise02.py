"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 
"""

# Creating list empty
numbers_real_list = []

# Loop iteration for inserting in list
for x in range(0, 5):
    number = float(input("What a your number real: "))
    numbers_real_list.append(number)

# loop iteration in order reverse
for x in numbers_real_list:
    print(x[::-1])

print("Numbers in order reverse: ", numbers_real_list)
