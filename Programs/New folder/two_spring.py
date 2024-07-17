#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:07:22 2021

@author: kripa
"""

import numpy as np
import matplotlib.pyplot as plt

x=[1]
y=[0]
vx=[0]
vy=[0]
g=9.8
m1=1
m2=0.001
dt=1e-7
k1=100
k2=10
en=[m1*g]
xnew=x[-1]
ynew=y[-1]
vxnew=vx[-1]
vynew=vy[-1]

for i in range(int(5e7)):
    ic=int(xnew<ynew)
    ax=-m1*g-ic*k1*(xnew-ynew)
    ay=-m2*g+ic*k1*(xnew-ynew)-k2*ynew
    xnew=xnew+vxnew*dt
    ynew=ynew+vynew*dt
    vxnew=vxnew+ax*dt/m1
    vynew=vynew+ay*dt/m2
   
    if i%1e6==0:
        #plt.plot(1,xnew,'o',1,ynew,'o')
        #plt.ylim([-1,1])
        #plt.show()
        energy=0.5*m1*vxnew**2+0.5*m2*vynew**2+m1*g*xnew+m2*g*ynew+ic*0.5*k1*(xnew-ynew)**2+0.5*k2*ynew**2
        x.append(xnew)
        y.append(ynew)
        vx.append(vxnew)
        vy.append(vynew)
        en.append(energy)
    
plt.plot(en)