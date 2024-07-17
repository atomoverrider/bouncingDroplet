
"""
Simulating an oscillating spring with a ball falling under gravity. When the ball is bellow the spring surface, it feels a force which throws it back upwards. The simulation is then plotted with respect to time.
"""

import numpy as np
import matplotlib.pyplot as plt

# FIXED VARIABLES

m=1 # Mass
k=100 # Spring Constant
g=9.8 # Gravitational acceleration
gamma=1 # Linear Damping Constant
dt=1e-3 # Time step
T=100 # Total Time

# FIGURE INITIALISATION

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

#Avals=[0.3,0.32,0.35,0.351,0.3512]
Avals=[0.351199959] # Amplitude values
omega=6 # Oscillation frequency

# --------------------- MAIN LOOP START -------------------
for A in Avals: # Running through different amplitude values
    x=[1.1]
    vx=[0]
    t=[0]
    for i in range(int(T/dt)): # Main simulation loop
        x1=A*np.sin(omega*t[-1]) # Spring surface oscillation
        ic=int(x[-1]<x1) # ic is 1 whe ball is below spring surface and 0 when above
        
        fx=-m*g-ic*k*(x[-1]-x1)-ic*gamma*vx[-1] # Force calculation 
        
        # Ball Dynamics
        x+=[x[-1]+vx[-1]*dt]
        vx+=[vx[-1]+(fx/m)*dt]
        
        t+=[t[-1]+dt]
        #plt.plot(0,x[-1],'o')
        #plt.ylim([-10,10])
        #plt.show()
    
    ax.plot(t,np.array(x),label='Particle Position')

# --------------------- MAIN LOOP END -----------------------

#OUTPUT

ax.plot(t,A*np.sin(omega*np.array(t)),'k--',label='Surface Position')
    
ax.legend()
ax.set_xlabel('Time(s)')
ax.set_ylabel('Ball Position(m)')
ax.set_title('Amplitude of oscillation = '+str(A)+'(m)')
ax.set_xlim([90,100])
ax.set_ylim([-1,6])
fig.savefig('/home/kripa/param_osc_surface/periodically_forced_spring_A='+str(A)+'.png')