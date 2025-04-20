#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# =================== #
#    Dictionnaires    #
# =================== #

# Declaration d'un dictionnaire
dictionnaire = { "cle": "valeur", "cle_2": ["elmt_1", "elmt_2", "elmt_3"] }
print(dictionnaire["cle"])
print(dictionnaire.get("cle"))
# Affectation de valeur
dictionnaire["cle_2"] = "valeur_2"
# Mise a jour
dictionnaire.update({"cle": "nouvelle_valeur", "cle_2": "nouvelle_valeur_2" })
# Supprimer une cle
del dictionnaire["cle"]
# Supprimer la derniere valeur et la stocker dans un tableau
variable = dictionnaire.pop("cle_2")
print(variable)
# Longueur
print(len(dictionnaire))
# Cles
print(dictionnaire.keys())
# Valeurs
print(dictionnaire.values())
# Cles & valeurs
print(dictionnaire.items())
# Boucle
for cle, valeur in dictionnaire.items():
    print(str(cle) + "==>" + str(valeur))
