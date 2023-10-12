# projet questionnaire


# Question: quelle est la capitale de la France? 
# (a) Marseille
# (b) Nice 
# (c) Paris
# (d) Nanthes

# votre  réponse
# Bonne réponse / Mauvaise réponse

def poser_question(question,r1,r2,r3,r4, choix_reponse):
    global score
    print("question\n")
    print(" " + question)
    print("   (a)", r1)
    print("   (b)", r2)
    print("   (c)", r3)
    print("   (d)", r4)
    print()
    reponse = input("votre réponse? : ")
    if reponse == choix_reponse:
        print("bonne réponse")
        score +=1
    else:
        print("mauvaise réponse")
print()

score = 0

poser_question("quelle est la capitale de la France?","Marseille", "Nice", "Paris", "Nanthes","c")
poser_question("quelle est la capitale de l'Italie?", "Florence", "Rome" ,"Venise" ,"Milan","a")

print("score final: ", score)