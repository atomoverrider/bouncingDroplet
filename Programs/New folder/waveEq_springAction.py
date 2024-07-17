#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:25:21 2021

@author: atom
"""

import numpy as np
import matplotlib.pyplot as plt

L = 100 #Number of points
l = 0.1 #Dish Length

yn, yo = np.zeros(L), np.zeros(L) #Vertical height
v = np.zeros(L) #Angular velocities
c=1

m=0.1
mc=2
k=100
g=9.8
gamma=0
dt=1e-4
T=10

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
#Avals=[0.3,0.32,0.35,0.351,0.3512]
Avals=[0]
omega=6

dataz,datay = [],[]

for A in Avals:
    by=[0.1]
    bx=[l/3]
    vy=[0]
    vx=[0]
    t=[0]
    dataz=[0]
    z=int(bx[-1]/l*L)
    for i in range(int(T/dt)):
        x1=A*np.sin(omega*t[-1])+yn
        ic=int(by[-1]<x1[z])
        fx=-m*g-ic*k*(by[-1]-x1[z])-ic*gamma*vy[-1]
        by+=[by[-1]+vy[-1]*dt]
        vy+=[vy[-1]+(fx/m)*dt]
        
        #v[z]+=ic*(-fx/mc)*dt
        dvdt=c**2*(np.roll(yn,1)+np.roll(yn,-1)-2*yn)/2
        v=v+dvdt*dt
        v[z]=v[z]+ic*(-fx/m)*dt
        yn=yn+v*dt
        yn[0]=yn[-1]=0
        
        t+=[t[-1]+dt]
        dataz.append(x1[z])

        if 1000.0//(i+1)==0:
             plt.ylim(-0.1,0.1)
             plt.plot(np.linspace(0,l,L),1*x1,'-')
             plt.plot(bx[-1],by[-1],'o')
             plt.show()
#    
#plt.xlim(90,100)    
plt.plot(t,by,'-')
plt.plot(t,dataz,'-')
#plt.ylim([-0.0030,-0.0005])
plt.show()
