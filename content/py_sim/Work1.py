import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# --- Input values ---
x0 = float(input('initial position from 0 to 10'))     # initial position
v0 = float(input('Initial velocity from -5 to 5'))     # initial velocity
F = float(input('Constant force from -10 to 10'))    # constant force
m = 1      # mass

# --- Simulation setup ---
t_stop = 2
dt = 0.02
t_values = np.arange(0, t_stop, dt)

# --- Kinematics ---
a = F / m
x = x0 + v0 * t_values + 0.5 * a * t_values**2
v = v0 + a * t_values
E_kin = 0.5 * m * v**2
W = F * (x - x0)

# --- Create figure and axes ---
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
ax_block = axs[0, 0]
ax_pos = axs[1, 0]
ax_ekin = axs[0, 1]
ax_work = axs[1, 1]

# --- Axis setup ---
ax_block.set_xlim(min(x)-1, max(x)+1)
ax_block.set_ylim(-1, 1)
ax_block.set_yticks([])
ax_block.set_title("Block Motion")
ax_block.axhline(y=-0.06, color='black', linewidth=5)

ax_pos.set_xlim(0, t_stop)
ax_pos.set_ylim(min(x)-1, max(x)+1)
ax_pos.set_title("Position vs Time")
ax_pos.set_xlabel("t [s]")
ax_pos.set_ylabel("x [m]")

ax_ekin.set_xlim(0, t_stop)
ax_ekin.set_ylim(0, max(E_kin)*1.1)
ax_ekin.set_title("Kinetic Energy vs Time")
ax_ekin.set_xlabel("t [s]")
ax_ekin.set_ylabel("Eₖ [J]")

ax_work.set_xlim(0, t_stop)
ax_work.set_ylim(min(W)*1.1, max(W)*1.1)
ax_work.set_title("Work vs Time")
ax_work.set_xlabel("t [s]")
ax_work.set_ylabel("W [J]")

# --- Artists to update ---
block_dot, = ax_block.plot([], [], 'rs', markersize=10)
line_pos, = ax_pos.plot([], [], 'b')
line_ekin, = ax_ekin.plot([], [], 'g')
line_work, = ax_work.plot([], [], 'm')

# --- Init function ---
def init():
    block_dot.set_data([], [])
    line_pos.set_data([], [])
    line_ekin.set_data([], [])
    line_work.set_data([], [])
    return block_dot, line_pos, line_ekin, line_work

# --- Animation update function ---
def update(frame):
    t = t_values[:frame]
    block_dot.set_data([x[frame]], [0])
    line_pos.set_data(t, x[:frame])
    line_ekin.set_data(t, E_kin[:frame])
    line_work.set_data(t, W[:frame])
    return block_dot, line_pos, line_ekin, line_work

# --- Animation setup ---
ani = FuncAnimation(fig, update, frames=len(t_values),
                    init_func=init, interval=dt*1000, blit=True)

plt.close(fig)  # Prevent double display
HTML(ani.to_jshtml())
