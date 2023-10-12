import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,10)  
y = x**2                    #tableau qui est le carré de x
print(x)

plt.figure(figsize=(12, 8))

plt.subplot(2,1,1)
plt.plot(x,y)
plt.title('graphique 1')

plt.subplot(2,1,2)
plt.plot(x,np.sin(x), label='sinus')
plt.plot(x,np.cos(x), label='cosinus')
plt.legend()
plt.show()


# creer 2 graphiques sur la mm figure
# plt.subplot(2, 1, 1)    #2lignes, 1 colonne, on travaille sur le graphique 1
# plt.plot(x, y, c='red')
# plt.title('graphique1')

# plt.subplot(2, 1, 2)    #2lignes, 2 colonne, on travaille sur le graphique en dessous
# plt.plot(x, x**3, c='blue')
# plt.title('graphique2')
# plt.show()
# plt.savefig('2graphiqueSurLammPage.png')


# permets de générer une grille de graphique
# plt.subplot(ligne, colonne, position)
# plt.subplot(2, 2, 1)
# plt.subplot(2, 2, 2)
# plt.subplot(2, 2, 3)
# plt.subplot(2, 2, 4)
