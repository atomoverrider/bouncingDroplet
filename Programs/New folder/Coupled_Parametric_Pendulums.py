#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:22:42 2020

@author: atom
"""

import numpy as np
import matplotlib.pyplot as plt

n, timeLength = 11, 200

dt, dx = 0.01, 0.01

x, v, time = np.zeros(n), np.zeros(n), np.arange(0,timeLength,dt)
x[n//2] =0.1
#x = 0*np.exp(-(np.arange(0,n,1)-n//2)**2/20)

g, a, l, k = 9.8, 0.1, 1, 1

h, omegaNot = a/g, np.sqrt(g/l)

#epsilon = h*omegaNot/2

omega = 6.9

for t in time:
    
    x = v*dt + x
    v = -g/(l+a*np.cos(omega*t))*x*dt + v - k*(2*x-np.roll(x,1)-np.roll(x,-1))
    
    #v[0]=v[-1]=0
    if t>100:
        plt.ylim(0.1,-0.1)
        plt.plot(x+np.linspace(0,1,n),np.zeros(n),'o')
        #print(x)
        #plt.plot(0,f*np.cos(omega*t)+1,'o')
        plt.show()
    
#plt.plot(time, data, '-')
#plt.show()