# REQUIRES REVIEW AND RECTIFICATION
"""
This program simulates a string surface made of discrete points which follow the wave equation solved using the Leap Frog Method. There is droplet bouncing on the surface at a fixed horizontal position. The collision is calculated using an instantaneous dent formation on the surface.
"""
import numpy as np
import matplotlib.pyplot as plt

# DISH DIMENSIONS

n = 100 # No. of points on Dish
L = 20 # Length of Dish
x = np.linspace(0,L,n) # Surface Array

y, y_old = np.zeros(n), np.zeros(n) # Surface Profiles 
v_new, v, v_old = np.zeros(n), np.zeros(n), np.zeros(n) # Surface Velocity Profiles

# ----------------- INITIAL SURFACE SHAPE ---------------------

"Assymetrical pluck"
#y_old[0:10] = 1.0/x[10]*x[0:10]
#y_old[10:n-2]=1.0/(x[n-1]-x[10])*np.flip(x[10:n-2])

"Symmetrical pluck"
#y_old = np.sin(10*np.pi*x)

"Assymetrical bump"
#y_old[5:20]=0.5*np.sin(np.pi/(x[20]-x[5])*(x[5:20]-x[5]))

"Symetrical bump"
#y_old[16:31]=0.5*np.sin(np.pi/(x[20]-x[5])*(x[5:20]-x[5]))

#y_old=0.5*np.exp(-(x-x[int(len(x)/2)])**2/0.05)

# --------------------------------------------------------------

# FIXED VARIABLES

dt = 1e-2
dx = x[1]-x[0]
c = 10
d = 0.5*(x[1]-x[0])**4
g = -30 # Gravitational Acceleration


f = 1+0.005*175 # Forcing Amplitude
omega = 5 # Forcing Frequency
gamma = 0.2 # Damping constants for horizonatl and vertical directions
gamma1 = 0.2
eta = 0 # Surface Damping Constant

t = 0 # Initial Time
t2 = t # Reset time after each collision

t_osc = np.arange(0,np.pi,dt) # Fixed time period devitions
v_osc = f*np.sin(omega*t_osc) # Forcing Velocities for a time period

l = int(n/2) # Horizontal position of particle (Discrete space of dish)
dent = np.zeros(n)

# DENT CALCULATION FUNCTIONS

def calc_dent(relV, C):
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

b = np.array((x[l], 2)) # Position
v_b = np.array((0.01, 0.0)) # Velocity
theta = 0 # Slope angle with respect to x axis

# DATA COLLECTION VARIABLES

data = np.zeros(0)
data2 = np.zeros(0)
time = np.zeros(0)

# INITIALISATION

for i in range(1,n-1):
    v_new[i] = dt*c**2/dx**2*(y[i+1]+y[i-1]-2*y[i])/2+v_old[i]


# ---------------------- MAIN LOOP START ---------------------------

while b[0]<=20 and b[0]>=0 and t<400:
    # Instantaneous forcing velocity
    m = v_osc[len(t_osc)-1-int(t/dt)%len(t_osc)]
    
    #SURFACE DYNAMICS
    
    for i in range(1,n-1):
        y[i] = y_old[i]+ v_new[i]*dt 
        
    y[0]+=m*dt
    y[n-1]+=m*dt
    
    v_old[:]=v_new[:]
    
    
    for i in range(1,n-1):
        v_new[i] = (1-eta*dt)*v_old[i] + dt*c**2/dx**2*(y[i+1]+y[i-1]-2*y[i])
     
    #v[0:2]=v[n-2:n]=m
    
    t+=dt

    
    # PARTICLE DYNAMICS
    
    v_b[1] += g*t2
    b += v_b*dt
    p = b[0]-x
    l = np.where(np.abs(p)==np.min(np.abs(p)))[0][0]
    
    #COLLISION DYNAMICS
    if b[1]<=y[l]:
        theta = np.arctan((y[l+2]-y[l-2])/4/dx)
        v_ins = v_new[l]+ m
        c,s = np.cos(theta),np.sin(theta)
        
        
        dent=alt_dent(c*(v_ins-v_b[1]),0.001,l)
        y+=dent
        
        b[1] = y[l]#+0.05
        
        v_perp = gamma*(v_ins*c - v_b[0]*s-v_b[1]*c)+ v_ins*c
        #v_para = v_b[0]*c + v_b[1]*s
        v_para = gamma1*(v_ins*s - v_b[0]*c-v_b[1]*s)+ v_ins*s
        
        #print(v_b)
        
        v_b[0] = v_perp*s + v_para*c
        v_b[1] = v_perp*c + v_para*s
        #data2=np.append(data2,b[0])
        time = np.append(time,t)
        #v[l-2:l+2]=-0.2*(v[l-2:l+2]-v_b[1])+v[l-2:l+2]
        #print(v_b,(y[l+2]-y[l-2])/4/dx, theta)
        t2 = 0
    
    t2+=dt
    data = np.append(data,b[0])
    #if t%10<1:
    #plt.ylim(-5,5)
    #plt.plot(x,y)
    #plt.plot(b[0],b[1],'o')
    #plt.show()   
    
    y_old = np.copy(y)
    #v_old = np.copy(v)
    #v = np.copy(v_new)

# ------------------------ MAIN LOOP END -------------------------

plt.plot(np.arange(0,t,dt)[0:len(data)-1],data[0:len(data)-1])
plt.ylim(0,20)
#plt.plot(time[0:len(data2)-1],data2[0:len(data2)-1],'-o')
plt.show()
    