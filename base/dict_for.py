# -*- coding:Utf-8 -*-


dictionnaire_traduction = {
    "chien" : "dog",        #association key value, doit avoir des clés uniques
    "chat" : "cat",
    "souris" : "mouse",
    "oiseau" : "bird"   
}

inventaire = {
    "bananes": 500,
    "pommes": 150,
    "pêches": 0,
    "ananas": 20,
    "cerises": 800
}

list_villes = ("Paris", "Bruxelles", "Londres")
# va créer un nouveau dictionnaire avec des clés de la liste: {'Paris': None, 'Bruxelles': None, 'Londres': None}
inventaire.fromkeys(list_villes,"valeur par défaut")

dict_associé = {
    "dict_1": dictionnaire_traduction,
    "dict_2": inventaire, 
    "dict_3": list_villes
}

for i in dict_associé:
    print(i)     # affiche les clés 
    
for i in dict_associé.values():
    print(i)     # affiche les valeurs

for k,v in dict_associé.items():
    print(k,v)     # affiche les clés, valeurs
