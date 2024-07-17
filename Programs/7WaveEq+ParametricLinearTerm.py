
"""
A simulation of a parametrically oscillated equation, where a linear parametrically oscillated term is added to the wave equation instead of the wave eqation itself having a parametric term. Simulation can further produce a phase diagram according to values.
"""

import numpy as np
import matplotlib.pyplot as plt

# Function returns 1 if simulation is unstable and 0 if stable

def loop(gam,om,c_in,a_in,d_in):
    # FIXED VARIABLES
    
    L=100 # No. of points on the surface
    u=0.1*np.sin(10*np.pi*np.arange(L)/L) # Initial shape of surface
    v=np.zeros(L) # Velocity array for surface
    
    gamma=gam # Fixed coefficient of parametric term
    omega_f=om # Frequency of parametric term
    a=a_in # Amplitude of parametric term
    
    t=0 # Time
    dt=0.1 # Time step
    c=c_in # Tension in wave equation
    damping=d_in # Linear damping constant
    
    # Data collection variable
    data=np.zeros(0)

    while np.max(u)<1 and t<1000: # Main loop simulation
        # Wave equation + Linear parametrically oscillated term
        dvdt=c**2*(np.roll(u,1)+np.roll(u,-1)-2*u)/2 -gamma*(1+a*np.cos(omega_f*t))*u
        
        v=v+dvdt*dt-damping*v*dt
        u=u+v*dt
        t+=dt       
        
    # Instability condition    
    if np.max(u)>1:
        return 1
    else:
        return 0


# LOOPING THROUGH DIFFERNT PARAMETERS TO CREATE A PHASE DIAGRAM

p,q = 25,50
mat = np.zeros([p,q])

for i in range(p):
    for j in range(q):
        a=(i)/p
        gam=9/4+(j+1-q/2)/q
        mat[i,j]=loop(gam,1,5,a,0)

plt.xlabel('gamma centered at 9/4')
plt.ylabel('a 0-1')
plt.imshow(mat)
