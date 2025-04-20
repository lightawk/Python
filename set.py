#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# ========== #
#    Sets    #
# ========== #

# liste sans ordre
# liste sans doublon

# pop existe aussi (comme pour la liste)
# pas d'index car le set n'est pas trié !

set = {}
set = {"A", "B", "C", "D", "A"}
# set.remove("A")
print(set)

set_2 = {"A", "B"}
# Affiche les elements en communs dans chaque set
print(set.intersection(set_2))
# Affiche la difference entre les deux sets
print(set.difference(set_2))
# Assemblage des deux listes
print(set.union(set_2))

# Convertir une liste en set (pour utiliser les intersection, union, etc.)
mon_set = set(liste)
