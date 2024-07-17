
"""
This program simulates a string surface made of discrete points which follow the wave equation solved using the Spectral Method. Particle Bouncing snippet exists but requires review
"""
import numpy as np
import matplotlib.pyplot as plt

# SURFACE DIMENSIONS

n = 64 # No. of points on surface
L = 5 # Length of surface
x = np.linspace(0,L,n) # Surface Array

y = np.zeros(n) # Surface Profile


u, u_old = np.ones(n)*(0j), np.fft.fft(y) # Fourier Transform of Surface
v, v_old = np.ones(n)*0j, np.ones(n)*0j # Velocity of FT


# FIXED VARIABLES

dt = 1e-2 # Time Step
c = 2.2 # Wave equation constant
v_gamma = 0 #
f = 2 # Forcing Amplitude

time = np.arange(0,10, dt) # Time array
k = n*np.fft.fftfreq(n) # Wave numbers of FT

# PARTICLE VARIABLES

l=n//3 # Particle postion with respect discrete surface
bx,by=x[l],2 # Coordinates
vy=0 # Verticle velocity
t2 = 0

for t in time:
    
    # SURFACE DYNAMICS
    u = v*dt + u_old
    v = -k**2*c**2*u*dt + v_old*(1-v_gamma)

    m = 10*np.cos(50*t)
    
    y = np.fft.ifft(u) + m*dt
    
    # PARTICLE DYNAMICS
    vy += -30*t2
    by += vy*dt
    if by<=y[l]:
        by=y[l]
        relV = m+np.fft.ifft(v)[l] - vy
        y+=-relV*0.003*np.exp(-(x-x[l])**2/0.2)
        vy = relV*(1.1)+vy
        t2=0
        
    t2+=dt
    
    u_old = np.fft.fft(y)
    v_old = np.copy(v)
    
    # OUTPUT
    plt.ylim(-2,2)
    plt.plot(bx,by,'o')
    plt.plot(x,y.real)
    plt.show()
    
