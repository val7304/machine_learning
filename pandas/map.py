# -*- coding:Utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#map() applique une fonction sur chaque éléments d'une colonne
# data['age'].map(lambda x: x+1)

# Modifier la colonne 'ag' pour créer 4 catégories: 
# cat1: <20ans
# cat2: 20-30ans
# cat3: 30-40 ans
# cat4:+40ans

def category_ages(age):
    if age <=20:
        return '<20 ans'
    elif (age>20) & (age <30):
        return '20-30 ans' 
    elif (age>30) & (age <40):
        return '30-40 ans'
    else: 
        return '+40 ans'


df = pd.read_excel(r"E:\workspace\python\machineLearning\pandas\titanic.xlsx", engine='xlrd')
data=df.drop(['name','sibsp','parch','ticket', 'parch', 'ticket','fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)


heading = data.head()
# print(heading)
mapping = data['age'].map(category_ages)
print(mapping)