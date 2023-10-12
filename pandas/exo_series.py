# -*- coding:Utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Modifier la colonne 'ag' pour créer 4 catégories: 
# cat1: <20ans
# cat2: 20-30ans
# cat3: 30-40 ans
# cat4:+40ans


df = pd.read_excel(r"E:\workspace\python\machineLearning\pandas\titanic.xlsx", engine='xlrd')
data=df.drop(['sibsp','parch','ticket', 'parch', 'ticket','fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

# op. très courante; feature enginering
# data = data.dropna(axis=0)   
# moinsDe20 = data[data['age'] < 20].groupby(['name','pclass']).mean()
# print(moinsDe20)

data.loc[data['age']<=20, 'age'] = 0
data.loc[(data['age']>20) & (data['age']<30), 'age'] = 1
data.loc[(data['age']>30) & (data['age']<40), 'age'] = 2
data.loc[data['age']>40, 'age'] = 3

heading = data.head()
# print(heading)
count = data['age'].value_counts()
# print(count)
stat= data.groupby(['age']).mean()
print(stat)


