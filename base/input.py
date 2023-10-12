#name = input("Enter your name : ")
#print("Hello " + name)

#debugger
#afficher un ou deux messages en fonction d'une température entrée par l'utilisateur

temp = int(input("Enter the temperature : "))

# if temp < 0:
#     print("Temperature is negative")
# elif temp == 0:
#     print("Temperature is null")
# else:
#     print("Temperature is positive")
 
  
#La température est supérieure à 40 °C, afficher : "It's really hot !"
#La température est en dessous de -30 °C, afficher : "It's really cold !"
  
if temp < 0 and temp > -30:
    print("temperature is negative")
if temp == 0:
    print("temperature is null")
if temp > 40:
    print("It's really hot !")
if temp > 0 and temp <= 40:
    print("Temperature is positive")
