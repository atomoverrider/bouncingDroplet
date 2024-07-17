#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:14:28 2020

@author: kripa
"""

import numpy as np
import matplotlib.pyplot as plt
L=100
u=0.1+np.zeros(L)
#u=0.01*np.random.rand(L)#np.sin(2*np.pi*np.arange(L)/L)
yn, yo = np.zeros(L), np.zeros(L)
v=np.zeros(L)
gamma=0.25
omega_f=1
t=0
dt=0.1
c=5
a=0.9





damping=1

l=0.1 #size of dish

bx,by=l/3,1
vx,vy=0,0.1
g=-9.8
t2=0

dent=np.zeros(L)

def alt_dent(relV,C,z):
    a=relV*C
    dent=-a*np.exp(-(np.linspace(0,l,L)-np.linspace(0,l,L)[z])**2/(l*0.001)**2)
    return dent

datax,datay = [],[]

while t<100:   
    
    dvdt=c**2*(np.roll(u,1)+np.roll(u,-1)-2*u)/2 - gamma*(1+a*np.cos(omega_f*t))*u
    v=v-damping*dt*v+dvdt*dt
    u=u+v*dt
    
    yn = gamma*a/omega_f**2*np.cos(omega_f*t) + 1-np.cos(u)
    v_actual = (yn-yo)/dt
    
    vy += g*t2
    vx+=-0*vx*dt
    bx+=vx*dt
    by+=vy*dt
    
    z = int(bx/l*L)
    
    if by<=u[z]:
        #datax.append(bx)
        theta = np.arctan((np.roll(u,1)[z]-np.roll(u,-1)[z])/4)
        v_ins = v_actual[z]
        #print(v_ins)
        cos,sin = np.cos(theta),np.sin(theta)
        
        by = u[z]#+0.05
        
        dent=alt_dent(cos*(v_ins-vy),0.0005,z)
        v=v+dent
        
        
        v_perp = 0.57*(v_ins*cos - vx*sin-vy*cos)+ v_ins*cos
        #v_para = v_b[0]*c + v_b[1]*s
        v_para = 0.57*(v_ins*sin + vx*cos-vy*sin)+ v_ins*sin
        
        #print(v_b)
        
        vx = v_perp*sin + v_para*cos
        vy = v_perp*cos + v_para*sin
        #data2=np.append(data2,b[0])
        #time = np.append(time,t)
        #v[l-2:l+2]=-0.2*(v[l-2:l+2]-v_b[1])+v[l-2:l+2]
        #print(v_b,(y[l+2]-y[l-2])/4/dx, theta)
        #print(v_perp,v_para,v_ins,vy)
        t2 = 0
    
    t+=dt
    t2+=dt
    
    yo = yn[:]
    datay.append(by)
#    if t>50:
#        break
    
    #plt.plot(np.linspace(0,l,L),10*u)
    #plt.plot(bx,by,'o')
    #plt.ylim(-5,5)
    #plt.plot(datax)
    #plt.show()
    
plt.plot(datay[400:],'-o')
#plt.ylim([-0.0030,-0.0005])
plt.show()
