"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
"""

# Section with variables
letter_gender = str(input("Input a letter, please: "))

# Logical decision structure
if letter_gender == "m" or letter_gender == "M":
    print("Your gender is: male ")
elif letter_gender == "f" or letter_gender == "F":
    print("Your gender is: female")
else:
    print("Gender invalid")
