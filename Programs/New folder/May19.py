#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:02:59 2021

@author: kripa
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 13:42:32 2021

@author: kripa
"""

import numpy as np
import matplotlib.pyplot as plt

L=2
N=100
dx=L/N

ux=np.zeros(N)
duxdt=np.zeros(N)
#uy=0.01*np.random.randn(N)
uy=0.00*np.sin(2*10*np.pi*np.arange(N)*dx/L)
duydt=np.zeros(N)
dt=1e-4
k=0
xp=L/3
yp=5e-1
vxp=0
vyp=0
g=-9.8
k1=10e-1
m=1e-5
ms=1
xpp=[]
ypp=[]
cp=0
en=[]
omega_f=3
n=5
gamma=(omega_f*N/(2*np.pi*n))**2#*np.pi))**2
t=0
a=0.7
damping=0.1

for i in range(int(1e7)):
    t+=dt 
    loc=int(xp/dx)
    cp=int(yp<uy[loc])
    
    
    duydx=(np.roll(uy,-1)-np.roll(uy,+1))/(2*dx)
    
    
    
    axp=k1*cp*(yp-uy[loc])*duydx[loc]/(m*(1+duydx[loc]**2)**(1))
    ayp=g-k1*cp*(yp-uy[loc])/(m*(1+duydx[loc]**2)**(1))
    xp=(xp+vxp*dt)%L
    vxp=vxp+axp*dt
    yp=yp+vyp*dt
    vyp=vyp*(1-0.001*cp)+ayp*dt
    xpp.append(xp)
    ypp.append(yp)
    
    #d2uxdt2=gamma*(1+a*np.cos(omega_f*t))*(np.roll(ux,1)+np.roll(ux,-1)-2*ux)/2;#-m*axp/ms
    d2uydt2=gamma*(1+a*np.cos(omega_f*t))*(np.roll(uy,1)+np.roll(uy,-1)-2*uy)/2;#-m*(ayp-g)/ms
    #d2uxdt2[loc]+=-m*axp/ms
    d2uydt2[loc]+=-m*(ayp-g)/ms
    #duxdt=duxdt*(1-damping*dt)+d2uxdt2*dt
    duydt=duydt*(1-damping*dt)+d2uydt2*dt
    #ux=ux+duxdt*dt
    uy=uy+duydt*dt
    uy[0]=0
    uy[L-1]=0
    
    if i%10000==0:    
        plt.plot(np.arange(0,L,L/N)+ux,uy)
        plt.plot(xpp,ypp,'r')
        plt.plot(xp,yp,'ro')
        #plt.ylim(-5e0,5e0)
        plt.show()
        en+=[-m*g*yp+0.5*m*(vxp**2+vyp**2)+cp*0.5*k1*(yp-uy[(int(xp))])**2*(1/(1+duydx[loc]**2))]