Liste_Niv_Selection = (['task-details-provider-camunda-root', 'cc-portfolio-provider-wave-backend', 'cc-camunda-optimize-backend'])#Liste de référence
Liste_Niv_Elt = (['task-details-provider-camunda-root', 'cc-notification-backend', 'cc-camunda-optimize-backend'])


line_coverage_values = ([86.1, 48.1, 94.9])

Liste_Index = []

# connaitre les index des éléments d'une liste ne contenant pas les valeurs d'une liste de référence.
for i in range(len(Liste_Niv_Elt)):
    for j in range(len(Liste_Niv_Selection)):
        selections = set(Liste_Niv_Selection)
        indexes = [ind for ind, el in enumerate(Liste_Niv_Elt) if el not in selections]
        Liste_Index.append(i)
        # print(indexes)

print(Liste_Index)