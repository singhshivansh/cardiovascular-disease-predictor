# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:35:24 2020

@author: Shradha
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('cardio_train.csv', sep = ';')
df = df.drop('id', axis = 1)
v1 = np.percentile(df['age'], 1)
c = df[df['age'] < v1].count()
sns.jointplot('age', 'weight', data = df)