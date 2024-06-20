"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

# Section of variables
values = str(input("Input you numbers: "))

# Converting format data and inserting values list and tuples
list_values = values.split(
    ","
)  # Using function "split" for separate values and automatic inserting in one list

tuple_values = tuple(list_values)

# Printing values of list and tuple
print("Values of list", list_values)
print("Values of tuple", tuple_values)
