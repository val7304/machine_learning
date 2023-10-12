# range sert à créer une séquence de nombres entiers. Voici comment créer un range :
r1 = range(10)      # Create a range from 0 to 10 excluded, with a step of 1
r2 = range(2, 10)   # Create a range from 2 to 10 excluded, with a step of 1
r3 = range(5, 50, 5)   # Create a range from 5 to 50 excluded, with a step of 5

# La syntaxe range() appelle le constructeur de la classe range.

# On peut en effet créer tout type d'objet de cette manière, par exemple :
li = list((1, 2, 5, 10.5, "green"))     # Create a list
t = tuple((1, 4, 4.5, "ok", "ok"))      # Create a tuple
x = int(4)                              # Create a int

# la boucle for est utilisé pour parcourir des types composites, comme des listes, des tuples, des sets...
# Écrivons par une boucle for qui ferait la même chose que la boucle while :
for n in range(10):
    print(f"n = {n}")
print("Program exited the for loop")

languages = ["C", "C++", "Java", "Python", "HTML", "CSS", "PHP", "Go", "Rust"]
for language in languages:
    print(language)

# récupérer en même temps l'élément et l'indice correspondant, grâce à la fonction enumerate() 
for i, language in enumerate(languages):
    print(f"{i} : {language}")

# altérer" une boucle avec deux mots clefs du langage : break et continue.
    # break permet de sortir d'une boucle, sans terminer l'itération en cours.
    # continue permet de terminer une itération en cours, sans exécuter les instructions qui suivent.
for i in range(5, 500, 5):
    if i == 300:
        break
    if i % 10 == 0:
        continue
    print(i)
#  les multiples de 10 ne seront pas affichés dans la console. 
#  lorsque i % 10 == 0, l'instruction continue est exécutée, et donc l'instruction print(i) n'est pas exécuté













