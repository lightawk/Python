#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# =============== #
#    Variables    #
# =============== #

# Afficher du texte
print ("Hello World")

# Afficher du texte sur plusieurs lignes
print("""
      Hello

      World
      """)

# Variable
variable = "Hello"
nom = "Alex"
print(variable + " " + nom)

# Formatage (1)
phrase = "{} {}".format(variable, nom)
print(phrase)

# Formatage (2)
phrase = f"{variable} {nom}"
print(phrase)

# Type
print(type(variable))
