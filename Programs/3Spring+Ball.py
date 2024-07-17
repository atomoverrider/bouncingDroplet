
"""
To simulate a ball falling due to gravity on a spring. Various spring constants are simulated and the dynamics are plotted through time.
"""

import numpy as np
import matplotlib.pyplot as plt

# FIXED VARIABLES

x=[1e-3] # List of verticle positions
vx=[0] # List of verticle velocities
t=[0] # List of time stamps
m=1e-9 # Mass of ball
kvals=[1,10,100,1000] # Various spring constants
g=9.8 # Gravitational acceleration
gamma=1 # Linear Damping constant
dt=0.0001 # Time step
T=10 # Total time

# FIGURE INITIALISATION

fig=plt.figure() 
ax=fig.add_subplot(1,1,1)

# ---------------------- MAIN LOOP START ---------------------
for k in kvals: # Running through different spring constants
    x=[10]
    vx=[0]
    t=[0]
    for i in range(int(T/dt)): # Main Simulation Loop
        ic=int(x[-1]<0) # ic is 1 when ball is below 0 and 0 when above
        
        fx=-m*g-ic*k*x[-1]-ic*gamma*vx[-1] # Force Calculation
        
        # Ball Dynammics
        x+=[x[-1]+vx[-1]*dt]
        vx+=[vx[-1]+(fx/m)*dt]
        
        t+=[t[-1]+dt]
    
    ax.plot(t,x,label='k='+str(k))

# ---------------------- MAIN LOOP END ---------------------    
ax.legend()
ax.set_xlabel('Time(s)')
ax.set_ylabel('Ball Position(m)')
ax.set_title('Ball falling on a spring under gravity')
#fig.savefig('/home/kripa/param_osc_surface/ball_spring_bounce_damped')