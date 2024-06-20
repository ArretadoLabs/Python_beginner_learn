"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
    entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
"""

# Section of variables in questions with count number

"""
Initializing counter with value 0 for increment based in answer user
"""
count = 0

first_question = int(input("Telefonou para a vítima? 1 - Sim ou 2 - Não "))
if first_question == 1:
    count += 1

second_question = int(input("Esteve no local do crime? 1 - Sim ou 2 - Não "))
if second_question == 1:
    count += 1

third_question = int(input("Mora perto da vítima ? 1 - Sim ou 2 - Não "))
if third_question == 1:
    count += 1

fourth_question = int(input("Devia para a vítima ? 1 - Sim ou 2 - Não "))
if fourth_question == 1:
    count += 1

fifth_question = int(input("Já trabalhou com a vítima ? 1 - Sim ou 2 - Não "))
if fifth_question == 1:
    count += 1


# Logical condition for identify level of suspect
if count == 2:
    print("Suspect")
elif count == 3 or count == 4:
    print("accomplice")
elif count == 5:
    print("Assassin")
elif count < 2:
    print("innocent")
