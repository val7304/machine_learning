d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4, 'd': 5}


# keys() renvoie la vue des clés
# items() renvoie la vue des tuples clé-valeur (clé, valeur).

print(list(d1.keys()))
# ['a', 'b', 'c']

print(type(d1.keys()))
# <class 'dict_keys'>

print(list(d1.items()))
# [('a', 1), ('b', 2), ('c', 3)]

print(type(d1.items()))
# <class 'dict_items'>

# Les clés communes à plusieurs dictionnaires peuvent être extraites avec la méthode keys() et l’opérateur &.

intersection_keys = d1.keys() & d2.keys()
print(intersection_keys)
# {'c', 'b'}
print(type(intersection_keys))
# <class 'set'>


# Dans le cas de items(), les éléments ayant à la fois des clés et des valeurs en commun sont extraits. 
# Les éléments avec uniquement la clé ou uniquement la valeur en commun sont exclus

intersection_items = d1.items() & d2.items()
print(intersection_items)
# {('b', 2)}


# générer un nouveau dictionnaire en passant un ensemble de tuples (clé, valeur) (= le résultat de l’opération d’ensemble de items()) à dict().
intersection_dict = dict(d1.items() & d2.items())
print(intersection_dict)
# {'b': 2}

print(type(intersection_dict))
# <class 'dict'>


# Toutes les clés de plusieurs dictionnaires, c’est-à-dire les clés contenues dans au moins un des plusieurs dictionnaires, peuvent être extraites avec la commande | opérateur.
union_keys = d1.keys() | d2.keys()
print(union_keys)
# {'d', 'a', 'b', 'c'}



