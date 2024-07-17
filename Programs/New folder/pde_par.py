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

import numpy as np
import matplotlib.pyplot as plt



L=100
u=0.0*np.random.randn(L)
v=np.zeros(L)
omega_f=8
gamma=omega_f**2*(1/2)**2+0

x=L/2
y=0.1
vx=0
vy=0
m=1e-5
g=9.8
t=0
dt=0.1
c=1
a=0.4
damping=0.8
    
data=np.zeros(0)

while True:#np.max(u)<1 and t<1000:   
    ic= int(y<u[int(x)] and vy<v[int(x)])#impactful contact
    pressure=np.zeros(L)
    pressure[int(x)]=ic*m*g
    dvdt=c**2*(np.roll(u,1)+np.roll(u,-1)-2*u)/2 -gamma*(1+a*np.cos(omega_f*t))*u-pressure
    v=v+dvdt*dt-damping*v*dt
    u=u+v*dt
    
    
    t+=dt
    ay=-g-ic*200*(y-u[int(x)])  
    vy+=ay*dt
    y+=vy*dt
    plt.plot(10000*u)
    plt.plot(x,y,'o')
    plt.ylim(-1,1)
    plt.show()
        
    