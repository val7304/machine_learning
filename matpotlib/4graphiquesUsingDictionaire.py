# -*- coding:Utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# dictionnaire: clé:valeurs(100points collectés)
dataSet =  {f"experience{i}": np.random.randn(100) for i in range(4)}
# print(dataSet)

# créer une fonction graphique qui utilise le dictionnaire 
# et qui créera les 4 graphiques automatiquement dans la mm figure

# def graphique(dataSet):

for i in dataSet:
    print(i)
    