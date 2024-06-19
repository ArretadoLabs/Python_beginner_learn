"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
"""

# Section of variables with data user input
day_week_number_id = int(input("Input data of identify day with number: "))

# Structure logical for identify number
if day_week_number_id == 1:
    print("Sunday")
elif day_week_number_id == 2:
    print("Monday")
elif day_week_number_id == 3:
    print("Tuesday")
elif day_week_number_id == 4:
    print("Wedenesday")
elif day_week_number_id == 5:
    print("Thursday")
elif day_week_number_id == 6:
    print("Friday")
elif day_week_number_id == 7:
    print("Saturday")
else:
    print("Day invalid, try again!")
