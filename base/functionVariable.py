


def demander_nom():
    nom = ""
    while nom == "":
        nom = input("quel est votre nom? ")
    return nom
    
def afficher_infos(nom,age,taille=0): 
    print("Bonjour " + nom + ", vous avez " + str(age) + " ans")
    # print(f"Bonjour {nom} , vous avez {age} ans")
    # print("Bonjour %s , vous avez %s ans" % (nom, age))
    condition = age >= 18
        # print(condition) 
        # print(type(condition))

    if condition:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")           
    print("l'an prochain, vous aurez: " + str(age+1) + " ans\n")
    # print("l'an prochain, vous aurez %s ans" % (age +1))
    
    # afficher taille
    # taille = 1.75
    # print(type(taille))
    if not taille == 0:
        print("Votre taille est de: " + str(taille) + "m")
    
   
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input("quel est votre age? ")
        try:
            age_int = int(age_str)        
        except:
            print("ERREUR: vous devez entrez un nombre pour votre age")
    return age_int

nom1 = demander_nom()
nom2 = demander_nom()

# age = demander_age(nom1)
# age2 = demander_age(nom2)

# afficher_infos(nom1, age)
# afficher_infos(nom2, age2)

NB_PERSONNE = 1

for i in range(0,NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_infos(nom,age)