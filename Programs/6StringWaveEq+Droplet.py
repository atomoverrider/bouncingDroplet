
"""
This program simulates a string surface made of discrete points which follow the wave equation solved using Forward Euler Method. There is droplet bouncing on the surface at a fixed horizontal position. The collision is calculated using an instantaneous dent formation on the surface.
"""
import numpy as np
import matplotlib.pyplot as plt

n = 100 # No. of point on the string
L = 20 # Length of Dish
x = np.linspace(0,L,n) # Dish Array

# ----------------- INITIAL STRING SHAPE ---------------------

y, y_old = np.zeros(n), np.zeros(n)
v, v_old = np.zeros(n), np.zeros(n)

"Assymetrical pluck"
#y_old[0:10] = 1.0/x[10]*x[0:10]
#y_old[10:n-2]=1.0/(x[n-1]-x[10])*np.flip(x[10:n-2])

"Symmetrical pluck"
#y_old = np.sin(np.pi*x)

"Assymetrical bump"
#y_old[5:20]=0.5*np.sin(np.pi/(x[20]-x[5])*(x[5:20]-x[5]))

"Symetrical bump"
#y_old[16:31]=0.5*np.sin(np.pi/(x[20]-x[5])*(x[5:20]-x[5]))

# --------------------------------------------------------------

# FIXED VARIABLES

dt = 1e-3
dx = x[1]-x[0]
c = 3.0
g = -30 # Gravitational Acceleration

f = 15 # Forcing Amplitude
omega = 100 # Forcing Frequency
gamma = 0.2 # Damping constants for horizonatl and vertical directions
gamma1 = 0.1 

t = 0 # Initial time
t2 = t # Reset time after each collision

l = int(n/2) # Horizontal position of particle (Discrete space of dish)

# DENT CALCULATION FUNCTIONS

def calc_dent(relV, C, l):
    dent = np.zeros(n)
    a = np.floor(relV*C/dx)
    b = x[l+3]-x[l]
    for i in range(3):
        dent[l+i]=dent[l-i]=-b*np.sqrt(1-(x[l+i]-x[l])**2/a**2)
    return dent

def alt_dent(relV,C,l):
    # Using Relative velocity of particle to surface, magnitude of relV, horizontal position of particle
    # Output is a gaussian curve centered at the particle
    a=relV*C
    dent=-a*np.exp(-(x-x[l])**2/(4*dx)**2)
    return dent
    
# PARTICLE COORDINATES

b = np.array((x[l], 0.1)) # Position
v_b = np.array((0.01, 0.0)) # Velocity
theta = 0 # Slope angle with respect to x axis

# DATA COLLECTION VARIABLES

data = np.zeros(0)
data2 = np.zeros(0)
rels=[]

# ---------------------- MAIN LOOP START ---------------------------

while True:
    # Instantaneous value of forcing
    m = f*np.cos(omega*t)
        
    # SURFACE DYNAMICS - Forward Euler Method
    for i in range(1,n-1):
        v[i] = dt*c**2/dx**2*(y[i+1]+y[i-1]-2*y[i])+v_old[i]+m*dt
    v[0]+=m*dt
    v[n-1]+=m*dt    
    
    for i in range(n):
        y[i] = dt*v[i] + y_old[i] 
    
    # DROPLET DYNAMICS
    v_b[1] += g*t2
    b += v_b*dt
    p = b[0]-x
    l = np.where(np.abs(p)==np.min(np.abs(p)))[0][0]
    
    #COLLISION DYNAMICS
    if b[1]<=y[l]:
        theta = np.arctan((y[l+2]-y[l-2])/4/dx)
        
        c,s = np.cos(theta),np.sin(theta)
        
        dent=alt_dent(v[l]-v_b[1],0.02,l)
        y+=dent
        b[1] = y[l]
        
        v_perp = gamma*(v[l]*c - v_b[0]*s-v_b[1]*c)+v[l]*c
        v_para = gamma1*(v[l]*s - v_b[0]*c-v_b[1]*s)+v[l]*s
        
        v_b[0] = v_perp*s + v_para*c
        v_b[1] = v_perp*c + v_para*s
        
        #v[l-2:l+2]=-0.2*(v[l-2:l+2]-v_b[1])+v[l-2:l+2]
        
        t2 = 0
    

    data = np.append(data,b[0])
    data2 = np.append(data2,y[l])
    
    if t>3:
        break
    
    t+=dt
    t2+=dt 
    v_old = np.copy(v)
    y_old = np.copy(y)
    
    # OUTPUT
    rels+=[v[0]]
    plt.ylim(-10,10)
    plt.plot(x,y)
    plt.plot(b[0],b[1],'o')
    plt.plot(rels)
    plt.show()  
    
# ------------------------ MAIN LOOP END -------------------------
plt.plot(np.arange(0,t,dt),data[0:len(data)-1])
plt.show()
