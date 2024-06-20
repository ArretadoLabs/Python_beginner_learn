"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
"""

# Section of variables with validation logical
name = str(input("What your name: "))
while len(name) < 3:
    print("Name invalid, try again!")
    name = str(input("again input your name: "))
# ===============================================================================
age = int(input("What you age: "))
while age < 0 or age >= 150:
    print("Age invalid, try again!!")
    age = float(input("Again, input you age: "))
# ===============================================================================
salary = float(input("What you salary: "))
while salary < 0:
    print("Salary invalid, try again! ")
    salary = float(input("Again, input your salary: "))
# ===============================================================================
gender = str(input("What your gender: f or m"))
while gender != "f" or gender != "m":
    print("Gender invalid, try again!")

state_civil = str(input("What you state civil ? "))
while (
    state_civil != "s" or state_civil != "v" or state_civil != "d" or state_civil != "d"
):
    print("State civil invalid, try again! ")
    state_civil = str(input("What you state civil ?"))
