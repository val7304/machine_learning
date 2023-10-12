import matplotlib.pyplot as plt

# Création des données pour le graphique
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Création de la figure et des axes
fig, ax = plt.subplots()

# Tracer le graphique
ax.plot(x, y)

# Ajuster la taille de la figure
fig.set_size_inches(6, 4)  # Ajustez les dimensions selon votre écran

# Ajuster la taille des étiquettes et des titres
ax.set_xlabel('Axe X', fontsize=10)
ax.set_ylabel('Axe Y', fontsize=10)
ax.set_title('Graphique', fontsize=12)

# Afficher le graphique
plt.show()