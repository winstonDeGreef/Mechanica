#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 21:18:58 2024

@author: rmudde
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp


def mijnsys(t,XYWZ):
    m = 1.0
    k= 0.1
    momI = 1
    delta = 0.1
    epsilon = 0.01
    v=XYWZ[0]
    z=XYWZ[1]
    omega=XYWZ[2]
    theta=XYWZ[3]
    dvdt = -k/m*z -epsilon/m*theta
    dzdt = v
    domegadt = -delta/momI*theta - epsilon/momI*z
    dthetadt = omega
    return [dvdt, dzdt, domegadt, dthetadt]
    
t_begin=0.
t_end=4000.
t_nsamples=6000
t_space = np.linspace(t_begin, t_end, t_nsamples)
z_init = 1.0
v_init = 0.0
theta_init = 0.0
omega_init = 0.0


method = 'RK45' #available methods: 'RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA'
num_sol = solve_ivp(mijnsys, [t_begin, t_end], [v_init, z_init, omega_init, theta_init], method=method, dense_output=True)
XY_num_sol = num_sol.sol(t_space)
v_num_sol = XY_num_sol[0].T
z_num_sol = XY_num_sol[1].T
omega_num_sol = XY_num_sol[2].T
theta_num_sol = XY_num_sol[3].T

fig, ax = plt.subplots(2,1, figsize = (10,10))
z_fig, theta_fig = ax

z_fig.plot(t_space, z_num_sol,'-r', linewidth=1, label='z(t)')
z_fig.legend(loc = "upper right")
z_fig.grid()

theta_fig.plot(t_space, theta_num_sol, linewidth=1, label='$\\theta$(t)')
theta_fig.legend(loc = "upper right")
theta_fig.grid()
theta_fig.set_xlabel('t')
plt.savefig('WilberforceHigherOrder.png', dpi=300,bbox_inches='tight')
plt.show()



"""
# z(t), theta(t) animation
fig, ax = plt.subplots(2,1, figsize = (10,10))
z_fig, theta_fig = ax

z_fig.plot(t_space, z_num_sol,'-r', linewidth=1, label='z(t)')
z_fig.legend(loc = "upper right")
z_fig.grid()

theta_fig.plot(t_space, theta_num_sol, linewidth=1, label='$\\theta$(t)')
theta_fig.legend(loc = "upper right")
theta_fig.grid()
theta_fig.set_xlabel('t')
def update(frame):
    ax[0].clear()
    ax[1].clear()
    z_fig.plot(t_space, z_num_sol,'-r', linewidth=1, label='z(t)')
    z_fig.plot(t_space[frame], z_num_sol[frame],'ok',)
    theta_fig.plot(t_space, theta_num_sol,'-b', linewidth=1, label='$\\theta$(t)')
    theta_fig.plot(t_space[frame], theta_num_sol[frame],'ok')
    ax[1].set_xlabel('time', fontsize=16)
    ax[1].set_ylabel('$\\theta$', fontsize=16)
    ax[0].set_ylabel('z', fontsize=16)
    print(frame)
    return fig, ax

#ani = FuncAnimation(fig, update, frames=range(400))
#ani.save("Wilberforce_animation.gif", fps=10)


# z-theta phase plot animation
fig, ax = plt.subplots(figsize=(6, 6), dpi=120)
ax.set_xlabel('z')
ax.set_label('theta')          

def update(frame):
    ax.clear()
    ax.plot(z_num_sol, theta_num_sol,'-r')
    ax.plot(z_num_sol[frame+2], theta_num_sol[frame+2],'k',marker='.',markersize=10)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlabel('z', fontsize=20)
    ax.set_ylabel('theta',  fontsize=20)  
    return fig, ax

#ani = FuncAnimation(fig, update, frames=range(199))
#ani.save("WilberfocePhasePlot_animation.gif", fps=10)




"""








