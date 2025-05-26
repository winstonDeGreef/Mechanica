#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:07:55 2025

@author: rmudde
"""

import numpy as np
import matplotlib.pyplot as plt

c=1
V=3/5
gamma=1/np.sqrt(1-V*V)

ctp = [0,1,2,3,4,5]
xp = [0,0,1,1,0,0]
ct=[0,0,0,0,0,0]
x=[0,0,0,0,0,0]

phi = 15/180*np.pi

def invLT(ctp,xp):
    ct = gamma*(ctp+V*xp)
    x = gamma*(xp+V*ctp)
    return ct, x

for i in range(0,6):
    ct[i],x[i] = invLT(ctp[i],xp[i])


fig, (ax1, ax2) = plt.subplots(1,2,figsize=(18,8))
ax1.axis('square')
ax1.set_xlim(-1,7)
ax1.set_ylim(-1,7)
ax1.plot((-1,7),(0,0),'k-')
ax1.plot((0,0),(-1,7),'k-')
ax1.text(-0.8, 6, 'ct`', fontsize = 32, color = 'b')
ax1.text(6, -0.6, 'x`', fontsize = 32, color = 'b')
ax1.text(-0.8, 5, 'ct', fontsize = 32, color = 'r')
ax1.text(5, -0.6, 'x', fontsize = 32, color = 'r')
for i in range(0,5):
    ax1.plot((xp[i],xp[i+1]),(ctp[i],ctp[i+1]),'b-')
    ax1.plot((x[i],x[i+1]),(ct[i],ct[i+1]),'r-')

for i in range(0,6):
    ax1.plot(xp[i],ctp[i],'bo',ms=10)
    ax1.plot(x[i],ct[i],'ro',ms=10)

ax1.grid()

ax2.set_xlim(-1,7)
ax2.set_ylim(-1,7)
ax2.plot((-1,7),(0,0),'k-')
ax2.plot((0,0),(-1,7),'k-')
ax2.grid()
ax2.text(-0.7,5.5, 'ct', fontsize = 32)
ax2.text(5.5,-0.6,'x', fontsize = 32)
ax2.plot((-1,7),(-1,7),'r--')
ax2.plot((-1,6),(-1/V,6/V),'b-')
ax2.plot((-1/V,6/V),(-1,6),'b-')
ax2.text(2.6, 5.5, 'ct`', fontsize = 32, color = 'b')
ax2.text(5.5, 2.8, 'x`', fontsize = 32, color = 'b')
for i in range(0,5):
    ax2.plot((x[i],x[i+1]),(ct[i],ct[i+1]),'m-',linewidth=2)
for i in range(0,6):
    ax2.plot(x[i],ct[i],'mo',ms=10)

plt.savefig('MinkowskiEvents.png', dpi=300, format='png')