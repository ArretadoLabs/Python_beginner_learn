"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas. 
"""

# Section with variables and user data input
weight_fish = float(input("What weight of fish: "))

# Using structure conditional for calculate tax
if weight_fish > 50:
    weight_excedent = weight_fish - 50
    value_tax = weight_excedent * 4
    print("Value of tax weight fish is: R$ %.2f " % (value_tax))

# Final conditional
print("Fish isent of tax value")
