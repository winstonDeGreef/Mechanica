#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:35:53 2024
fox-rabbit prey-preditor system
dr/dt = lamda_r r - mu_r *r*f
df/dt = -lambda_f + mu_f *r*f

@author: rmudde
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

#parameters
lambda_r = 0.1
mu_r = 0.03
lambda_f = 0.1
mu_f = 0.01

# Set initial conditions
Pop0 = [80, 2]
    
def Diffs(Pop,t):
    # Extract variables
    rabbit = Pop[0]
    fox = Pop[1]

    # Define equations of Lotka-Volterra model
    dPopdt = [lambda_r * rabbit - mu_r * rabbit * fox,
            -lambda_f * fox + mu_f * rabbit * fox ]
    return dPopdt

# Set the time grid
t = np.linspace(0, 360, 500)

# Solve the ODE system
sol = odeint(Diffs, Pop0, t)

# Extract the solution variables for plotting
rabbit = sol[:, 0]  # extract the first variable
fox = sol[:, 1]  # extract the second variable

# Plot the solution
plt.plot(t, rabbit, label='rabbit')
plt.plot(t, fox, label='fox')
plt.xlabel('Time')
plt.ylabel('Number')
plt.legend(loc='upper right')
# Set the maximum y-value on the plot
plt.ylim(0, np.max(rabbit) + 10)
plt.grid(True)

plt.figure()
plt.plot(rabbit,fox,'-k')


#===================
#oplossing met RK45

def Mysys(t,RF):
    lambda_r = 0.2
    mu_r = 0.03
    lambda_f = 0.1
    mu_f = 0.01
    r = RF[0]
    f = RF[1]
    drdt = lambda_r * r - mu_r * r * f
    dfdt = -lambda_f * f + mu_f * r * f
    return [drdt, dfdt]

t_begin=0.
t_end=200.
t_nsamples=1000
t_space = np.linspace(t_begin, t_end, t_nsamples)
r_init = 80
f_init = 2

method = 'RK45' #available methods: 'RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA'
num_sol = solve_ivp(Mysys, [t_begin, t_end], [r_init, f_init], method=method, dense_output=True)
RF_num_sol = num_sol.sol(t_space)
r_num_sol = RF_num_sol[0].T
f_num_sol = RF_num_sol[1].T


plt.figure()
plt.plot(r_num_sol, f_num_sol,'-g')
plt.show()
plt.figure()
plt.plot(t_space,r_num_sol,'-b',t_space,f_num_sol,'-r')
plt.xlabel('time',size=18)
plt.ylabel('population',size=18)
plt.legend(['rabbits', 'foxes'], loc="upper right")
plt.savefig('RabbitsAndFoxes.png', dpi=300,bbox_inches='tight')


# animation
fig, ax = plt.subplots(figsize=(6, 6), dpi=120)
ax.set_xlabel('# rabbits')
ax.set_label('# foxes')          
x=r_num_sol
y=f_num_sol
def update(frame):
    ax.clear()
    plt.plot(r_num_sol, f_num_sol,'-b', linewidth=1)
    ax.plot(x[frame:frame+3], y[frame:frame+3],'-r')
    ax.plot(x[frame+2], y[frame+2],'r',marker='.',markersize=16)
    ax.set_xlim(-10, 100)
    ax.set_ylim(-1, 40)
    ax.set_xlabel('# rabbits', fontsize=20)
    ax.set_ylabel('# foxes',  fontsize=20)  
    return fig, ax

ani = FuncAnimation(fig, update, frames=range(399))
#ani.save("rf_animation.gif", fps=10)







