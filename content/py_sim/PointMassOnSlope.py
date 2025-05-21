import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parameters
alpha_deg = float(input('alpha (degrees) from 0 to 45'))       # angle of the slope in degrees
mu = float(input('mu (-) from 0 to 1'))            # friction coefficient
g = 981              # gravity in cm/s²
t_stop = 1           # seconds
dt = 0.01            # time step in seconds

# Convert to radians
alpha = np.radians(alpha_deg)

# Effective acceleration with and without friction
geff = g * (np.sin(alpha) - mu * np.cos(alpha)) if np.sin(alpha) > mu * np.cos(alpha) else 0
gnofric = g * np.sin(alpha)

# Time array
t = np.arange(0, t_stop, dt)

# Position and velocity arrays
x_fric = 0.5 * geff * np.cos(alpha) * t**2
y_fric = -0.5 * geff * np.sin(alpha) * t**2
v_fric = geff * t

x_nofric = 0.5 * gnofric * np.cos(alpha) * t**2
y_nofric = -0.5 * gnofric * np.sin(alpha) * t**2
v_nofric = gnofric * t

# Setup figure and axes
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
plt.subplots_adjust(wspace=0.4)

# Left plot: slope animation
ax1.set_xlim(50, 400)
ax1.set_ylim(50, 350)
ax1.set_aspect('equal')
ax1.set_title("Masses Sliding on a Slope")

# Middle plot: x-position over time
ax2.set_xlim(0, t_stop)
ax2.set_ylim(0, max(max(x_nofric), max(x_fric)) * 1.2)
ax2.set_title("x-position over time")
line1, = ax2.plot([], [], 'r-', label='x (no friction)')
line2, = ax2.plot([], [], 'b-', label='x (friction)')
ax2.legend()
ax2.set_xticklabels([])
ax2.set_yticklabels([])

# Right plot: velocity over time
ax3.set_xlim(0, t_stop)
ax3.set_ylim(0, max(max(v_nofric), max(v_fric)) * 1.2)
ax3.set_title("Velocity over time")
line3, = ax3.plot([], [], 'r--', label='v (no friction)')
line4, = ax3.plot([], [], 'b--', label='v (friction)')
ax3.legend()
ax3.set_xticklabels([])
ax3.set_yticklabels([])

# Sloped surface
x0, y0 = 100, 300
dx = 250
dy = -dx * np.tan(alpha)
ax1.plot([x0, x0 + dx], [y0, y0 + dy], 'k')
ax1.plot([x0, x0 + dx], [y0 + dy, y0 + dy], 'k')

# Mass markers
mass_nofric, = ax1.plot([], [], 'ro', label='No friction')
mass_fric, = ax1.plot([], [], 'bo', label='With friction')
ax1.legend()
ax1.set_xticklabels([])
ax1.set_yticklabels([])
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    mass_nofric.set_data([], [])
    mass_fric.set_data([], [])
    return line1, line2, line3, line4, mass_nofric, mass_fric

def update(i):
    if i == 0:
        i = 1  # avoid empty slice

    i = min(i, len(t) - 1)

    # Update x-position lines
    line1.set_data(t[:i], x_nofric[:i])
    line2.set_data(t[:i], x_fric[:i])

    # Update velocity lines
    line3.set_data(t[:i], v_nofric[:i])
    line4.set_data(t[:i], v_fric[:i])

    # Update positions on slope (single points in lists)
    mass_nofric.set_data([x0 + x_nofric[i]], [y0 + y_nofric[i]])
    mass_fric.set_data([x0 + x_fric[i]], [y0 + y_fric[i]])

    return line1, line2, line3, line4, mass_nofric, mass_fric

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)
HTML(ani.to_jshtml())