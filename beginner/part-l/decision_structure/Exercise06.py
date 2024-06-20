"""
Faça um Programa que leia três números e mostre o maior deles. 
"""

# Section of variables with data user input
number_one = int(input("Number one: "))
number_two = int(input("Number two: "))
number_three = int(input("Number three: "))

# Logical decision using function MAX
print("Bigger number of three is ->", max(number_one, number_two, number_three))

# Solution without function MAX
if number_one > number_two and number_one > number_three:
    print("Number one of value %d is bigger" % (number_one))
elif number_two > number_three:
    print("Number two of value %d is bigger " % (number_two))
else:
    print("Number three of value %d is bigger" % (number_three))
