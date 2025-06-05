import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

# Parameters
g = 9.813  # m/s^2
mu = 0.1   # friction coefficient
m1 = 1.0   # hanging mass
M = 1.0    # default mass on table, can be 3.0 or 5.0
t_stop = 1.5
dt = 0.01
t_vals = np.arange(0, t_stop, dt)

# Compute acceleration
acc = (m1 - mu * M) * g / (m1 + M)
if acc < 0:
    raise ValueError("No motion, friction too high!")

# Positions over time
x1_vals = 40 + 50 * 0.5 * acc * t_vals**2  # red block on table (horizontal)
y2_vals = 210 + 50 * 0.5 * acc * t_vals**2 # grey block (vertical)

# Set up figure
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 900)
ax.set_ylim(500, 0)
ax.axis('off')

# Draw static elements
table_line, = ax.plot([20, 320], [180, 180], color='black')
pulley = plt.Circle((320, 180), 15, color='grey')
ax.add_patch(pulley)

# Red and grey masses
red_mass = plt.Rectangle((40, 150), 30, 30, color='red')
grey_mass = plt.Rectangle((320, 210), 30, 30, color='grey')
ax.add_patch(red_mass)
ax.add_patch(grey_mass)

# Cords
cord_red, = ax.plot([], [], color='black')
cord_grey, = ax.plot([], [], color='black')

# x-t graph
graph_ax = fig.add_axes([0.55, 0.15, 0.4, 0.3])
graph_ax.set_xlim(0, t_stop)
graph_ax.set_ylim(0, 4.2)
graph_ax.set_xlabel("$t$ (s)")
graph_ax.set_ylabel("$x$ (m)")
graph_line, = graph_ax.plot([], [], color='blue')

x_plot = []
t_plot = []

def init():
    red_mass.set_xy((40, 150))
    grey_mass.set_xy((320, 210))
    cord_red.set_data([], [])
    cord_grey.set_data([], [])
    graph_line.set_data([], [])
    return red_mass, grey_mass, cord_red, cord_grey, graph_line

def animate(i):
    x1 = x1_vals[i]
    y2 = y2_vals[i]

    red_mass.set_xy((x1, 150))
    grey_mass.set_xy((320, y2))

    cord_red.set_data([x1 + 30, 320], [165, 165])
    cord_grey.set_data([335, 335], [180, y2])

    t_plot.append(t_vals[i])
    x_plot.append((x1 - 40) / 50)
    graph_line.set_data(t_plot, x_plot)

    return red_mass, grey_mass, cord_red, cord_grey, graph_line

ani = animation.FuncAnimation(
    fig, animate, frames=len(t_vals), init_func=init,
    interval=dt * 1000, blit=True, repeat=False
)

HTML(ani.to_jshtml())
