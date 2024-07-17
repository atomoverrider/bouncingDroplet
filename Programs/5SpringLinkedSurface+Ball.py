
"""
Simulation of a surface interlinked with springs with fixed spring constants. A ball falling under gravity experiances a force due to the shape of the surface.
"""

import numpy as np
import matplotlib.pyplot as plt

# SURFACE DIMENSIONS

L=10 # Surface length
N=1000 # No. of points
dx=L/N # Length Discretization

ux=np.zeros(N) # x axis coordinates
duxdt=np.zeros(N) # x axis first derivative
uy=0.1*np.sin(2*2*np.pi*np.arange(N)*dx/L) # y axis coordinate
duydt=np.zeros(N) # y axis first derivative

# FIXED VARIABLES

dt=1e-5 # Time step
k=5 # Spring constant of surface
xp=L/2 # Ball x coordinate
yp=0.5e0 # Ball y coordinate
vxp=0 # Ball velocities
vyp=0
g=-9.8 # Gravitational acceleration
k1=10 # Ball's spring constant
m=1e-3 # Ball mass

# DATA COLLECTION VARIABLES

xpp=[]
ypp=[]
en=[] # Energy

cp=0

for i in range(int(1e7)):
    
    loc=int(xp/dx) # Ball location in descrete units
    cp=int(yp<uy[loc]) # cp is 1 if ball is below surface and 0 if above
    
    #Surface Dynamics
    
    d2uxdt2=k*(np.roll(ux,1)+np.roll(ux,-1)-2*ux)/dx**2
    d2uydt2=k*(np.roll(uy,1)+np.roll(uy,-1)-2*uy)/dx**2
    duxdt=duxdt+d2uxdt2*dt
    duydt=duydt+d2uydt2*dt
    
    duydx=(np.roll(uy,-1)-np.roll(uy,+1))/(2*dx)
    
    # Ball Dynamics
    
    axp=k1*cp*(yp-uy[loc])*duydx[loc]/(m*(1+duydx[loc]**2)**(1))
    ayp=g-k1*cp*(yp-uy[loc])/(m*(1+duydx[loc]**2)**(1))
    xp=xp+vxp*dt
    vxp=vxp+axp*dt
    
    yp=yp+vyp*dt
    vyp=vyp+ayp*dt
    xpp.append(xp)
    ypp.append(yp)
    
    # Output
    
    if i%10000==0:    
        plt.plot(np.arange(N)*dx+ux,uy)
        plt.plot(xpp,ypp,'r')
        plt.plot(xp,yp,'ro')
        plt.ylim(-1,2)
        plt.show()
        en+=[-m*g*yp+0.5*m*(vxp**2+vyp**2)+cp*0.5*k1*(yp-uy[(int(xp))])**2*(1/(1+duydx[loc]**2))]