"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

# Section variables
file_string = str(input("What name of you format file: "))

# Using method split for separate values and inserting in list
name_format = file_string.split(".")

# Printing value of only format file
print("File format is: ", repr(name_format[-1]))
