a = 5

print("Complétez ce script pour qu'il affiche True si a est multiple de 3, et False si ce n'est pas le cas.") 
print("Changez la valeur de a pour tester si votre script fonctionne correctement. Il faudra passer par une variable b pour référencer vers le booléen.")

resultat = 0
for i in range(a, 1000):
    if i%3 == 0:
        resultat += i
        b  = bool(resultat)
print(b)


