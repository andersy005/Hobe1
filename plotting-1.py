#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:35:40 2017

@author: Anderson B.
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('seaborn')
import numpy as np

# Generate the data
x = np.arange(0, 10, 0.2)
y = np.sin(x)
z = np.cos(x)

print(x)

# Generate the plot
plt.plot(x, y)

plt.show()


# Generate the figure and the axes
fig, axs = plt.subplots(nrows=2, ncols=1)

# On the first axis, plot the sine and label the ordinate
axs[0].plot(x, y)
axs[0].set_ylabel('Sine')

# On the second axis, plot the cosine
axs[1].plot(x, z)
axs[1].set_ylabel('Cosine')


plt.show()