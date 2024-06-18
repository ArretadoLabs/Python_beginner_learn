"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
"""

# Section with variables and input data user
height_people = float(input("What height of people: "))

# Calculating weight ideal for people based in you height
weight_people = (72.7 * height_people) - 58

# Printing value of weight ideal for people
print("Weight ideal of people a have %.2f is %.2f KG" % (height_people, weight_people))
