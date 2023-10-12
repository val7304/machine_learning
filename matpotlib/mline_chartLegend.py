import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Tracer votre graphique
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, label='Courbe 1')
plt.plot(x, [y_i * 2 for y_i in y], label='Courbe 2')
plt.plot(x, [y_i * 3 for y_i in y], label='Courbe 3')

# Créer une ligne personnalisée pour la séparation dans la légende
line = mlines.Line2D([], [], color='black', linestyle='--', linewidth=1.5)

# Ajouter la ligne à la légende
plt.legend(handles=[line], labels=[''], loc='upper right')

# Afficher le graphique
plt.show()
