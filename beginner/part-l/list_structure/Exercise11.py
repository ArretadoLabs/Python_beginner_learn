"""
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
"""

# Creating empty lists and variables initializing
list_age = []
list_height = []
average_height = 0
count_student = 0


# Inserting and manipulation data
for x in range(0, 5):
    height_student = float(input("What you height: "))
    list_height.append(height_student)
    average_height += height_student
    age_student = int(input("What you age: "))
    list_age.append(age_student)

aux_average_height = average_height / len(list_height)
print("The average of height students is: %.2f " % aux_average_height)

for x in list_age:
    if x > 13 and x < aux_average_height:
        count_student += 1

print("The amount studens in condition mentioned is: ", count_student)
