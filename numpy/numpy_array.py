# -*- coding:Utf-8 -*-
import numpy as np

# https://www.youtube.com/watch?v=NzDQTrqsxas
# doc:  https://numpy.org/doc/1.24/reference/arrays.ndarray.html


# tableau à nDimension: nD array
# tableau a 2 dimension: comparé avec un tableau excel: colonne= , lignes= exemple de dataset
# tableau a 2 dimension:on peut stocker les pixels d'une image, car une img est a 2 dimensions de 0 à 255 : uniquement en noir et blanc

# tableau en 3D pour les couleurs RGB

#  package python le plus important pour faire du machine learning et du data science. 
# Numpy comprend le tableau array dit ndarray (n dimensions) qui est un objet extrêmement puissant
 
# méthode pour le ndarray, voyons les différents constructeurs qui permettent d'initialiser les tableau ndarray:

# np.array()
# np.zeros()
# np.ones()
# np.full()
# np.random.randn()

# attributs les plus importants à retenir: 
# shape: permets de voir à quoi ressemble le tableau, ? ligne, ? colonnes, la profondeur : retourne un tuple
# size

# pour développer des programmes puissants, pensez à définir le type de valeur dans le np.array() avec dtype = np.int16, np.float64

# méthodes les plus utiles pour manipuler la forme de nos tableau numpy:
# np.vstack
# np.hstack
# np.concatenate
# np.reshape
# np.squeeze
# np.ravel



# ndim=1
# shape =(2,)

# ndim=2, attribut shape
# shape =(2,3) # retourne un  tuple (immutable), accès au séquences (index): shape[0] = 2 ([0]: ligne), shape[1]=3 ([1]: colonne)

# ndim=3
# shape =(2,3,2)

# array 1D
# A = np.array([1, 2, 3])
# print(A.ndim, A.shape)  #1 (3,)

# ------------------  generateurs ------------------
# --------------------------------------------------

# a la place de [1, 2, 3] =  constructeur qui initialize les tableau
B = np.zeros((3, 2))     #tupple a l'intérieur np.zeros((ligne, colonne))  
# print(B, B.ndim, B.shape, type(B.shape))
# [[0. 0.] 
#  [0. 0.] 
#  [0. 0.]] 2 (3, 2) <class 'tuple'>


# print(C, C.size)   
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]] 12

# inititalise un tableau
D = np.full((2, 9), 9)
# print(D)
# [[9 9 9 9 9 9 9 9 9] 
#  [9 9 9 9 9 9 9 9 9]]
 
# generateur: constructeur  - utilise le module random, et la fonction randn(d0,d1,...,dn)
# np.random.randn(3,4)

# fixer le genrateur aleatoire
# np.random.seed(0)

# print(np.eye(4))
# matrice d'identité 
# on entre le nombre d'léments que l'on veut sur la diagonale
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# -------------- interressant avec matpotlib
# ------------------------------------------
# np.linspace(point de début, point de fin, qty de nbre ds le tableau -répartie de facon égale entre le point de début et le point de fin )
# np.linspace(0, 10, 20)       #20points répartis entre 0 et 10

# np.arange(point de début, point de fin, pas entre)
# np.arange(0,10,1)
# np.arange(0,10,0.5)

# dtype: nbre de bits utilisés
# np.linspace(0,10,20, dtype=np.float64)   #grde précision dans les nombres mais sera lent à l'execution
# np.linspace(0,10,20, dtype=np.float16)   #nbre moins précis mais sera plus rapide 

# Manipulation 

A = np.zeros((3,2))
B = np.ones((3,2))

# print(A)
# print(B)

# les assemblés: 
# a la verticale: 
V = np.vstack((A,B))
# print(V, V.shape)
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]
#  [1. 1.]
#  [1. 1.]
#  [1. 1.]] (6, 2) on a + de lignes

#  a l'horyzontale: 
# np.hstack((matrice, colonne a assemblé))
H = np.hstack((A,B))
# or axis=0: mm résultat que hstack, axys=1: mm resultat que vstack
# utilisé plutot concatenate pour utilisé un axis=2 ce que ne permets pas ni hstack ni vstack
# HC = np.concatenate((A,B), axis=0)  

# print(H, H.shape)
# [[0. 0. 1. 1.]
#  [0. 0. 1. 1.]
#  [0. 0. 1. 1.]](3, 4) on a plus de colonnes

# remanipuler la forme d'un tableau pour lui donner une nouvelle forme
# attention, ne fonctionne que si on a le mm nombre d'éléments
# D.shape((6, 2))       #tableau de 6 lignes, 2 colonnes
# D.size  #12

# on veut le redimesionner en tableau 3,4 (3, 4 = 12)
# D = D.reshape((3,4))
# [[0. 0. 1. 1.]
#  [0. 0. 1. 1.]
#  [0. 0. 1. 1.]] (3, 4)

# D = D.ravel() permet d'applatir un tableau à 1dimension:
D = D.ravel()
S = D.ravel().shape
print(D, S)    #[9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9]

# souvent utilisé avec les tableaux a 1 dimension, c'est la , qui cause probleme, nous n'avons pas de valeurs ensuite
# vitale dans les calculs matricielles ou faire des sommes sur certains tableaux
# peut créer aussi des problèmes lors de la création de graphique ou d'images

A = np.array([1,2,3])
A = A.reshape((A.shape[0], 1))
print(A.shape)  #(3, 1)

# fais disparaitre toutes les dimensions ou il y a des 1
A = A.squeeze()
print(A.shape) # (3,)















