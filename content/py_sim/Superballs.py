#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:24:04 2024

animation of superballs
@author: rmudde
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N=300
t_end = 20
dt = t_end/N
t = np.linspace(0,t_end,N)

bardikte = 0.01
barx = [-0.1, 0.1]
barz = [ -bardikte, -bardikte ]

Dbig = 100
Dmedium = 50
Dsmall = 20
vbig = -1
vmedium = vbig
vsmall = vbig
z0= 10

scaling = 50/1.555

x = np.linspace(0,0,N)
zb = np.linspace(z0 + Dbig/2/scaling , z0 + Dbig/2/scaling , N)
zm = np.linspace(z0 + (Dbig + Dmedium/2)/scaling, z0 + (Dbig + Dmedium/2)/scaling,N)
zs = np.linspace(z0 + (Dbig + Dmedium + Dsmall/2)/scaling, z0 + (Dbig + Dmedium + Dsmall/2)/scaling,N)

bardikte = 12/2/scaling
barx = [-0.1, 0.1]
barz = [ -bardikte, -bardikte ]



for i in range(1,N):
    zb[i] = zb[i-1] + vbig*dt
    zm[i] = zm[i-1] + vmedium*dt
    zs[i] = zs[i-1] + vsmall*dt
    if zb[i] - Dbig/2/scaling <0:
        vbig = -vbig
        vmedium = -3*vmedium
        vsmall = -7*vsmall
        print('joepie, i= ',i)
    

fig, ax = plt.subplots(1,1, figsize = (10,10))
plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 
ax.set_ylim(-0.45, 16)
ax.plot(x[0],zb[0],'ob', markersize=100)
ax.plot(x[0],zm[0],'og', markersize=50)
ax.plot(x[0],zs[0],'or', markersize=20)
ax.plot(barx, barz,'-k', linewidth=12)

def update(frame):
    ax.clear()
    plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 
    ax.set_ylim(-0.45, 16)
    ax.plot(x[frame],zb[frame],'ob', markersize=100)
    ax.plot(x[frame],zm[frame],'og', markersize=50)
    ax.plot(x[frame],zs[frame],'or', markersize=20)
    ax.plot(barx, barz,'-k', linewidth=12)
    return fig, ax

ani = FuncAnimation(fig, update, frames=range(1,N))
ani.save("Superball_animation.gif", fps=30)

plt.figure()
plt.plot(t,zb)