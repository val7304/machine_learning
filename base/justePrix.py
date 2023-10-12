# trouver le prix exact d'un produit quelconque.

# Le programme demandera un prix, et répondra en disant si le prix à trouver est plus grand ou plus petit que le prix entré. 
# Le programme continuera de demander une proposition tant que vous n'avez pas donné le juste prix.

price = 450  # Price to guess, try with different values to test your program
proposal = int(input("Enter a guess for the price : "))
# Testez pour différentes valeurs de prix, afin de vérifier que votre algorithme fonctionne.


if proposal < price or proposal < price:
    proposal += int(input("Enter a guess for the price : "))
else: 
    print("bravo!")
        