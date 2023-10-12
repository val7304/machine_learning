# collection: tableaux, listes, tuples
# tuple(): immutable
# liste [] : mutable : ajouter supprimer des éléments, les modifier
# plusieurs éléménets


# ------------------ TUPLES -----------------------------------
# variable avec plusieurs valeurs
a = 5
b = "toto"

# tableaux: tuples, on ne peux plus rajouter des éléménts dedans, il est fixe contrairement aux liste
# personnes = ("valérie","jean","martin", "véro")
# print(len(personnes))
# print(personnes[0])
# print(personnes[-1])
# print(len(personnes[0]))

# for i in range(0,len(personnes)):
#     print(personnes[i])

# for i in personnes:
#     print(i)          renvoie les prénoms
#     print(len(i))     renvoie le nbre de lettre
#     print((i[0]))     renvoie la 1ere lettre de chaque

# valeurs = range(0,10)   #range est comme un tuple (0,1,3,4...) 
# print(valeurs[-1])      #renvoi 9



# ------------------ LIST -----------------------------------


personnes = ["valérie","jean","martin", "véro"]
#add
nouvelle_personne = "david"
personnes.append(nouvelle_personne)
#delete
del personnes[1]

# print(personnes)

#work
# for i in personnes:
#     print(i)

#avec une fonction
def afficher_personnes(c):
    for i in c:
        print(i)

#appel de la function: 
# afficher_personnes(personnes)

def modifier_valeur(a):     #a doit etre un int
    # a = 10        #simple
    a[0] = 10       #avec une liste

test = [1,2,3,4]        #la liste est un container
print(test) #return 5
modifier_valeur(test)
print(test) #return [10, 2, 3, 4]







