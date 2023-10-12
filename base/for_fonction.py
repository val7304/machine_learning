# -*- coding:Utf-8 -*-


x = 1
y = 2

def sign(x):
    if(x > 0):
        print(x, 'est positif')
    elif x == 0:
        print(x, 'est nul')
    else: 
        print(x, 'est négatif')
        
sign(0)        
sign(-10) 
sign(10)       
        
# for qui appelle la fonction sign
# for i in range(5, 10, 2):
# créer une boucle qui va de 10 à -10 avec un pas de -1
for i in range(10, -10, -1):
    # print(i)
    sign(i)
    
        