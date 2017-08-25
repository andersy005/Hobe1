#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:00:18 2017

@author: Anderson B
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm


# Generate a noisy line, and save the data in a pandas-DataFrame
x = np.arange(100)

y = 0.5*x - 20 + np.random.randn(len(x))

df = pd.DataFrame({'x':x, 'y':y})

print(df.head())


# Fit a linear model, using the "formula" language
# added by the pacakge "patsy"

model = sm.ols('y~x', data=df).fit()

print(model.summary())