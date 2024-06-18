"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
"""

# Section of variables with input data user
hour_value_work = float(input("What value of hour you work: "))

hours_worked_month = float(input("How many hours worked in month: "))

# Calculating salary brute
salary_brute = hour_value_work * hours_worked_month

# Printing value of salary brute
print("Your salary brute in month is: ", salary_brute)
