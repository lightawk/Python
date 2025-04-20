#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# ================ #
#    Conditions    #
# ================ #

# Test de condition
if True:
    print("Vrai")
else:
    print("Faux")

# Test de condition sur une chaine
variable = "Alex"
if variable == "Alex":
    print("Vrai")
elif variable == "Paul":
    print("Humm")
else:
    print("Faux")

# Test de condition sur des listes
liste = ["A", "B", "C"]

liste_2 = ["A", "B", "C"]
if liste == liste_2:
    print("Identique en valeur")
else:
    print("Differente en valeur")

liste_2 = liste
if liste is liste_2:
    print("Identique en valeur")
else:
    print("Differente en valeur")

objet = False
if objet:
    print("Vrai")
else:
    print("Faux")
