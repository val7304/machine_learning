# import matplotlib.pyplot as plt

# # Données de l'exemple
# categories = ['Catégorie {}'.format(i) for i in range(170)]
# valeurs = [i+1 for i in range(170)]

# # Ajuster la taille de la figure
# plt.figure(figsize=(10, 8))

# # Tracer le graphique avec la palette de couleurs "Set3"
# plt.barh(categories, valeurs, color='blue')

# # Réduire les marges
# plt.subplots_adjust(left=0.2, right=0.95, top=0.9, bottom=0.1)

# # Afficher le graphique
# plt.show()


import matplotlib.pyplot as plt
import mplcursors

# Données d'exemple
categories = ['Catégorie {}'.format(i) for i in range(170)]
values = [i for i in range(170)]

# Augmenter la taille de la figure
plt.figure(figsize=(10, 20))

# Réduire les marges
plt.subplots_adjust(left=0.2, right=0.9)

# Tracer le graphique en barres horizontales avec des barres plus fines
plt.barh(categories, values, height=0.5)

# Activer le mode scrollable
mplcursors.cursor(hover=True)

# Afficher le graphique
plt.show()
