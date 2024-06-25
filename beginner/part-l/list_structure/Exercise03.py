"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 
"""

# Creating empty list and variables
notes_list = []
sum_notes = 0


# Iteration loop for inserting data in list
for x in range(0, 4):
    note = float(input("What you note: "))
    notes_list.append(note)

# Calculating sum of notes
for x in notes_list:
    sum_notes += x


print("The sum of notes is: %.2f " % (sum_notes))

# Calculate of average notes
average_note = sum_notes / len(notes_list)

print("The average of notes is: %.2f " % (average_note))
