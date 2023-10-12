# -*- coding:Utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# require to install: pip install xlrd

df = pd.read_excel(r"E:\workspace\python\machineLearning\pandas\titanic.xlsx", engine='xlrd')
# pd.__version__
print(df.shape)
print(df.size)

# affiche un dataFrame (tableau avec index)
# construit sur la base de numpy
# print(df.columns)
# Index(['pclass', 'survived', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket',
#        'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'],
#       dtype='object')


# fonctions:
# print(df.head())   #affiche le début, permet de voir si le dataframe à été chargé comme il faut
# df.describe()   #stat rapide

# df.drop(['column', 'column'])   #elimine certaines   colonnes, axis=1 est égale à la 1ere ligne et la premiere colonne
data=df.drop(['name','sibsp','parch','ticket', 'parch', 'ticket','fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)
# print(data)
# print(data.describe())  #donne la moyenne, mean: 38% en moyenne de gens survécurent
#             pclass     survived          age
# count  1309.000000  1309.000000  1046.000000      #compte le nombre de lignes, ici ils nous manque certains ages de passagers
# mean      2.294882     0.381971    29.881135
# std       0.837836     0.486055    14.413500
# min       1.000000     0.000000     0.166700
# 25%       2.000000     0.000000    21.000000
# 50%       3.000000     0.000000    28.000000
# 75%       3.000000     1.000000    39.000000
# max       3.000000     1.000000    80.000000
# (1309, 14)    1309 passagers

# 2options pour remplacer les données: 
# 1. compléter par une valeur par defaut! attention ceci va corrompre le dataframe sur les stats reeles
        # data.fillna(data['age'].mean())
# 2. elimine les ligne au données manquantes: on perds des données, axis=0: on veut travailler sur des lignes
data = data.dropna(axis=0)   
# ou
# data.dropna(axis=0, inplace=True) #inplace : permet de mettre en place le résultat d'une fonction dans le dataFrame

# fonctions qui modifies un dataframe:
# drop(), dropna(), set_index(), replace()

# print(data)     #[1046 rows x 4 columns], on passe de 1309 passagers à 1046
# print(data.describe())  #ca change les stats
#             pclass     survived          age
# count  1046.000000  1046.000000  1046.000000
# mean      2.207457     0.408222    29.881135
# std       0.841497     0.491740    14.413500
# min       1.000000     0.000000     0.166700
# 25%       1.000000     0.000000    21.000000
# 50%       2.000000     0.000000    28.000000
# 75%       3.000000     1.000000    39.000000
# max       3.000000     1.000000    80.000000



p = data['pclass'].value_counts()   #compte les répétitions, le nombre de passager par classe
# print(p)
# 3    501 passagers en 3eme
# 1    284 en 1ere
# 2    261 en 2eme
# Name: pclass, dtype: int64

# en faire un graphic
# p = data['pclass'].value_counts().plot.bar()
# d = data['age'].hist()
# plt.show()

# df.groupby(['column'])  #analyse par groupe
# g = data.groupby(['sex']).mean()
# print(g)
#           pclass  survived        age
# sex
# female  2.048969  0.752577  28.687071     #75% des femmes ont survecu contre 20% des hommes
# male    2.300912  0.205167  30.585233     #les hommes avait une moyenne d'age de 30ans

c = data.groupby(['sex', 'pclass']).mean()
print(c)

#                survived        age
# sex    pclass
# female 1       0.962406  37.037594    #+ de personnes hommes et femmes on servecu si ils étaient en 1ere class
#        2       0.893204  27.499191
#        3       0.473684  22.185307
# male   1       0.350993  41.029250
#        2       0.145570  30.815401
#        3       0.169054  25.962273
