#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:55:24 2020

@author: atom
"""

import numpy as np
import matplotlib.pyplot as plt

N = 30
L = 10

p = np.zeros([N,2])
p[:,0]=np.linspace(0,L,N)
#p[:,1]=-10*np.sin(np.pi*p[:,0]/L)


dt = 0.01

L = L/(N-1)-0.35
k = 8000
v=0
gamma = 1

omega = 50
t=0
f=0.2


while True:
    delL = -np.roll(p,2)+p
    delR = -np.roll(p,-2)+p
    lL=np.sqrt(delL[:,0]**2+delL[:,1]**2)-L
    lR=np.sqrt(delR[:,0]**2+delR[:,1]**2)-L
    
    force = f*np.cos(omega*t)
    fa = np.vstack((-k*lL*np.divide(delL[:,0],lL+L),-k*lL*np.divide(delL[:,1],lL+L))).T
    fb = np.vstack((-k*lR*np.divide(delR[:,0],lR+L),-k*lR*np.divide(delR[:,1],lR+L))).T
    fNet = fa+fb
    #fNet[0,:]=fNet[N-1,:]=[0,force]
    v = gamma*v+fNet*dt+f*omega*np.sin(omega*t)
    v[0,:]=v[N-1,:]=[0,f*omega*np.sin(omega*t)]
    v[:,0]=0*v[:,0]
    p = p + v*dt
    t+=dt
    
    plt.xlim(-5,15)
    plt.ylim(-50,50)
    plt.plot(p[:,0],p[:,1],'-')
    plt.show()