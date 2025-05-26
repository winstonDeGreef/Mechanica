#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:44:32 2025

@author: rmudde
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

M=45
N=2*M
c=1
V=[]
for i in range(0,M+1):
    velo = 0.02*i +0.000000001
    V.append(velo)
for i in range(1,M):
    V.append(V[M-i])

phi = 15/180*np.pi

########################################
# maak figuren
########################################
fig, ax = plt.subplots(1,1,figsize=(8,8))
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.plot((-1,1),(0,0),'k-')
ax.plot((0,0),(-1,1),'k-')
ax.grid()
ax.text(0.8*np.sin(-phi), 0.8*np.cos(-phi), 'ct', fontsize = 24)
ax.text(0.8*np.cos(-phi), 0.8*np.sin(-phi),'x', fontsize = 24)
ax.plot((-1,1),(-1,1),'k--')
ax.plot((-1,1),(1,-1),'k--')
ax.plot((-1,1),(-1/V[0],1/V[0]),'b-')
ax.plot((-1/V[0],1/V[0]),(-1,1),'b-')
ax.text(0.8*np.sin(V[0]-phi), 0.8*np.cos(V[0]*45*np.pi/180-phi), 'ct`', fontsize = 24, color = 'b')
ax.text(0.8*np.cos(V[0]-phi), 0.8*np.sin(V[0]*45*np.pi/180-phi), 'x`', fontsize = 24, color = 'b')
ax.text(-0.5,0.9,'V/c=',fontsize = 20)
ax.text(-0.25,0.9,"%.2f" % round(np.abs(V[0]), 2),fontsize = 20)

gamma=1/np.sqrt(1-V[0]*V[0])
ax.plot((1/4*gamma*V[0],1),(1/4*gamma,1/4/gamma + V[0]),'g-')
ax.plot((2/4*gamma*V[0],1),(2/4*gamma,2/4/gamma + V[0]),'g-')
ax.plot((3/4*gamma*V[0],1),(3/4*gamma,3/4/gamma + V[0]),'g-')
ax.plot((1/4*gamma,1/4*gamma+gamma*V[0]),(1/4*gamma*V[0],gamma+1/4*gamma*V[0]),'r-')
ax.plot((2/4*gamma,2/4*gamma+gamma*V[0]),(2/4*gamma*V[0],gamma+2/4*gamma*V[0]),'r-')
ax.plot((3/4*gamma,3/4*gamma+gamma*V[0]),(3/4*gamma*V[0],gamma+3/4*gamma*V[0]),'r-')

def update(frame):
    ax.clear()
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.plot((-1,1),(0,0),'k-')
    ax.plot((0,0),(-1,1),'k-')
    ax.grid()
    ax.text(0.8*np.sin(-phi), 0.8*np.cos(-phi), 'ct', fontsize = 24)
    ax.text(0.8*np.cos(-phi), 0.8*np.sin(-phi),'x', fontsize = 24)
    ax.plot((-1,1),(-1,1),'k--')
    ax.plot((-1,1),(1,-1),'k--')
    ax.plot((-1,1),(-1/V[frame],1/V[frame]),'b-')
    ax.plot((-1/V[frame],1/V[frame]),(-1,1),'b-')
    ax.text(0.8*np.sin(V[frame]-phi), 0.8*np.cos(V[frame]-phi), 'ct`', fontsize = 24, color = 'b')
    ax.text(0.8*np.cos(V[frame]-phi), 0.8*np.sin(V[frame]-phi), 'x`', fontsize = 24, color = 'b')
    ax.text(-0.5,0.9,'V/c=',fontsize = 20)
    ax.text(-0.25,0.9,"%.2f" % round(np.abs(V[frame]), 2),fontsize = 20)
    
    gamma=1/np.sqrt(1-V[frame]*V[frame])
    ax.plot((1/4*gamma*V[frame],1),(1/4*gamma,1/4/gamma + V[frame]),'g-')
    ax.plot((2/4*gamma*V[frame],1),(2/4*gamma,2/4/gamma + V[frame]),'g-')
    ax.plot((3/4*gamma*V[frame],1),(3/4*gamma,3/4/gamma + V[frame]),'g-')
    ax.plot((1/4*gamma,1/4*gamma+gamma*V[frame]),(1/4*gamma*V[frame],gamma+1/4*gamma*V[frame]),'r-')
    ax.plot((2/4*gamma,2/4*gamma+gamma*V[frame]),(2/4*gamma*V[frame],gamma+2/4*gamma*V[frame]),'r-')
    ax.plot((3/4*gamma,3/4*gamma+gamma*V[frame]),(3/4*gamma*V[frame],gamma+3/4*gamma*V[frame]),'r-')
    
    return fig, ax

ani = FuncAnimation(fig, update, frames=range(N))
ani.save("Minkowski2_animation.gif", fps=5)