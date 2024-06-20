"""
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
"""

list_color = []  # Creating empty list

# Initializing with loop iteration for inserting data in list
for x in range(0, 5):
    color_name = str(input("What name of color: "))
    list_color.append(color_name)

print("first color: %s and last color: %s " % (list_color[0], list_color[-1]))
