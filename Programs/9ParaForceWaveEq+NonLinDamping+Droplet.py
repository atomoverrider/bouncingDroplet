
"""
This program simulates the droplet bouncing on the dish. The dish follows the wave equation which is parametrically oscillated. It also has non linear damping parameters that can be controlled.
"""

# IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

# CONFIGURING A PLOT OBJECT

fig, ax = plt.subplots(figsize=(8,5))
ax.set_ylabel('Verticle Height', fontsize=15)
ax.set_xlabel('Dish Length', fontsize=15)

# CAMERA OBJECT

camera = Camera(fig)

# DISH DIMENSIONS - Length, No. of Points, Distance between points

L=10
N=500
dx=L/N

# COORDINATES OF POINTS OF DISH WITH TIME DERIVATIVES

ux=np.zeros(N)
duxdt=np.zeros(N)
uy=np.zeros(N)
duydt=np.zeros(N)

# FIXED VARIABLES

dt=1e-4 # Time step
xp=L/3 # Horizontal Position of Droplet
yp=5e-1 # Vertical Position of Droplet
vxp=0 # Horizontal Velocity
vyp=0 # Vertical Velocity
g=-9.8 # Gravitational constant
k1=10e-1 # Spring constant acting when droplet is below the dish surface
m=10e-6 # Mass of Droplet
ms=1 # Mass of Surface Points

# OSCILLATION PARAMETERS

omega_f=1 # Frequency
n=50 # No. of wavelengths to be excited
gamma=(omega_f*N/(2*np.pi*n))**2 # Calculated Tension
a=0.3 # Parametric oscillation amplitude
damping=0.1 # Linear Damping term

# NON LINEAR DAMPING PARAMETERS

alpha=0
beta=60

# STORAGE VARIABLES

xpp=[]
ypp=[]
z=[]
slopes=[]
en=[]

# INITIALISATION VALUES

cp=0
t=0


# -------------------------------------------------------------------

""" MAIN LOOP START """

for i in range(int(1e7)):
    if t>500: # When time reaches 500 units, end the loop
        break
    t+=dt
    loc=int(xp/dx) # Mapping the droplet position to one of the points on the dish
    cp=int(yp<uy[loc]) # 1 if droplet is below surface, 0 if above (Multiplied on forces acting below surface)
    
    # First order spatial derivative of surface (Slopes)
    duydx=(np.roll(uy,-1)-np.roll(uy,+1))/(2*dx)
    
    # Droplet Dynamics
    axp=k1*cp*(yp-uy[loc])*duydx[loc]/(m*(1+duydx[loc]**2)**(1))
    ayp=g-k1*cp*(yp-uy[loc])/(m*(1+duydx[loc]**2)**(1))
    xp=(xp+vxp*dt)%L # Periodic horizontal space
    vxp=vxp+axp*dt
    yp=yp+vyp*dt
    vyp=vyp*(1-0.001*cp)+ayp*dt
    
    # Surface Dynamics
    d2uydt2=gamma*(1+a*np.cos(omega_f*t))*(np.roll(uy,1)+np.roll(uy,-1)-2*uy)/2 -beta*uy**3
    d2uydt2[loc]+=-m*(ayp-g)/ms
    duydt=duydt*(1-damping*dt)+d2uydt2*dt
    uy=uy+duydt*dt
    uy[0]=0 # Fixed Boundaries
    uy[-1]=0
    
    # Data Collection
    xpp.append(xp)
    ypp.append(yp)
    z.append(uy[loc])
    slopes.append(duydx[loc])
    
    if i%500==0 and t>100:   
        surface=ax.plot(np.arange(0,L,L/N)+ux,100*uy,'-b')
        #surface=ax.plot(100*uy,'-b')
        #ax.plot(xpp,ypp,'r', label='Particle Trajectory')
        particle=ax.plot(xp,yp,'ro')
        #ax.set(ylim=(-0.1, 0.1))
        ax.legend(surface,['Surface Profile'])
        # ax.set_ylabel('Verticle Height', fontsize=15)
        # ax.set_xlabel('Dish Length', fontsize=15)
        #ax.legend()
        #ax.show()
        camera.snap()


""" MAIN LOOP END """

# VIDEO OUTPUT

animation = camera.animate()
animation.save('D:/a'+str(a)+'.mp4',fps=20)


# OTHER OUTPUT METHODS

# plt.ylabel("Vertical Displacement")
# plt.xlabel("Time")
# plt.title("Particle and Surface comparison Time 500 Beta 0")
# plt.plot(ypp[l//4:l//4+l//30]-1.5)
# plt.plot(5000*z[l//4:l//4+l//30])

# plt.ylabel("Surface Amplitude")
# plt.xlabel("Time")
# plt.title("Time 500 Beta 20")
# plt.plot(z)

# np.save('D:/xpp'+str(a),xpp)
# np.save('D:/ypp'+str(a),ypp)
# np.save('D:/z'+str(a),z)
# np.save('D:/slopes'+str(a),slopes)