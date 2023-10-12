# -*- coding:Utf-8 -*-
# boucle itérative avec une condition

n = 1
while n <= 10:
    print("n = " + str(n))
    n += 1  # Assignment and modification in 1 instruction : equivalent to n = n + 1
# print("Program exited the while loop")

# petit programme simple affichant une suite de Fibonacci, c.à.d. une suite
# de nombres dont chaque terme est égal à la somme des deux précédents.
 
a, b, c = 1, 1, 1             # a & b servent au calcul des termes successifs
                              # c est un simple compteur
print (1)                     # affichage du premier terme
while c<15:                   # nous afficherons 15 termes au total
    a, b, c = b, a+b, c+1
    print (b)