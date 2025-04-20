#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# =========================== #
#    Chaines de caracteres    #
# =========================== #

# Operations sur les variable
variable = "Hello"

# Majuscule
print(variable.upper())
# Minuscule
print(variable.lower())
# Compter le nombre d'occurences
print(variable.count("H"))
# Position
print(variable.find("H"))
# Remplecement de chaine
print(variable.replace("H", "h"))

# print(dir(variable))
# documentation de str
# print(help(str))
# print(help(str.lower))

# Longueur
print(len(variable))
# Caractere en position X..
print(variable[1])
# Range..
print(variable[0:5])
print(variable[:3])
# Decoupage de variable
print(variable[::-1])
