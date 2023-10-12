# fichier principal
def demander_nom():
    name = ""
    while name =="":
        name = input("quel est votre nom? ")
    return name
    
def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("quel est votre age? ")
        try:
            age_int = int(age_str)        
        except:
            print("ERREUR: vous devez entrez un nombre pour votre age")
    return age_int

nom = demander_nom()
age = demander_age()

print("Bonjour " + nom + ", vous avez " + str(age) + " ans")
print("l'an prochain, vous aurez: " + str(age+1) + " ans")



# while: tant que 
# n = 1
# while n <= 4:
#     print("n vaut: " + str(n))
#     n = n +1
# print("fin de la boucle")    
    
# motDePass = ""
# while not motDePass =="123":
#     motDePass= input("Entrez le mot de passe: ")
# print("Mot de passe correct, vous avez accès au compte")
    





