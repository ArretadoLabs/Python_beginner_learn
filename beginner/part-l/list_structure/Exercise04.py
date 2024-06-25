"""
Faça um Programa que leia um vetor de 10 caracteres, 
e diga quantas consoantes foram lidas. Imprima as consoantes. 
"""

# Creating empty list
list_letters = []
list_letters_consonant = []
# Iteration loop for inserting data
for x in range(0, 5):
    letter = str(input("Input a letter: "))
    list_letters.append(letter)
    if (
        letter != "a"
        and letter != "e"
        and letter != "i"
        and letter != "o"
        and letter != "u"
    ):
        list_letters_consonant.append(letter)

print("List of letters original: ", list_letters)
print("list of letters consonants: ", list_letters_consonant)
