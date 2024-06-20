"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
"""

# Variables section
note = -1
while note < 0 or note > 10:
    note = float(input("What your note: "))
    if note < 0 or note > 10:
        print("Note invalid, try again!! ")


print("The note of value %d is valid " % (note))
