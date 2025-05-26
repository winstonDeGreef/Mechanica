#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:13:59 2024

@author: rmudde
"""
import matplotlib.pyplot as plt
import numpy as np

N = 2000000
dt = 0.001

z = np.zeros(N)
v = np.zeros(N)
theta = np.zeros(N)
omega = np.zeros(N)
t = np.zeros(N)

m = 1.0
I = 1.0
k = 2.0
delta = 2.0
epsilon = 0.1

z[0] = 1.0
v[0] = 0.0
theta[0] = 0.0
omega[0] = 0.0
t[0] = 0.0

for i in range(1,N):
    v[i] = v[i-1] - k/m*z[i-1]*dt - epsilon / m * theta[i-1] *dt
    z[i] = z[i-1] + 0.5*(v[i] + v[i-1]) * dt
    omega[i] = omega[i-1] - delta/I * theta[i-1] * dt - epsilon / I * z[i-1] *dt
    theta[i] = theta[i-1] + 0.5*( omega[i] + omega[i-1]) * dt
    t[i] = i*dt


plt.figure()
plt.plot(t,z,'-r',label='z(t)')
plt.plot( t, theta,'-b',label='$\\theta$(t)')
plt.xlabel('t')
plt.legend(loc='upper left')
plt.savefig('WilberorceEuler.png', dpi=300,bbox_inches='tight')