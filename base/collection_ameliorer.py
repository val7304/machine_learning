# projet questionnaire


# Question: quelle est la capitale de la France? 
# (a) Marseille
# (b) Nice 
# (c) Paris
# (d) Nanthes

# votre  réponse
# Bonne réponse / Mauvaise réponse

'''
    titre = question[0]
    choix = question[1]
    bonne_reponse =  question[2]
    
'''
def demander_reponse_numerique_utilisateur(min, max):
    reponse = input(f"votre réponse? (entrez entre {min} et  {max} ): ")
    try:
        reponse_int = int(reponse)
        if min <= reponse_int <= max:
            return reponse_int
        print("Vous devez entre un nombre entre", min, "et", max)
    except:
        print("ERROR: Veuillez n'entrer que des chiffres")
    # fonction recursive car on a pas la réponse du 1er coup
    return demander_reponse_numerique_utilisateur(min, max)


# def poser_question(titre_question,r1,r2,r3,r4, choix_reponse):
def poser_question(question):
    choix = question[1]
    bonne_reponse =  question[2]
    
    # global score
    print("QUESTION\n")
    print(" " + question[0])
    
    # print("  ", choix[0])
    # print("  ", choix[1])
    # print("  ", choix[2])
    # print("  ", choix[3])
    nbre_choix= len(choix)
    # print(nbre_choix)
    for i in range(nbre_choix):
        nbre_choix =nbre_choix
        print(f" {i+1} - " + choix[i])
    print()

# gestion des exeptions: 
    # 1, le user rentre des lettres
    # 2, le user rentre un nombre mais au dela des réponses, function qui demanderai de rentrer un nombre entre un min et un max
    resultat_reponse_correcte = False
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))        
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("bonne réponse")
        resultat_reponse_correcte = True
        # score +=1
    else:
        print("mauvaise réponse")
        
    print()
    return resultat_reponse_correcte


    # pour un input on ne peut que concatener la chaine (+) pas de , 
    # reponse = input("votre réponse? : ")
    # reponse = input(f"votre réponse? (entrez entre 1 et  {nbre_choix} ): ")
    # reponse_int = int(reponse)
       
    # on transforme en minuscule
    # if reponse.lower() == bonne_reponse.lower():
    # "on doit convertir car il attends un nombre mtnt"
    


''''
questionnaire[] 
    question    #serait un tuple
        titre = "quelle est la capitale de la France?"
        reponse = ("Marseille", "Nice", "Paris", "Nanthes")
        bonne_reponse = "c"
        à la place d'avoir la lettre, on prendrais l'index: 
        #bonne pratice
        index_bonne_reponse = "Paris"
    
    #on isole le tuple avec des () pour les éléments de réponses
    poser_question("quelle est la capitale de la France?",("Marseille", "Nice", "Paris", "Nanthes"),"Paris")
    
    #bonne pratice aussi mais un peu lourde
    reponse = (("Marseille", false),("Nice", false), ("Paris", true), ("Nanthes", false))
'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1     
    print("score final: ", score,"/",len(questionnaire))

    

# question1 = ("quelle est la capitale de la France?",("Marseille", "Nice", "Paris", "Nanthes", "Lille"),"Paris")
# question2 = ("quelle est la capitale de l'Italie?", ("Florence", "Rome" ,"Venise" ,"Milan"),"Rome")
# question3 = ("quelle est la capitale de la Belgique?", ("Mons", "Bruxelles" ,"Gand" ,"brugge"),"Bruxelles")

questionnaire =(
    ("quelle est la capitale de la France?",("Marseille", "Nice", "Paris", "Nanthes", "Lille"),"Paris"), 
    ("quelle est la capitale de l'Italie?", ("Florence", "Rome" ,"Venise" ,"Milan"),"Rome"), 
    ("quelle est la capitale de la Belgique?", ("Mons", "Bruxelles" ,"Gand" ,"brugge"),"Bruxelles")
    )
# poser_question(question1)
# poser_question(question2)

lancer_questionnaire(questionnaire)


