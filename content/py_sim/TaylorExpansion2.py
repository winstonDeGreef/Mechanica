import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parameters
a = 1
c = 1
m = 1
v0 = 0.5  # initial velocity at x = -a

# Dimensionless velocity
V0 = np.sqrt(m * a / c) * v0

# Time settings
dtau = 0.002
kmax = 10000
tau = np.linspace(0, kmax * dtau, kmax)

# Harmonic approximation around x = -a
omega0 = np.sqrt(1 / 2)
B = V0 / omega0
x_harm = -1 + B * np.sin(omega0 * tau)

# Numerical solution (Heun's method)
x = np.zeros(kmax)
v = np.zeros(kmax)
x[0] = -1
v[0] = V0

for i in range(kmax - 1):
    F1 = (x[i]**2 - 1) / (x[i]**2 + 1)**2
    v_temp = v[i] + dtau * F1
    x_temp = x[i] + dtau * v[i]
    F2 = (x_temp**2 - 1) / (x_temp**2 + 1)**2
    v[i+1] = v[i] + 0.5 * dtau * (F1 + F2)
    x[i+1] = x[i] + 0.5 * dtau * (v[i] + v[i+1])

# Time in seconds
t_scaling = np.sqrt(m * a**3 / c)
t = tau * t_scaling

# Animation
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Left: Potential and particle motion
ax[0].set_xlim(-2, 2)
ax[0].set_ylim(-1, 1)
ax[0].set_title("Potential V(x) and Particle Position")
line_potential, = ax[0].plot([], [], 'r', label='V(x)')
point_num, = ax[0].plot([], [], 'ro', label='Numerical')
point_harm, = ax[0].plot([], [], 'go', label='Harmonic')
ax[0].legend()

X = np.linspace(-2, 2, 500)
V = X / (X**2 + 1)
line_potential.set_data(X, V)

# Right: x vs t
ax[1].set_xlim(0, t[-1])
ax[1].set_ylim(1.2 * np.min(x), 0.5 * np.max(x))
ax[1].set_title("x(t)")
line_num, = ax[1].plot([], [], 'r-', label='Numerical')
line_harm, = ax[1].plot([], [], 'g-', label='Harmonic')
ax[1].legend()
t_data, x_data, xh_data = [], [], []

def init():
    point_num.set_data([], [])
    point_harm.set_data([], [])
    line_num.set_data([], [])
    line_harm.set_data([], [])
    return point_num, point_harm, line_num, line_harm

def update(frame):
    xnum = x[frame]
    xh = x_harm[frame]
    Vnum = xnum / (xnum**2 + 1)
    Vharm = xh / (xh**2 + 1)

    point_num.set_data([xnum], [Vnum])
    point_harm.set_data([xh], [Vharm])

    t_data.append(t[frame])
    x_data.append(xnum)
    xh_data.append(xh)

    line_num.set_data(t_data, x_data)
    line_harm.set_data(t_data, xh_data)
    return point_num, point_harm, line_num, line_harm


ani = FuncAnimation(fig, update, frames=range(0, kmax, 20), init_func=init,
                    interval=20, blit=True)


HTML(ani.to_jshtml())
