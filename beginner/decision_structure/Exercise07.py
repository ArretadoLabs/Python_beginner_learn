"""
Faça um Programa que leia três números e mostre o maior e o menor deles. 
"""

# Section variables with value data user input
number_one = int(input("Number one: "))
number_two = int(input("Number two: "))
number_three = int(input("Number three: "))

# Solution with function MAX and MIN
print("The bigger number is: ", max(number_one, number_two, number_three))
print("The smaller number is: ", min(number_one, number_two, number_three))

# Solution without function MAX and MIN
if number_one > number_two and number_one > number_three and number_two > number_three:
    print("Bigger number is %d and smaller number is %d " % (number_one, number_three))
elif (
    number_one > number_two and number_one > number_three and number_three > number_two
):
    print("Bigger number is %d and smaller number is %d " % (number_one, number_two))
elif (
    number_two > number_three and number_two > number_one and number_three > number_one
):
    print("Bigger number is %d and smaller number is %d " % (number_two, number_one))
elif (
    number_two > number_three and number_two > number_one and number_one > number_three
):
    print("Bigger number is %d and smaller number is %d " % (number_two, number_three))
elif (
    number_three > number_one and number_three > number_two and number_two > number_one
):
    print("Bigger number is %d and smaller number is %d " % (number_three, number_one))
elif (
    number_three > number_one and number_three > number_two and number_one > number_two
):
    print("Bigger number is %d and smaller number is %d " % (number_three, number_two))
