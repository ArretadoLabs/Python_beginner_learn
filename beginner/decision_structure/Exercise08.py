"""
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
"""

# section with variables and user data input
shift_learn = str(input("What you shift learning: "))

# Logical structure for identify shift learning
if shift_learn == "m" or shift_learn == "M":
    print("Good Morning")
elif shift_learn == "a" or shift_learn == "A":
    print("Good Afternoon")
elif shift_learn == "n" or shift_learn == "N":
    print("Good Night")
else:
    print("Shift invalid, try again!")
