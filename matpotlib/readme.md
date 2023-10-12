### Matplot lib

2 méthodes: Ne mélangez pas les deux
- OOP: orienté objet
- plt.plot : version plus basique

#### Va engendrer le meme résultat:
OOP:
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.show()
    

Function: la + simple
    plt.plot(x,y)   #données axe x (ordonné: horyzontale)
    plt.show(x,y)   #données axe Y (abssys: verticale)

vient du module matplotlib libre pour un pyplot qye l'on charge en général as plt: 
import matplotlib.pyplot as plt

## Styles: possibilités infinies
plt(x, y, label=..., lx=...,ls=..., c=...)
plt(x, y, nom de la courbe, epaisseur du trait,style du trait,couleur du trait)

example: plt.plot(x, y, c="red")



## Cycle de vie d'une figure

- plt.figure(figsize=(12, 8)): représente la feuille/fenêtre de travail, on lui donne la taille de la fenêtre en parametre, dimension en Inch
- premier graphique, donne une figure: plt.plot(x, y) 
- ajouter une autre courbe sur la figure: plt.plot(x, x**3)
- ajout d'un titre: plt.title('Figure 1')
- définir une légende: on défini les lables dans les plt.plot(x, y, label=''), on l'affiche avec plt.legend()
- terminer la figure avec : plt.show()
- fonction pour sauver la figure: plt.savefig('nomdelafigure.png')


