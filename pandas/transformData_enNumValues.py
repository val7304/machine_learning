# -*- coding:Utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# convertion de strings en données numériques

# map()
# replace()
# cat.codes()

df = pd.read_excel(r"E:\workspace\python\machineLearning\pandas\titanic.xlsx", engine='xlrd')
data=df.drop(['name','sibsp','parch','ticket', 'parch', 'ticket','fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)


heading = data.head()
print(heading)

mapping = data['sex'].map({'male':0, 'female':1})       #tableau associatif
print(mapping)


remplacer=  data['sex'].replace(['male','female'], [0,1])
print(remplacer)

Datacodes = data['sex'].astype('category')
# print(Datacodes), astype ajoute une catégorie
# Name: sex, Length: 1309, dtype: category
# Categories (2, object): ['female', 'male']

Datacodes = data['sex'].astype('category').cat.codes
print(Datacodes)

# cat.codes: convertit les catégories en valeurs numérique




