import numpy as np


# La méthode numpy.allclose(a1, a2, rtol=1e-05, atol=1e-08, equal_nan=False) 
# prend en entrée le tableau a1 et a2 et renvoie True si chaque élément de a1 est égal à l’élément correspondant de a2, 
# ou leur différence est comprise dans la valeur de tolérance.

# La valeur de tolérance est calculée à l’aide des arguments a2, rtol et atol.
# atol + rtol*absolute(a2)

# La méthode numpy.allclose() est utile dans les calculs où l’on veut vérifier si les tableaux finaux sont égaux 
# au tableau attendu ou non. Nous pouvons utiliser la méthode numpy.allclose() pour comparer deux tableaux en Python 
# de la manière suivante:

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

print(np.allclose(a1,a2))
print(np.allclose(a3,a2))
