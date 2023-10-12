# une fonction qui retourne plusieurs valeurs 

#avec une valeur
def obtenir_infos():
    return "Valérie",37,1.62
    
def afficher_info(nom, age, taille):
    print(f"Informations: Nom: {nom}, Age: {age}, Taille: {taille}")    #Informations: Nom: Valérie, Age: 37, Taille: 1.62
    
#appel de la function: 
infos = obtenir_infos()
print(infos)            #return ('Valérie', 37, 1.62)
# afficher_info(infos)    #return error:  afficher_info() missing 2 required positional arguments: 'age' and 'taille'
# il va falloir ouvrir le tupple:
afficher_info(*infos)   #return Informations: Nom: Valérie, Age: 37, Taille: 1.62 pareil que si oon avait fait infos[0],infos[1],infos[2] etc



