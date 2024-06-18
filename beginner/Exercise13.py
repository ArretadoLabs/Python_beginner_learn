"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
"""

# Section of variables with data user input
height_people = float(input("What height of people: "))

# Calculating weight ideal for man and women
weight_man = (72.7 * height_people) - 58
weight_women = (62.1 * height_people) - 44.7

# Printing value final of weight ideal for man and women
print("Weight ideal for man with %.2f CM is %.2f KG " % (height_people, weight_man))
print("Weight ideal for women with %.2f CM is %.2f KG " % (height_people, weight_women))
