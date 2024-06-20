"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações. 
"""

# Section of variables
login_user = str(input("Input you login: "))
password_user = str(input("Input you password: "))

# logical validation
while login_user == password_user:
    print("Login and password is equals, try again!! ")
    login_user = str(input("Input you login: "))
    password_user = str(input("Input you password: "))

# Printing values final
print("You login is: %s " % (login_user))
print("You password is: %s " % (password_user))
