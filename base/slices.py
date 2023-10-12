# s'applique aux liste et au tuples

personnes = ("valérie","jean","martin", "véro","pierre","david", "paul")

# for i in personnes:
#     print(i)
    
# on souhaite selectionner que 2 ou personnes
# [start:stop:step]
# [:]   va selectionner l'ensemble
# [::2]   va selectionner un sur deux (step de 2)
# [::-2]   va selectionner un sur deux à partir de la fin(step de 2)
for i in personnes[::-2]:
        print(i)
 
nom = "Jean"
print(nom[::-1]) #affiche dans l'ordre opposé : naeJ


 