#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:23:58 2025

@author: rmudde
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:44:32 2025

@author: rmudde
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N=199

c=1
V=3/5   #velocity S'
gamma = 1/np.sqrt(1-V*V)
U=4/5   #velocity m according to S

ct = np.linspace(-0.15,1,N)
xs = V*ct
xm = U*ct

# snijpunten van xm(t) baan met x' en ct' assen volgens S
#t' as
ct_tijd_comp = gamma*gamma*(1-V*U)*ct
x_tijd_comp = V*ct_tijd_comp
#x' as
ct_x_comp = gamma*gamma *V*(U-V)*ct
x_x_comp = gamma*gamma*(U-V)*ct

########################################
# maak figuren
########################################
fig, ax = plt.subplots(1,1,figsize=(8,8))
ax.set_xlim(-0.2,1)
ax.set_ylim(-0.2,1)
ax.plot((-1,1),(0,0),'k-')
ax.plot((0,0),(-1,1),'k-')
ax.grid()
ax.text(0.9,-0.07,'x', fontsize = 24)
ax.text(-0.1,0.9,'ct', fontsize = 24)
ax.plot((-1,1),(-1,1),'r--')
#ax.plot((-1,1),(1,-1),'r--')
ax.plot((-1,1),(-1/V,1/V),'b-')
ax.plot((-1/V,1/V),(-1,1),'b-')
ax.text(0.9,0.45,'x`',color='b', fontsize = 24)
ax.text(0.45,0.9,'ct`',color='b', fontsize = 24)
ax.plot((-1,1),(-1/U,1/U),'m-',linewidth=2)
ax.plot((1/5*gamma*V,1),(1/5*gamma, 1/5*gamma+V*(1-1/5*gamma*V)),'g--')
ax.plot((2/5*gamma*V,1),(2/5*gamma, 2/5*gamma+V*(1-2/5*gamma*V)),'g--')
ax.plot((3/5*gamma*V,1),(3/5*gamma, 3/5*gamma+V*(1-3/5*gamma*V)),'g--')
ax.plot((1/5*gamma,1/5*gamma+V*(1-1/5*gamma*V)),(1/5*gamma*V,1),'g--')
ax.plot((2/5*gamma,2/5*gamma+V*(1-2/5*gamma*V)),(2/5*gamma*V,1),'g--')
ax.plot((3/5*gamma,3/5*gamma+V*(1-3/5*gamma*V)),(3/5*gamma*V,1),'g--')
ax.text(0.22,0.09,'0.2',color='g', fontsize=20)
ax.text(0.47,0.24,'0.4',color='g', fontsize=20)
ax.text(0.72,0.39,'0.6',color='g', fontsize=20)
ax.text(0.06,0.25,'0.2',color='g', fontsize=20)
ax.text(0.205,0.49,'0.4',color='g', fontsize=20)
ax.text(0.35,0.74,'0.6',color='g', fontsize=20)


def update(frame):
    ax.clear()
    ax.set_xlim(-0.2,1)
    ax.set_ylim(-0.2,1)
    ax.plot((-1,1),(0,0),'k-')
    ax.plot((0,0),(-1,1),'k-')
    ax.grid()
    ax.text(0.9,-0.07,'x', fontsize = 24)
    ax.text(-0.1,0.9,'ct', fontsize = 24)
    ax.plot((-1,1),(-1,1),'r--')
    #ax.plot((-1,1),(1,-1),'r--')
    ax.plot((-1,1),(-1/V,1/V),'b-')
    ax.plot((-1/V,1/V),(-1,1),'b-')      
    ax.text(0.9,0.45,'x`',color='b', fontsize = 24)
    ax.text(0.45,0.9,'ct`',color='b', fontsize = 24)
    ax.plot((-1,1),(-1/U,1/U),'m-',linewidth=2)
    
    ax.plot((1/5*gamma*V,1),(1/5*gamma, 1/5*gamma+V*(1-1/5*gamma*V)),'g--')
    ax.plot((2/5*gamma*V,1),(2/5*gamma, 2/5*gamma+V*(1-2/5*gamma*V)),'g--')
    ax.plot((3/5*gamma*V,1),(3/5*gamma, 3/5*gamma+V*(1-3/5*gamma*V)),'g--')
    ax.plot((1/5*gamma,1/5*gamma+V*(1-1/5*gamma*V)),(1/5*gamma*V,1),'g--')
    ax.plot((2/5*gamma,2/5*gamma+V*(1-2/5*gamma*V)),(2/5*gamma*V,1),'g--')
    ax.plot((3/5*gamma,3/5*gamma+V*(1-3/5*gamma*V)),(3/5*gamma*V,1),'g--')
    ax.text(0.22,0.09,'0.2',color='g', fontsize=20)
    ax.text(0.47,0.24,'0.4',color='g', fontsize=20)
    ax.text(0.72,0.39,'0.6',color='g', fontsize=20)
    ax.text(0.06,0.25,'0.2',color='g', fontsize=20)
    ax.text(0.205,0.49,'0.4',color='g', fontsize=20)
    ax.text(0.35,0.74,'0.6',color='g', fontsize=20)
    ax.plot(xs[frame],ct[frame],'bo')
    ax.plot(xm[frame],ct[frame],'mo')
    ax.plot((x_tijd_comp[frame],xm[frame]),(ct_tijd_comp[frame],ct[frame]),'m--',linewidth=2)
    ax.plot((x_x_comp[frame],xm[frame]),(ct_x_comp[frame],ct[frame]),'m--',linewidth=2)
    ax.plot((0,xm[frame]),(ct[frame],ct[frame]),'k--',linewidth=2)
    ax.plot((xm[frame],xm[frame]),(0,ct[frame]),'k--',linewidth=2)
    
    return fig, ax

ani = FuncAnimation(fig, update, frames=range(N))
ani.save("MinkowskiMovingParticle_animation.gif", fps=15)