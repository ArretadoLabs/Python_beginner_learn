"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. 
"""

# Section with variables with user input data with validation value range
note_one = float(input("Note one: "))
# validation of value in range
if note_one < 0 or note_one > 10:
    print("Note invalid, try again!!")
    note_one = float(input("Note one, again: "))

note_two = float(input("Note two: "))
# validation of value in range
if note_two < 0 or note_two > 10:
    print("Note invalid, try again!!")
    note_one = float(input("Note two, again: "))

# Operation for calculate average notes
average_notes = (note_one + note_two) / 2

# Structure decision
if average_notes == 10.0:
    print("Approved with distinction")
elif average_notes >= 7.0 and average_notes <= 9.9:
    print("Approved")
else:
    print("Reproved")
