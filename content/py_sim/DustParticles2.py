#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 11:13:07 2025
center of mass for N dust particles
@author: rmudde
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 3000         # number of particles
m = 0.002       # mass of each particle in kg (2 g)
Mtot = N * m       # total mass
Mmedium = N/10*m
Msmall = N/100*m
dt = 0.06       # time step
Ntimes = 1000    # number of updates
tijd=np.linspace(0,Ntimes*dt,Ntimes)

# box 
L = 50

# Generate random speeds and directions
np.random.seed(0)                               # for reproducibility
speeds = np.random.uniform(1, 5, N)             # speed between 0 and 5 m/s
angles = np.random.uniform(0, 2 * np.pi, N)     # direction in radians

# Compute velocity components
vx = speeds * np.cos(angles)
vy = speeds * np.sin(angles)


# Total momentum
def CMtot():
    total_px = np.sum(m * vx)
    # Center of mass velocity
    vx_tot = total_px / Mtot
    
    medium_px = np.sum(m * vx[0:int(N/10)])
    # Center of mass velocity
    vx_medium = medium_px / Mtot
    
    small_px = np.sum(m * vx[0:int(N/100)])
    # Center of mass velocity
    vx_small = small_px / Mtot
    
    return vx_tot, vx_medium, vx_small

vx_tot, vx_medium, vx_small = CMtot()

# Center of mass position after t seconds
t = 10  # seconds
x_tot = vx_tot * t
x_medium = vx_medium * t
x_small = vx_small * t

# Particle positions after 10 seconds
x_positions = vx * t
y_positions = vy * t

def UpdatePositions(x_positions,y_positions):
    x_new = x_positions + vx*dt
    y_new = y_positions + vy*dt
    for i in range(N):
        if x_new[i]> L:
            x_new[i] = L-(x_new[i]-x_positions[i])
            vx[i] = -vx[i]
        if x_new[i] < -L:
            x_new[i] = -L+(x_new[i]-x_positions[i])
            vx[i] = -vx[i]
        if y_new[i]> L:
            y_new[i] = L-(y_new[i]-y_positions[i])
            vy[i] = -vy[i]
        if y_new[i] < -L:
            y_new[i] = -L+(y_new[i]-y_positions[i])
            vy[i] = -vy[i]
    return x_new, y_new, vx, vy


Rtot_x = np.linspace(0,0,Ntimes)
Rtot_x[0] = x_tot
Rmedium_x = np.linspace(0,0,Ntimes)
Rmedium_x[0] = x_medium
Rsmall_x = np.linspace(0,0,Ntimes)
Rsmall_x[0] = x_small



for i in range(1,Ntimes):
    if i % 100 == 0:
        print(i)
    x_positions,y_positions,vx,vy = UpdatePositions(x_positions,y_positions)
    vx_tot, vx_medium, vx_small = CMtot()

    Rtot_x[i] = Rtot_x[i-1]+ vx_tot*dt
    Rmedium_x[i] = Rmedium_x[i-1]+ vx_medium*dt
    Rsmall_x[i] = Rsmall_x[i-1]+ vx_small*dt


# Plot
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(tijd,Rtot_x,'r-',label='N=3000')
ax.plot(tijd,Rmedium_x,'b-',label='N=300')
ax.plot(tijd,Rsmall_x,'k-',label='N=30')
ax.set_title('x-position center of mass',fontsize=24)
ax.set_ylabel('x position (m)',fontsize=24)
ax.set_xlabel('time (s)',fontsize=24)
ax.legend(loc="upper left",fontsize=24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)