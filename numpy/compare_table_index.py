# l’opérateur == lorsqu’il est utilisé avec les tableaux, retourne le tableau avec la forme équivalente aux deux tableaux, le tableau retourné contient True à un index si les éléments des deux tableaux sont égaux dans cet index, et le tableau le sera autrement contiennent False à cet index.

# Comme nous voulons comparer les deux tableaux au lieu de chaque élément, nous pouvons utiliser la méthode numpy.all() 
# avec l’opérateur ==. 

# La méthode numpy.all() renvoie True si tous les éléments du tableau d’entrée le long de l’axe donné sont True; sinon, il renvoie False.
# Cette méthode renvoie True si les deux tableaux sont vides ou si un tableau a une longueur de 1. 
# Et soulèvera également une erreur si la forme des deux tableaux n’est pas la même; c’est pourquoi les autres méthodes doivent être préférées.
 

import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

print((a1==a2).all())
print((a3==a2).all())
