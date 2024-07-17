#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:19:26 2021

@author: kripa
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:29:24 2021

@author: kripa
"""
# dx/dt=5 
import matplotlib.pyplot as plt
import numpy as np

x=[0.1]
y=[0]
xnew=x[0]
ynew=y[0]
mx=1
my=0.001
k=10
L=0.5
vx=[0]
vy=[0]
vxnew=vx[0]
vynew=vy[0]

g=9.8

deltat=1e-3
t=[0]
tnew=t[0]
energy=[0.5*mx*vxnew**2+0.5*my*vynew**2+mx*g*xnew+my*g*ynew+0.5*k*ynew**2]
xcm=(mx*xnew+my*ynew)/(mx+my)
xd=xnew-ynew
vxcm=(mx*vxnew+my*vynew)/(mx+my)
vxd=vxnew-vynew

#TE=[0.5*k*x[-1]**2+0.5*m*v[-1]**2]
for i in range(int(1e5)):
    if xnew>ynew:
        ax=-g
        ay=-g-k*(ynew)/my
        xnew=xnew+vxnew*deltat
        ynew=ynew+vynew*deltat
        xcm=(mx*xnew+my*ynew)/(mx+my)
        vxnew+=(ax)*deltat
        vynew+=(ay)*deltat
        enew=0.5*mx*(vxnew**2)+0.5*my*(vynew**2)+mx*g*xnew+my*g*ynew+0.5*k*(ynew**2)
    if xnew<=ynew:
        xcm=(mx*xnew+my*ynew)/(mx+my)
        xd=xnew-ynew
        vxcm=(mx*vxnew+my*vynew)/(mx+my)
        vxd=vxnew-vynew
        axcm=-g-k*xcm/(mx+my)
        axd=-k*(mx+my)*xd/(mx*my)
        xcm+=vxcm*deltat
        xd+=vxd*deltat
        vxcm+=(axcm)*deltat
        vxd+=axd*deltat
        xnew=((mx+my)*xcm+mx*xd)/(mx+my)
        ynew=((mx+my)*xcm-my*xd)/(mx+my)
        vxnew=((mx+my)*vxcm+mx*vxd)/(mx+my)
        vynew=((mx+my)*vxcm-my*vxd)/(mx+my)
        

        enew=0.5*mx*(vxnew**2)+0.5*my*(vynew**2)+mx*g*xnew+my*g*ynew+0.5*k*(xnew)**2+0.5*k*(ynew**2)
        #break
    
    tnew+=deltat
  
    if i%1==0:
        x.append(xnew)
        y.append(ynew)
        vx.append(vxnew)
        vy.append(vynew)
        t.append(tnew)
        energy.append(enew)
        plt.plot(1,xnew,'ro')
        plt.plot(1,ynew,'bo')
        plt.plot(1,xcm,'ko')
        plt.xlim([0,1.5])
        #plt.ylim([-5,5])
        plt.show()

x=np.array(x)
y=np.array(y)
vx=np.array(vx)
vy=np.array(vy)
plt.plot(energy)
    

#print(x)
#print(t)    
#plt.plot(t,x)
