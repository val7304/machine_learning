Tarif_normal = 10
Tarif_moins6 = 3
Tarif_6_17_plus_65 = 5

age = int(input("Enter your age : "))

if age < 6 :
    total = Tarif_moins6
if age > 7 and age <= 17 or age >= 65:
    total = Tarif_6_17_plus_65
else:
    total = Tarif_normal    

print("Suivant votre âge, vous payerez: " + str(total) + "€") 

reduction = str(input("Possèdez-vous une carte de réduction? oui-non : "))

if reduction == "oui":
    total = total / 2
else: 
    total

print("Votre place vous reviens, au total à: " + str(total) + "€") 
    
# Tarif normal : 10 €
# Tarif moins de 6 ans : 3 €
# Tarif entre 6 et 17 ans (inclus) et plus de 65 ans (inclus) : 5 €

# Et si la personne possède une carte de réduction, le prix de son billet est réduit de 50%.
# Utilisez la fonction input() pour demander l'âge de la personne et si elle possède une carte de réduction. 
# Puis déduisez de ces deux informations le prix de la place




