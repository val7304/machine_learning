


# pourcentage l'un par rapport à l'autre
odict_values= 84.082
line_coverage_values= 10

# if line_coverage_values > odict_values:
Pourcentage = line_coverage_values*odict_values/100
print(Pourcentage) #80.77080000000001
    

    


############ <example> ############ fonction personnalisée en Python pour calculer des pourcentages.

def percentage(part, whole):
    percentage = 100 * float(part)/float(whole)
    return str(percentage) + "%"

# print(percentage(95, 84))

############ <example> ############ 

quotient = 3 / 5

percent = quotient * 100

# print(percent)


############ <example> ############ # Si vous voulez le pourcentage l'un par rapport à l'autre, vous devez utiliser le code suivant.

def percent(x, y):
    if not x and not y:
        print("x = 0%\ny = 0%")
    elif x < 0 or y < 0:
        print("The inputs can't be negative!")
    else:
        final = 100 / (x + y)
        x *= final
        y *= final
        # print('x = {}%\ny = {}%'.format(x, y))

# percent(3, 6)





# if line_coverage_values > odict_values:
#     line_coverage_values = line_coverage_values*(odict_values/100)
#     # Pourcentage = 100 * line_coverage_values/odict_values
#     print(line_coverage_values, odict_values) #84.84060000000001 89.4


