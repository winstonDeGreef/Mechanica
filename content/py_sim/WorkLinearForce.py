import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# --- Inputs ---
x0 = float(input('Initial position (m) from 0 to 10'))        # Initial position (m)
v0 = float(input('Initial velocity (m/s) from -10 to 10'))        # Initial velocity (m/s)
k = float(input('Spring constant (N/m) from 0.1 to 1'))       # Spring constant (N/m)
m = 2.0        # Mass (kg)

# --- Derived ---
omega = np.sqrt(k / m)
t_stop = 4.0
dt = 0.02
t_values = np.arange(0, t_stop, dt)

# --- Analytical solution for x(t) ---
C1 = 0.5 * x0 + 0.5 * v0 / omega
C2 = 0.5 * x0 - 0.5 * v0 / omega
x = C1 * np.exp(omega * t_values) + C2 * np.exp(-omega * t_values)

# Velocity is not needed directly as E_kin = total energy - work (from energy conservation)
W = 0.5 * k * (x**2 - x0**2)
v_squared = v0**2 + 2 * W / m
E_kin = 0.5 * m * v_squared

# --- Plot setup ---
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
ax_block = axs[0, 0]
ax_pos = axs[1, 0]
ax_ekin = axs[0, 1]
ax_work = axs[1, 1]

# Set axis limits
ax_block.set_xlim(min(x)-1, max(x)+1)
ax_block.set_ylim(-1, 1)
ax_block.set_title("Block motion")
ax_block.set_yticks([])
ax_block.axhline(y=-0.06, color='black', linewidth=5)

ax_pos.set_xlim(0, t_stop)
ax_pos.set_ylim(min(x)-1, max(x)+1)
ax_pos.set_title("Position vs Time")

ax_ekin.set_xlim(0, t_stop)
ax_ekin.set_ylim(0, max(E_kin)*1.1)
ax_ekin.set_title("Kinetic Energy vs Time")

ax_work.set_xlim(0, t_stop)
ax_work.set_ylim(min(W)*1.1, max(W)*1.1)
ax_work.set_title("Work vs Time")

# Artists
block_dot, = ax_block.plot([], [], 'rs', markersize=10)
line_pos, = ax_pos.plot([], [], 'b')
line_ekin, = ax_ekin.plot([], [], 'g')
line_work, = ax_work.plot([], [], 'r')

# --- Init ---
def init():
    block_dot.set_data([], [])
    line_pos.set_data([], [])
    line_ekin.set_data([], [])
    line_work.set_data([], [])
    return block_dot, line_pos, line_ekin, line_work

# --- Update function ---
def update(frame):
    t = t_values[:frame]
    block_dot.set_data([x[frame]], [0])
    line_pos.set_data(t, x[:frame])
    line_ekin.set_data(t, E_kin[:frame])
    line_work.set_data(t, W[:frame])
    return block_dot, line_pos, line_ekin, line_work

# --- Animation ---
ani = FuncAnimation(fig, update, frames=len(t_values),
                    init_func=init, interval=dt*1000, blit=True)

plt.close(fig)  # Prevent double static plot
HTML(ani.to_jshtml())
