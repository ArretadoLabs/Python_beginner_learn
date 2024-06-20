"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. 
"""

# Variables with value user input
salary = float(input("What you salary: R$ "))

# Structure logical in decision
if salary > 0 and salary <= 280:
    print("Your salary current is: R$ %.2f " % (salary))
    print("Your percent growth in salary is: 20%")
    print("Your value growth in salary is: R$ %.2f " % (salary * 0.20))
    print("And final salary is : %.2f " % (salary + (salary * 0.20)))
elif salary > 280 and salary <= 700:
    print("Your salary current is: R$ %.2f " % (salary))
    print("Your percent growth in salary is: 15%")
    print("Your value growth in salary is: R$ %.2f " % (salary * 0.15))
    print("And final salary is : %.2f " % (salary + (salary * 0.15)))
elif salary > 700 and salary <= 1500:
    print("Your salary current is: R$ %.2f " % (salary))
    print("Your percent growth in salary is: 10%")
    print("Your value growth in salary is: R$ %.2f " % (salary * 0.10))
    print("And final salary is : %.2f " % (salary + (salary * 0.10)))
else:
    print("Your salary current is: R$ %.2f " % (salary))
    print("Your percent growth in salary is: 5%")
    print("Your value growth in salary is: R$ %.2f " % (salary * 0.05))
    print("And final salary is : %.2f " % (salary + (salary * 0.05)))
