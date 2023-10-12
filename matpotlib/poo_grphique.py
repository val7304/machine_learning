import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,10)  
y = x**2                    #tableau qui est le carré de x
print(x)

# objets qui vont utilisés des méthoses qui créerons les graphiques
# créer un graphique qui partage le mm axe, le mm absys avec :sharex=True 
fig, ax =  plt.subplots(2,1, sharex=True)
# attention subplots est de type array= 
type(ax)    #return numpy.array
ax.shape    #pour voir la dimension du tableau, retourne 2

ax[0].plot(x,y)
ax[1].plot(x,np.sin(x))
#une seule absyss, partagée pour les deux graphs

plt.show()




