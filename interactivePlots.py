#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:56:07 2017

@author: Anderson Banihirwe
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
matplotlib.style.use('seaborn')
import numpy as np

try:
    import tkinter as tk
    
except ImportError:
    import Tkinter as tk
    
    
t = np.arange(0, 10, 0.1)
c = np.cos(t)
s = np.sin(t)

def normalPlot():
    '''Just show a plot. The progam stops, and only continues
    when the plot is closed,
    either by hitting the "Window Close" button, or by typing
    "ALT+F4". '''
    
    
    plt.plot(t, s)
    plt.title('Normal plot: you have to close it to continue\
              by clicking the "Window Close" button, or by hitting "ALT+F4"')
    plt.show()
    
    
def positionOnScreen():
    '''Position two plots on your screen. This uses the
    Tickle-backend, which I think is the default on all
    platforms.'''
    
    
    
    # Get the screen size
    root = tk.Tk()
    (screen_w, screen_h) = (root.winfo_screenwidth(),
                            root.winfo_screenheight())
    root.destroy()
    
    def positionFigure(figure, geometry):
        ''' Position one figure on a given location on the screen.
        This works for Tk and for Qt5 backends, but may fail on others.'''
        
        mgr = figure.canvas.manager
        (pos_x, pos_y, width, height) = geometry
        
        try:
            position = '{0}x{1}+{2}+{3}'.format(width, height, pos_x, pos_y)
            mgr.window.geometry(position)
            
        except TypeError:
            mgr.window.setGeometry(pos_x, pos_y, width, height)
            
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(t, c)
    ax.set_title('Top Left: Close this one last')
    
    
    topLeft = (0, 0, screen_w//2, screen_h//2)
    positionFigure(fig, topLeft)
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(t, s)
    
    ax2.set_title('Top Right: Close this one first (e.g. with ALT+F4)')
    topRight = (screen_w//2, 0, screen_w//2, screen_h//2)
    positionFigure(fig2, topRight)
    plt.show()
    
    

    
    
    
    
if __name__ == '__main__':
    normalPlot()
    positionOnScreen()