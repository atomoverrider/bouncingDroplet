
"""
This is a simulation of a rigid surface being oscillated at a fixed frequency and amplitude. A ball is falling under gravity that encounters the surface and bounces.
"""

import numpy as np
import matplotlib.pyplot as plt

# Function returns unique amplitudes of the simulation with corresponding counts for them
def f(amp,gam,o,n):
    
    omega=o # Frequency of oscillation
    A=amp # Amplitude of oscillation
    gamma=gam # Linear damping constant for the ball
    dt=0.01 # Time step
    t=np.arange(0,n,dt) # Time array
    posf=A*np.sin(omega*t) # Rigid surface position
    posp=[] # Ball position list
    u=0 # Ball velocity after collision
    v=0 # Ball velocity
    g=9.8 # Gravitational acceleration
    xp=A+0.5 # Ball position
    tcoll=0. # Time stamp at last collision
    
    for i in range(len(t)): # Main loop simulation
        # Ball dynamics
        xpo=xp
        xp=xp+v*dt
        
        # Collision dynamics
        if xp<posf[i]: # If ball is below rigid surface
            tcoll = t[i]
            vs=A*omega*np.cos(omega*t[i]) # Surface velocity
            u=-gamma*(v-vs)+vs
            xp=posf[i]
        v=u-g*(t[i]-tcoll)      
        posp+=[xp]
        
    # Computing unique amplitudes and how many times each of them occur
    b,c=posp>np.roll(posp,1),posp>np.roll(posp,-1)
    b,c=[i for i, x in enumerate(b) if x],[i for i, x in enumerate(c) if x]
    
    d=np.ndarray(0)
    
    for x in np.intersect1d(b,c):
        d=np.append(d,round(posp[x],2))
    
    amps,counts = np.unique(d,return_counts=True)
    
    inds = counts.argsort()
    amps,counts = amps[inds[::-1]],counts[inds[::-1]]
    
    peaks = [amps[i] for i, x in enumerate(counts) if x>0.2*counts[0]]
    
    return amps,counts,peaks,d
    # plt.title("Amplitude:"+str(amp)+" Gamma:"+str(gamma)+" Omega:"+str(o))
    # plt.xlabel("Time (dt=0.01)")
    # plt.ylabel("Ball Height")
    # plt.plot(posp[6000:8000])