"""
Program imports a function to plot a bifurcation graph with varying the amplitude of oscillation.
"""

import "-RigidSurfaceBifurcationWithBall"
import numpy as np
import matplotlib.pyplot as plt

mat=np.zeros([200,50]) # Grid variable

for i in range(200):
    g=0.1 # Linear Damping for the Ball
    amp=1+0.005*i # Amplitude of oscillation
    omega=5 # Frequency of oscillation
    
    a,c,p,d=rigidSimBifurcation.f(amp,g,omega,1500)
    x,y=np.histogram(d,bins=50,range=(0,14),density=True)
    mat[i,:]=x

# OUTPUT
    
plt.xlabel('Amplitude 1-2')
plt.ylabel('Droplet amplitude range')
plt.imshow(mat.T)