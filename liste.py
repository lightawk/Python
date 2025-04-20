#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# ============ #
#    Listes    #
# ============ #

# Declarer une liste
liste = []
liste = list()
liste = ["A", "B", "C", "D", "E"]

# Operations sur les listes
print(len(liste))
# Ajouter un element a la fin de la liste
liste.append("F")
# Inserer un element a une postion definie dans la liste
liste.insert(1, "G")
# Affichage des elements
print(liste[1]) # premier
print(liste[2:]) # a partir de 2
print(liste[::2]) # par pas de 2

liste_2 = ["AA", "BB", "CC", "DD", "EE"]
# liste.insert(1, liste_2)
# Etendre une liste avec une autre
liste.extend(liste_2)
# Supprime un element de la liste
liste.remove("A")
# Supprime le dernier element et le stocke dans une variable
variable = liste.pop()
# Inverse la liste
liste.reverse()
# Trie la liste
liste.sort()
liste.sort(reverse=True)
sorted(liste)
# min() ; max() ; sum()
# liste.index("A")
# print("A" in liste)

# Parcours de liste
lettres = ["A", "B", "C", "D", "E"]
# Boucle stantard
#for lettre in lettres:
#    print(lettre)
# Boucle avec indice
for index,lettre in enumerate(lettres, start=2):
    print(index, lettre)
# Creer une chaine a partir de la liste
jointure = ", ".join(lettres)
print(jointure)
# Cree une liste a partir d'une chaine
csv = "A;B;C;D"
liste_csv = csv.split(";")
print(liste_csv)
