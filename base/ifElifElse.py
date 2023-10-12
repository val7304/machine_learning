a = 5
if a == 5:
    print("a is equal to 5")
print("print outside the if bloc")    

#si a est égal à 5 (condition que l'on vérifie en utilisant l'opérateur ==), alors l'opération renvoie True

#En python, pour placer des instructions dans un bloc, il faut indenter la ligne (avec 4 espaces ou une tabulation). 
# Vous voyez qu'ici, le print() n'est pas au même niveau que les lignes du dessus, mais décalé 'une fois' vers la droite")

#structures conditionnelles avec plusieurs chemins possibles, on utilise les mots clefs elif (pour else if) et else

b = 10
if b == 10:
    print("b is 10")
elif b == 15:
    print("b is 15")
else:
    print("b is neither 10 nor 15")
c = 20
if c > 10:
    print("c is strictly greater than 10")
elif c > 5:
    print("c is strictly greater than 5")

# Une structure conditionnelle commence donc toujours par un bloc if, suivi de zéro, 
# un ou plusieurs bloc(s) elif pour se terminer (mais pas obligatoirement) par un bloc else.

# Si on remplace le elif par un if dans le bout de code ci-dessus, alors on obtient deux structures 
# conditionnelles indépendantes. La console affichera cette fois :
# c is strictly greater than 10
# c is strictly greater than 5

 #imbriquer un bloc de code dans un autre. 
 # structure conditionnelle dans un bloc d'une structure. Exemple :
 
d = 3
if d > 5:
    print("d > 5")
    if d < 5:
        print("d < 3")

    