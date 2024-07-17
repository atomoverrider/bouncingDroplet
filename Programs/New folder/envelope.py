#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:11:27 2021

@author: kripa
"""

import numpy as np
import matplotlib.pyplot as plt

L=100
theta=0.1*np.random.randn(L)#0.1*np.sin(np.pi*10*np.arange(L)/L)
thetadot=np.zeros(L)
wavedamping=5
omega_f=6.3
g=9.8
h=0*(g/omega_f**2)
l=1
k=10000
t=0
dt=0.001

while t<100:
    thetadotdot=(g/l)*(1-h*omega_f**2/g*np.sin(omega_f*t))*np.sin(theta)+k*(np.roll(theta,1)+np.roll(theta,-1)-2*theta)
    thetadot=thetadot*(1-wavedamping*dt)+thetadotdot*dt
    theta=theta+thetadot*dt
    t=t+dt
    plt.plot(theta)
    plt.show()
    #plt.ylim([-0.1,0.1])