# -*- coding:Utf-8 -*-

# dictionnaires: structures de données qui contiennent des associations clef/valeur
# utiles pour stocker les paramètres W1, b1, W2, b2, etc... d'un réseau de neurones qui serait développé avec Numpy.
# utile pour enregistrer des données de fichiers dans des clefs qui portent le nom de ses fichiers.

# méthodes utiles sur les dictionnaires:
# dict.values() : retourne les valeurs du dictionnaire
# dict.keys(): retourne les clefs du dictionnaire
# dict.items(): retourne les pairs clef:valeur du dictionnaire
# dict.get(clef): retourne la valeur d'une clef, sinon une valeur par défaut
# dict.fromkeys(liste): permet de créer un dictionnaire à partir d'une liste

# n'on pas d'index comme les liste, mais des clés
# clé1: valeur
# clé2: valeur

dictionnaire_traduction = {
    "chien" : "dog",        #association key value, doit avoir des clés uniques
    "chat" : "cat",
    "souris" : "mouse",
    "oiseau" : "bird"   
}
# print(dictionnaire_traduction, type(dictionnaire_traduction), len(dictionnaire_traduction))
# la position n'existe pas dans un dictionnaire, on n'utilise donc pas de [] ni de méthod append ou list
# n'a pas de début, pas de fin, pas d'ordre
# add key value to dictionnaire_traduction:
dictionnaire_traduction["cheval"] = "horse"
# print(dictionnaire_traduction.values())

inventaire = {
    "bananes": 500,
    "pommes": 150,
    "pêches": 0,
    "ananas": 20,
    "cerises": 800
}

# on recherche quelque chose qui n'existe pas il va retourner une erreur: 
# inventaire["poires"], à la place on utilise la methode get, qui ne retourne rien:
# print(inventaire.get("poires"))      #retourne None
print(inventaire.get("poires",0))      #inventaire.get("poires",valeur par defaut si None) retourne 0
print(inventaire.get("ananas",0))       #retourne 20

    
# print(inventaire,type(inventaire), len(inventaire))

# nesté un dictionnaire: un dic qui en contiens d'autres
dict_associé = {
    "dict_1": dictionnaire_traduction,
    "dict_2": inventaire
}

# print(dict_associé.keys(), dict_associé.values())


# print(dict_associé, type(dict_associé), len(dict_associé))

# import numpy as np

# # en machine learning, on utilise les dico pour stocker les parametres de leur réseau de neurones
# parametres = {
#     "W1": np.random.randn(10, 100),
#     "b1": np.random.randn(10,1),
#     "W2": np.random.randn(10, 10),
#     "b2": np.random.randn(10,1),
# }

list_villes = ("Paris", "Bruxelles", "Londres")
# va créer un nouveau dictionnaire avec des clés de la liste: {'Paris': None, 'Bruxelles': None, 'Londres': None}
print(inventaire.fromkeys(list_villes,"valeur par défaut"))

#permet d'extraire une association 
# 1 il va retirer la clé de l'inventaire, 2 il va extraire la valeur et l'afficher en sortie de la fonction
fruits = inventaire.pop('pommes')
print(fruits)   #150
print(inventaire)  #{'bananes': 500, 'pêches': 0, 'ananas': 20, 'cerises': 800} sans les pommes
















