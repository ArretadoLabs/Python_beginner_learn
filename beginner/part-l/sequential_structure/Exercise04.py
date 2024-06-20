"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
"""

# Section of variables with data user input
note_one = float(input("First note of bimester: "))
note_two = float(input("Second note of bimester: "))
note_third = float(input("Third note of bimester: "))
note_fourth = float(input("Fourth note of bimester: "))

# Calculating note average of four bimester
average_note_bimester = (note_one + note_two + note_third + note_fourth) / 4.0

# displaying note average final
print("The average of notes is: ", average_note_bimester)
