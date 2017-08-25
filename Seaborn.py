#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:07:41 2017

@author: Anderson Banihirwe

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('seaborn')
import seaborn as sns

x = np.linspace(1, 7, 50)
print(x)

y = 3 + 2*x + 1.5*np.random.randn(len(x))
df = pd.DataFrame({'xData':x, 'yData':y})

print(df.head())
sns.regplot('xData', 'yData', data=df)
plt.show()