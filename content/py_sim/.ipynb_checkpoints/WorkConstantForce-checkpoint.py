import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# --- Parameters ---
v0 = 5         # Initial velocity (m/s)
F = 6.5        # Constant force (N)
m = 1.0        # Mass (kg)
x0 = 0.0       # Initial position (m)
t_stop = 2.0   # Total time (s)
dt = 0.02      # Time step (s)

# --- Time array ---
t_values = np.arange(0, t_stop + dt, dt)

# --- Derived motion ---
x = x0 + v0 * t_values + 0.5 * F / m * t_values**2
v = v0 + F / m * t_values
E_kin = 0.5 * m * v**2
W = F * (x - x0)

# --- Plot setup ---
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
ax_motion = axs[0, 0]
ax_position = axs[1, 0]
ax_ekin = axs[0, 1]
ax_work = axs[1, 1]

# Set axis limits
ax_motion.set_xlim(min(x)-1, max(x)+1)
ax_motion.set_ylim(-1, 1)
ax_motion.set_title("Particle Motion")
ax_motion.set_yticks([])
ax_motion.axhline(y=-0.06, color='black', linewidth=5)

ax_position.set_xlim(0, t_stop)
ax_position.set_ylim(min(x)-1, max(x)+1)
ax_position.set_title("Position vs Time")
ax_position.set_xticklabels([])
ax_position.set_yticklabels([])

ax_ekin.set_xlim(0, t_stop)
ax_ekin.set_ylim(0, max(E_kin)*1.1)
ax_ekin.set_title("Kinetic Energy vs Time")
ax_ekin.set_xticklabels([])
ax_ekin.set_yticklabels([])

ax_work.set_xlim(0, t_stop)
ax_work.set_ylim(min(W)*1.1, max(W)*1.1)
ax_work.set_title("Work Done vs Time")
ax_work.set_xticklabels([])
ax_work.set_yticklabels([])
# Artists
dot, = ax_motion.plot([], [], 'rs', markersize=10)
line_pos, = ax_position.plot([], [], 'b')
line_ekin, = ax_ekin.plot([], [], 'g')
line_work, = ax_work.plot([], [], 'r')

# --- Init function ---
def init():
    dot.set_data([], [])
    line_pos.set_data([], [])
    line_ekin.set_data([], [])
    line_work.set_data([], [])
    return dot, line_pos, line_ekin, line_work

# --- Update function ---
def update(frame):
    t = t_values[:frame]
    dot.set_data([x[frame]], [0])
    line_pos.set_data(t, x[:frame])
    line_ekin.set_data(t, E_kin[:frame])
    line_work.set_data(t, W[:frame])
    return dot, line_pos, line_ekin, line_work

# --- Animation ---
ani = FuncAnimation(fig, update, frames=len(t_values),
                    init_func=init, interval=dt*1000, blit=True)

plt.close(fig)
HTML(ani.to_jshtml())
