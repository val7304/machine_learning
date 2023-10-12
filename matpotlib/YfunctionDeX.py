import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,10)     #creation de 10points allant de 0 à 2

# ---Erreur courante: 
# * faire passer + de points Y que dans X ou l'inverse, exemple: x = np.linspace(0,2,20)

y = x**2                    #tableau qui est le carré de x
print(x)

# tracé Y en fonction de x, je vais tracé x sur les abscisses et y serait ordonné
plt.plot(x,y, c="blue", lw=3, ls='--')    #trace une belle ligne avec plot, ls='--' donne une ligne pointillée
# plt.scatter(x,y, c="green")        #fonction scatterpour faire un nuage de points

plt.show()

