#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:12:11 2020

@author: kripa
"""

import numpy as np
import matplotlib.pyplot as plt

omega=5
A=1+0.005*50
gamma=0.1
dt=0.01
t=np.arange(0,700,dt)
posf=0*np.ones(np.shape(t))
posf=A*np.sin(omega*t)
posp=[]
u=0
v=0
g=9.8
xp=A+0.5
tcoll=0.
for i in range(len(t)):
    xpo=xp
    xp=xp+v*dt
    if xp<posf[i]:
        #print(xpo,posf[i],xp)
        tcoll = t[i]
        vs=A*omega*np.cos(omega*t[i])
        u=-gamma*(v-vs)+vs
        xp=posf[i]
    v=u-g*(t[i]-tcoll)      
    posp+=[xp]
    
    
    
    # if abs(xp-posf[i])<0.1 or xp<posf[i]:
    #     tcoll=t[i]
    #     vs=A*omega*np.cos(omega*t[i])
    #     print('y',i)
    #     u=-gamma*(v-vs)+vs
       
plt.plot(t,posp,'r',t,posf,'b')
plt.xlim([220,250])
plt.ylabel('Position')
plt.xlabel('Time')
plt.legend(['Droplet','Surface'])
#plt.savefig('Simple_bouncing.png')
#plt.savefig('Period_doubling.png')