# Écrivez un programme demandant une année quelconque et affichant ensuite si l'année rentrée dans la console est bissextile ou non.

year = int(input("Enter an year: "))
year_c = year

if year_c%4==0 and year_c%100!=0 or year_c%400 == 0:
    print(str(year) + " est une année bissextile")
else: 
    print(str(year) + " n'est pas une année bissextile")
