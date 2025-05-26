#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:03:59 2024
poging om aarde om zon te simuleren
@author: rmudde
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

L = 1e-6
C = 1e-6


def diffvgl(t,Pos):
    I = Pos[0]
    V = Pos[1]
    L = 1e-6
    C = 1e-6
    dIdt = V/L
    dVdt = - I/C
    return [ dIdt, dVdt ]

t_begin=0.
t_end=2*2*np.pi * np.sqrt(L*C)
t_nsamples=100
t_space = np.linspace(t_begin, t_end, t_nsamples)

I_0 = 0.0
V_0 = 5.0


method = 'RK45' #available methods: 'RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA'
num_sol = solve_ivp(diffvgl, [t_begin, t_end], [I_0, V_0], method=method, dense_output=True)
XY_num_sol = num_sol.sol(t_space)
I_num_sol = XY_num_sol[0].T
V_num_sol = XY_num_sol[1].T


fig, ax = plt.subplots(2,1, figsize = (10,10))
I_fig, V_fig = ax

I_fig.plot(t_space, I_num_sol,'-r', linewidth=1, label='I(t)')
I_fig.legend(loc = "upper right")
I_fig.grid()

V_fig.plot(t_space, V_num_sol, linewidth=1, label='$V_L$(t)')
V_fig.legend(loc = "upper right")
V_fig.grid()
V_fig.set_xlabel('t')
#plt.savefig('LCsolution.png', dpi=300,bbox_inches='tight')
plt.show()

#############################################################
# I(t), V_L(t) animation
fig, ax = plt.subplots(2,1, figsize = (10,10))
I_fig, V_fig = ax

I_fig.plot(t_space, I_num_sol,'-r', linewidth=2, label='z(t)')
I_fig.legend(loc = "upper right")
I_fig.grid()

V_fig.plot(t_space, V_num_sol, linewidth=2, label='$V_C$(t)')
V_fig.legend(loc = "upper right")
V_fig.grid()
V_fig.set_xlabel('t')
def update(frame):
    ax[0].clear()
    ax[1].clear()
    I_fig.plot(t_space, I_num_sol,'-r', linewidth=2, label='z(t)')
    I_fig.plot(t_space[frame], I_num_sol[frame],'ok',)
    I_fig.grid()
    ax[0].set_xticklabels([-0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2],fontsize=21)
    ax[0].set_yticklabels([-6, -4, -2, 0, 2, 4],fontsize=21)
    V_fig.plot(t_space, V_num_sol,'-b', linewidth=2, label='$V_L$(t)')
    V_fig.plot(t_space[frame], V_num_sol[frame],'.', markerfacecolor = 'k', ms = 16)
    V_fig.grid()
    plt.xticks(fontsize=21)
    plt.yticks(fontsize=21)
    ax[1].set_xlabel('time', fontsize=24)
    ax[1].set_ylabel('$V_L$', fontsize=24)
    ax[0].set_ylabel('I', fontsize=24)
    if np.mod(frame,10) == 0:
        print(frame)
    return fig, ax

ani = FuncAnimation(fig, update, frames=range(t_nsamples))
ani.save("LC_animation.gif", fps=20)