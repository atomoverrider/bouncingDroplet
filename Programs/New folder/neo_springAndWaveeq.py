#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:22:14 2021

@author: atom
"""

import numpy as np
import matplotlib.pyplot as plt

N=13
y = 0.1*np.sin(np.linspace(0,3*np.pi,N))
v = np.zeros(N)
by = [0.2]
vy = 0
l = N//2

m=0.02
mu=0.01

k1=0.5
k2=5
g=0

T=10
dt=1e-5

data=[0]

f=0.1
omega=20
h=0.5

def energy(o=0):
    P = -m*g*by[-1] - mu*g*np.sum(y) + o*0.5*k1*(by[-1]-y[l])**2 + 0.5*k2*np.sum((np.roll(y,1)+np.roll(y,-1)-2*y)**2)
    K = 1/2*m*vy**2 + 1/2*mu*np.sum(v**2)
    
    return [K,P,K+P]

E,Kin,Pot = [energy()[-1]],[energy()[0]],[energy()[1]]

for t in range(int(T/dt)):

    #ic=int(vrel<0 and by[-1]<=y[l])
    ic=int(by[-1]<y[l])
    jc=int(k1*(by[-1]-y[l])<0)
    
    vrel=vy-v[l]
    Fs = k2*(1+f*np.cos(omega*t))*(np.roll(y,1)+np.roll(y,-1)-2*y)
    
    a = (Fs - mu*g)/mu
    a[l]+= ic*k1*(by[-1]-y[l])/mu
    
    v+=a*dt
    y+=v*dt
    y[0]=y[-1]=0
    v[0]=v[-1]=0
    
    data+=[y[l]]
    
    ap= (-ic*jc*k1*(by[-1]-y[l]) - m*g)/m
    vy+=ap*dt
    by+=[by[-1]+vy*dt]
    
    E+= [energy(ic)[-1]]
    Kin+=[energy(ic)[0]]
    Pot+=[energy(ic)[1]]
    
    # if ic and jc:
    #     y[l]=by[-1]
        
    if t%1000==0:
        plt.ylim(-0.2,0.2)
        plt.plot(np.arange(0,N,1),y,'-o')
        plt.plot(l,by[-1],'o')
        plt.show()