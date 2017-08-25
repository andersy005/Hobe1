#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 22:45:01 2017

@author: Anderson B
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
'Gender': ['f', 'f', 'm', 'f', 'm',
'm', 'f', 'm', 'f', 'm', 'm'],
'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,
5.1, 3.9, 3.7, 2.1, 4.3]
})

#print(data.head())


# Group the data
grouped = data.groupby('Gender')

print(grouped.head())
print(grouped.describe())


# Plot the data
grouped.boxplot()
plt.show()
 
# Get the groups as DataFrames
df_female = grouped.get_group('f')

print(df_female)

# Get the corresponding numpy-array
values_female = grouped.get_group('f').values

print(values_female)