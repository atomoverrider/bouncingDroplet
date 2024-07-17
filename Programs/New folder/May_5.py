#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:24:52 2021

@author: kripa
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:22:18 2020

@author: kripa
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:14:28 2020

@author: kripa
"""

#Using periodic tension like Melde's string to get parametric oscillations

import numpy as np
import matplotlib.pyplot as plt



L=500
u=0.1*np.random.randn(L)
v=np.zeros(L)
omega_f=1
n=10
gamma=(omega_f*L/(2*np.pi*n))**2#*np.pi))**2

x=L/2
y=0.1
vx=0
vy=0
m=1e-5
g=9.8
t=0
dt=1e-4
k=1

a=0.4
damping=0.05

alpha=0
beta=60

data=np.zeros(0)
i=0
while True:#np.max(u)<1 and t<1000: 
    if t>700:
        break 
    i+=1
    ic= int(y<u[int(x)] and vy<v[int(x)])#impactful contact
    pressure=np.zeros(L)
    #pressure[int(x)]=ic*m*g
    #dvdt=c**2*(np.roll(u,1)+np.roll(u,-1)-2*u)/2 -gamma*(1+a*np.cos(omega_f*t))*u-pressure
    dvdt=gamma*(1+a*np.cos(omega_f*t))*(np.roll(u-alpha*u**3,1)+np.roll(u-alpha*u**3,-1)-2*u)/2 -beta*u**3
    v=v+dvdt*dt-damping*v*dt
    u=u+v*dt
    u[-1]=u[0]=0
    
    
    t+=dt
    ay=-g-ic*200*(y-u[int(x)])  
    vy+=ay*dt
    y+=vy*dt
    if i%10000==0:
        data = np.append(data,max(u))
        # plt.plot(1*u)
        # #plt.plot(x,y,'o')
        # #plt.ylim(-1e-1,1e-1)
        # plt.show()
     
plt.plot(data)
    