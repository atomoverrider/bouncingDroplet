
"""
Simulating a parameterically oscillated surface using 'pde' library. Determining instability for different parameters to plot a phase diagram.
"""
# IMPORT LIBRARIES

from pde import PDE, FieldCollection, PlotTracker, ScalarField, UnitGrid
import pde
import matplotlib.pyplot as plt
import numpy as np

# MAIN LOOP

def LOOP(number,A,o):
    a = A # Oscillation amplitude
    omega = o # Frequency
    n=number # No. of wavelengths to excite on the surface
    gamma = (omega*500/(2*np.pi*n))**2 # Calculated tension of surface
    d = 0.05 # Damping Constant
    eq = PDE( # Equation initialisation
        {
            "v": f"{gamma} *(1+{a}*cos({omega}*t))* laplace(u) - {d}*v",
            "u": f"v",
        }
    )
    
    # INITIALISE STATE
    grid = UnitGrid([1, 500])
    v = ScalarField(grid, 0, label="Field $v$")
    u = 0.1 * ScalarField.random_normal(grid, label="Field $u$")
    state = FieldCollection([v, u])
    storage = pde.MemoryStorage()
    
    # SOLVE
    sol = eq.solve(state, t_range=200, dt=1e-3, tracker=["progress", storage.tracker(1)])
    
    # DATA COLLECTION
    x=np.zeros(0)
    for time, u in storage.items():
        z=u.data[0][0]
        x=np.append(x,z[250])
    s=int(len(x)*0.4)
        
    # DETERMINE WHETHER SIMULATION IS STABLE OR UNSTABLE
    # Comparing max amplitude of two sub ranges in the collected data
    if max(x[int(len(x)*0.8)::])>max(x[s:int(len(x)*0.6)]):
        return 1
    else:
        return 0


# Looping through values of 'a' and 'n' to produce a phase diagram
p,q=50,50
base=10
matLinear=np.ones([p-base,q])

n10=(500/(2*np.pi*10))**2
n50=(500/(2*np.pi*50))**2

for i in range(base,p):
    for j in range(q):
        l=LOOP(i,j/q+0.,1)
        matLinear[i-base,j]=l
        if l==1:
            break
    print(i)
