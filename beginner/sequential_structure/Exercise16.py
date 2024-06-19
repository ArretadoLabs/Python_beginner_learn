"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
"""

# Variables with data user input
size_area_meters_square = int(input("Which size area in square meters: "))

# Amount of paint
amount_paint_tin = size_area_meters_square / 18

# Printing amount of tin paint
print("Amount of tin paint is: %.2f " % (amount_paint_tin))

# calculating value of money spend in paint tin
value_final_paint_tin = amount_paint_tin * 80

print("Value final of amount tin paint: %.2f " % (value_final_paint_tin))
