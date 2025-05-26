#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:03:58 2025

@author: rmudde
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 08:57:27 2025

@author: rmudde
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N=21
M=100
Vsound = 1
Vcar = 0.6

########################################
# maak cirkels
########################################
phi = np.linspace(0,2*np.pi,M)
t = np.linspace(0,1,N)
R = Vsound*t
R2 = 0*t
for j in range(3,N):
    R2[j]=R[j-3]
R3 = 0*t
for j in range(6,N):
    R3[j]=R[j-6]
R4 = 0*t
for j in range(9,N):
    R4[j]=R[j-9]
R5 = 0*t
for j in range(12,N):
    R5[j]=R[j-12]
R6 = 0*t
for j in range(15,N):
    R6[j]=R[j-15]
R7 = 0*t
for j in range(18,N):
    R7[j]=R[j-18]    
Xmax = np.max(R)

########################################
# maak figuren
########################################
fig, [ax1,ax2] = plt.subplots(1,2,figsize=(18,8))
ax1.set_xlim(-1.05*Xmax,1.05*Xmax)
ax1.set_ylim(-1.05*Xmax,1.05*Xmax)
ax1.plot(0,0,'b.',markersize=15)
ax1.plot(R[0]*np.cos(phi),R[0]*np.sin(phi),'r-')
# disabling xticks by Setting xticks to an empty list
ax1.set_xticks([])   
# disabling yticks by setting yticks to an empty list
ax1.set_yticks([]) 

ax2.set_xlim(-Xmax,Xmax)
ax2.set_ylim(-Xmax,Xmax)
ax2.plot(0,0,'b.',markersize=15)
ax2.plot(R[0]*np.cos(phi),R[0]*np.sin(phi),'r-')
# disabling xticks by Setting xticks to an empty list
ax2.set_xticks([])   
# disabling yticks by setting yticks to an empty list
ax2.set_yticks([]) 

def update(frame):
    ax1.clear()
    ax1.set_xlim(-1.05*Xmax,1.05*Xmax)
    ax1.set_ylim(-1.05*Xmax,1.05*Xmax)
    ax1.plot(0,0,'b.',markersize=15)
    ax1.plot(R[frame]*np.cos(phi),R[frame]*np.sin(phi),'r-')
    ax1.plot(R2[frame]*np.cos(phi),R2[frame]*np.sin(phi),'r-')
    ax1.plot(R3[frame]*np.cos(phi),R3[frame]*np.sin(phi),'r-')
    ax1.plot(R4[frame]*np.cos(phi),R4[frame]*np.sin(phi),'r-')
    ax1.plot(R5[frame]*np.cos(phi),R5[frame]*np.sin(phi),'r-')
    ax1.plot(R6[frame]*np.cos(phi),R6[frame]*np.sin(phi),'r-')
    ax1.plot(R7[frame]*np.cos(phi),R7[frame]*np.sin(phi),'r-')
    # disabling xticks by Setting xticks to an empty list
    ax1.set_xticks([])   
    # disabling yticks by setting yticks to an empty list
    ax1.set_yticks([]) 
    
    ax2.clear()
    ax2.set_xlim(-1.05*Xmax,1.05*Xmax)
    ax2.set_ylim(-1.05*Xmax,1.05*Xmax)
    ax2.plot(Vcar*t[frame],0,'b.',markersize=15)
    ax2.plot(R[frame]*np.cos(phi),R[frame]*np.sin(phi),'r-')
    ax2.plot(Vcar*t[3] + R2[frame]*np.cos(phi),R2[frame]*np.sin(phi),'r-')
    ax2.plot(Vcar*t[6] + R3[frame]*np.cos(phi),R3[frame]*np.sin(phi),'r-')
    ax2.plot(Vcar*t[9] + R4[frame]*np.cos(phi),R4[frame]*np.sin(phi),'r-')
    ax2.plot(Vcar*t[12] + R5[frame]*np.cos(phi),R5[frame]*np.sin(phi),'r-')
    ax2.plot(Vcar*t[15] + R6[frame]*np.cos(phi),R6[frame]*np.sin(phi),'r-')
    ax2.plot(Vcar*t[18] + R7[frame]*np.cos(phi),R7[frame]*np.sin(phi),'r-')
    # disabling xticks by Setting xticks to an empty list
    ax2.set_xticks([])   
    # disabling yticks by setting yticks to an empty list
    ax2.set_yticks([]) 
    
    return fig, ax1, ax2

ani = FuncAnimation(fig, update, frames=range(N))
ani.save("Doppler_animation.gif", fps=)