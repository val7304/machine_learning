# En Python, une liste est une séquence ordonnée modifiable (mutable) d'objets. On utilise les crochets [] pour créer une liste :

l1 = [1, 2, 3.5, "hello", True, "red", 3.5, 5.5445, "b"]

# Une liste peut contenir différents types d'objets. Ici, l1 contient aussi bien un int, un float, un str ou un bool.
# Pour accéder aux éléments d'une liste, il faut écrire la variable référençant vers cette liste, suivi de l'indice (la position)
# entre crochets.
# RAPPEL : on commence à "compter" les éléments à partir de 0 !
# Exemples :

a = l1[0]       # Get the first item of the list
b = l1[2:7]     # Get items from 3rd to 7th
c = l1[4:]      # Get items for 5th to last
d = l1[:5]      # Get items from 1st to 5th
e = l1[-2]      # Get the penultimate item

# modifier ses éléments :

l1[0] = 100             # Modify the 1st item
l1[2:4] = [50, 60, 70]  # Modify the 3rd, 4th and 5th items

# ajouter de nouveaux éléments dans une liste existante.

l1.append("important message")      # Add the item at the end
l1.insert(2, "220")                 # Add the item between the 2nd and the 3rd
l2 = [6, 7, 8.6, "xyz"]
l1.extend(l2)                       # Add the items of l2 list at the end of l1 list

#variable_name.function()  pour appeler une méthode (une fonction d'un objet) d'instance.

# Les méthodes append(), insert() et extend() vont "travailler" sur la liste référencée par `l1.
# Les méthodes sont des fonctions qui opèrent donc sur un objet, là où les fonctions comme print() ou input() s'utilisent "toutes seules"
# (et ne sont donc pas appelées méthodes). 

l1.remove("important message")  # Remove the item : "important message"
l1.pop(4)                       # Remove the 5th item
l1.clear()                      # Empty the list

# voir la documentation en exécutant help(list) dans une console interactive.
#  connaître le nombre d'éléments d'une liste, on utilise la fonction len() :
l1_length = len(l1)

# savoir si un élément est présent dans une liste, on utilise le mot-clef in :
6 in l1     #renverra un booléen.

# copier une liste :
l3 = l1.copy()

# copy() créer une nouvelle liste en mémoire, qui sera une copie de celle référencée l1. En revanche, si vous faites :
l4 = l1
# Vous ne créez pas une nouvelle liste, mais vous faites simplement référencer l3 vers la même liste que l1. 
# Les deux variables référenceront donc vers la même liste.

# Vous pouvez vérifier vers quel objet référence une variable avec la fonction id() : exemple :
print(id(l1))
print(id(l3))
print(id(l4))

# listes multidimensionnelles
#  séquence d'objets. Il est donc possible qu'une liste contienne des listes, et donc de créer une liste à plusieurs dimensions :

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
coefficient = matrix[0][2]      #la variable coef vaut 3 (première ligne : indice 0, 3e colonne : indice 2).

# tuple est une séquence ordonnée non modifiable (immuable ou immutable en anglais). 
# C'est donc comme une liste, mais qui ne pourra plus être modifié après sa création.
# Pour créer une liste, on utilise les parenthèses () :
t = (1, 2, 3, 5, 6.5, "ok", False, "some text")

# récupérer un (ou des) élément(s) du tuple, on fait comme avec une liste :
f = t[3]    # Get the 4th item of the tuple
# un tuple est immuable, on ne peut ni modifier des éléments du tuple, ni en ajouter ou en retirer


# On peut en effet créer tout type d'objet de cette manière, par exemple :
li = list((1, 2, 5, 10.5, "green"))     # Create a list
t = tuple((1, 4, 4.5, "ok", "ok"))      # Create a tuple
x = int(4)                              # Create a int




































