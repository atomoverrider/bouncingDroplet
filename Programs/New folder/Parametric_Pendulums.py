#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:38:48 2020

@author: atom
"""

import numpy as np
import matplotlib.pyplot as plt

dt, dx = 0.005, 0

x, v, time = 0.00000001, 0, np.arange(0,200,dt)

g, f, l = 1, 1, 1

h, omegaNot = f/g, np.sqrt(g/l)

epsilon = 0

data = 2*np.zeros(0)

omega = 2*omegaNot + epsilon

for t in time:
    x = v*dt + x
    v = (f*np.cos(omega*t)-g)/l*x*dt + v    
    data = np.append(data, x)
    #plt.xlim(-1,1)
    #plt.plot(x,0,'o')
    #plt.plot(0,f*np.cos(omega*t)+1,'o')
    #plt.show()
    
plt.plot(time, data, '-')
plt.show()