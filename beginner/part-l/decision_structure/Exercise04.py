"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
"""

# Variables with data user input
letter = str(input("Your input letter: "))

# Logical structure decision
if (
    letter != "a"
    and letter != "e"
    and letter != "i"
    and letter != "o"
    and letter != "u"
):
    print("The %s letter is consonant!!" % (letter))
else:
    print("The %s letter is vowel!! " % (letter))
