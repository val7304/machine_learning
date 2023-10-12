# -*- coding:Utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1 série = 1 colonne, 1tableau numpy à 1dimension auquel on a ajouté un axe d'index
# plusieurs series = 1 dataframe
# on peut assembler des series lorsqu'elles partagent le mm index

# comme un dictionnaire qui contient des séries: 
# dictionnaire: Dict['clé'] = valeur
# dataframe:    df['column'] = une série

#     Apples
# 0   3
# 1   2
# 2   0
# 3   1
# 1ere colonne est un index Axe Index (indépendant de numpy)
# 2eme colonne= ndarray (contient son propre index, valeurs nbre de pommes)  


df = pd.read_excel(r"E:\workspace\python\machineLearning\pandas\titanic.xlsx", engine='xlrd')

data=df.drop(['sibsp','parch','ticket', 'parch', 'ticket','fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

# fonctions qui modifies un dataframe:
# drop(), dropna(), set_index(), replace()
data = data.dropna(axis=0)   
# remplace l'index par le nom des passagers 
data = data.set_index('name')
print(data)

stat = data[data['age'] < 18].groupby(['sex','pclass']).mean()
print(stat)

# data['age'] = série       (ndarray)         
# data['age'][0:10]         (indexing)

# data['age'] < 18          (mask)     
# data[data['age'] < 18]    (boolean indexing)    

# data[['age','pclass']] = dataframe

indexLoc = data.iloc[0:2,0:2]       #(localisation par index: index localisation qui permets le mm indexing que sur numpy,
                                    #travaille sur les lignes)
print(indexLoc)                     


# locolumn = data.loc[0:2]         #travaille sur les colonnes, : dit que l'on veut toutes les colonnes
# print(locolumn)


