#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# ============ #
#    Tuples    #
# ============ #

# liste immutable
# plus rapide qu'une liste
# securise la donnee

# Declaration d'un tuple
tuple = ("A", "B", "C", "D")
print(tuple)
# Compte le nombre de fois ou l'element est present
compte = tuple.count("A")
# Position d'un element dans le tuple
compte = tuple.index("B")
print(compte)

# Verifier l'existence d'un element dans le tuple
print("A" in tuple)

# Pas possible
# tuple[0] = "Z"
