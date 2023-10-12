# -*- coding:Utf-8 -*-

# f = lambda x: x ** 2
# print(f(3))     #retourne 9

# def lambda (x, y): 
#   x ** 2 + y
# ou
f = lambda x, y: x ** 2 + y
print(f(3,4))     #retourne 13(9+4=13)

# calcul energie potentielle d'un corps mécanique
# besoin d'arguments comme la masse, la hauteur, la constante de pesanter 
# def e_potentielle(masse, hauteur, g = 9.81):        #g a une valeur par default, on n'est plus obligé de l'appeller dans la fonction
#   ajout d'une limite, si E est inferieur à limite , attention, retournera un bollean
def e_potentielle(masse, hauteur, limite, g = 9.81):     
    # instructions
    E = masse * hauteur * g         # variable interne
    # print(E, "Joules")
    # return E      #si on utilise return on doit appeller la fonction depuis une variable:
    return E < limite

# resultat = e_potentielle(80, 5, 9.81)       #resultat = 3924.0 Joules
# ou
# resultat = e_potentielle(masse = 80, hauteur = 5)   
# calcul de l'energie sur une autre planete on change la valeur du g
# resultat = e_potentielle(masse = 80, hauteur = 5, g = 6.52)   

# avec limite en +
resultat = e_potentielle(50,10,6000) 
print(resultat)  #retourne True
    
# print("Bonjour")
# homme de 80kg, 5mètres et à 9.81 la constante de pesanteur
# e_potentielle(80, 5, 9.81)  #retourne 3924 joule, on ajoute le mot joule dans la fonction 



    



