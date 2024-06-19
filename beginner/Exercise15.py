"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido
"""

# Section of variables with data user input
hour_work_value = float(input("How many you have value for hour in work: "))
hours_worked_month = int(input("How many you worked in month: "))

# Calculating values, logical structure
salary_brute = hour_work_value * hours_worked_month
inss = (salary_brute * 0.08)
ir = (salary_brute * 0.11)
sindicate = (salary_brute * 0.05)
salary_liquid = salary_brute - (inss + ir + sindicate)

#Display values 
print("You salary brute is: ", salary_brute)
print("You value discount under INSS: ", inss)
print("You value discount under IR: ", ir)
print("You value discount under sindicate: ", sindicate)
print("And you salary liquid is: R$ ", salary_liquid)





