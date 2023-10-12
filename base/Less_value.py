# créer collection

nom_chauffeur = ["patrick","paul","mark","jean","pierre", "marie","maxime"]
distance_chauffeur_km = [1.5,2.2,0.4,0.9,7.1,1.1,0.6]

distance_min = distance_chauffeur_km[0] # suppose que c'est le premier

#travaille sur les valeurs
#on pourrait incrémenter mais il y aurait des problemes 
# for distance in distance_chauffeur_km:
#     if distance < distance_min:
#         distance_min = distance

#a la place, travailler sur les index: 
# jusqu'au nombre d"éléments

for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i
                
   
        
print("distance minimale: " + str(distance_min) + " km")    #return: distance minimale: 0.4 km

print("Index de la distance minimale: " + str(index_min))   #return 2
#travailler sur l'index, sauvegarder cette valeur et la retrouver dans la liste des noms des chauffeurs

#add le nom du chauffeur
print("le prénom du chauffeur est: " + nom_chauffeur[index_min])    #le prénom du chauffeur est: mark

# sort()
# mauvais idée car on perdrais l'ordre du nom du chauffeur si la liste était triée
distance_chauffeur_km.sort()
print(distance_chauffeur_km[0]) #return 0.4
print(distance_chauffeur_km)    #tout est trié: [0.4, 0.6, 0.9, 1.1, 1.5, 2.2, 7.1]

#V2
#best option: MAIS UN SORT NE SUFFIT PAS
noms_distances = [("patrick",1.5), ("paul", 2.2), ("mark",0.4), ("jean", 0.9), ("pierre",7.1), ("marie", 1.1), ("maxime", 0.6)]
nom_distance_min = noms_distances[0]
for noms_distances in noms_distances:
    if noms_distances[1] < nom_distance_min[1]:
        nom_distance_min = noms_distances
    
    

print("Distance minimale: ", str(nom_distance_min[1])+"km", "nom du chauffeur: ", str(nom_distance_min[0])) 
        #return: Distance minimale:  0.4km nom du chauffeur:  mark


