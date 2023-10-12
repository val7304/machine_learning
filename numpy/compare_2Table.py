import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])


print(np.array_equal(a1,a1))
print(np.array_equal(a1,a2))

# numpy.array_equal(a1, a2, equal_nan=False) prend deux tableaux a1 et a2 comme entrée et renvoie True si les 
# deux tableaux ont la même forme et les mêmes éléments, et la méthode renvoie False sinon .
# La valeur par défaut de l’argument mot-clé equal_nan= est False et doit être définie sur True si nous voulons 
# que la méthode considère deux valeurs NaN comme égales.