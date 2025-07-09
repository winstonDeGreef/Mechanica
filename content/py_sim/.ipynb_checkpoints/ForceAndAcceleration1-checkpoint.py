import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parameters
t_stop = 5
dt = 0.01
t = np.arange(0, t_stop + dt, dt)

# Force functions definitions, explicitly use numpy vectorized operations
def force1(t):
    a = 10
    x = 0.5 * a * t**2
    v = a * t
    return x, v

def force2(t):
    x = (1/6) * 10 * t**3
    v = 0.5 * 10 * t**2
    return x, v

def force3(t):
    # Use numpy.pi and ensure t is array
    x = 125 * (1 - np.cos(np.pi * t / 2))
    v = 125 * (np.pi / 2) * np.sin(np.pi * t / 2)
    return x, v

# Choose force here: '1', '2' or '3'
force_num = input('1/2/3')  # change this to '2' or '3' for other forces

if force_num == '1':
    selected_force = force1
elif force_num == '2':
    selected_force = force2
else:
    selected_force = force3

x_vals, v_vals = selected_force(t)

# Ensure x_vals and v_vals are numpy arrays
x_vals = np.array(x_vals)
v_vals = np.array(v_vals)

# Setup figure with 3 parts:
fig = plt.figure(figsize=(12, 6))

# Left plot: mass on line
ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=2)
ax1.set_xlim(-5, np.max(x_vals)*1.1)
ax1.set_ylim(-1, 2)
ax1.axis('off')
line_y = 0.5
ax1.plot([-5, np.max(x_vals)*1.1], [line_y-0.06, line_y-0.06], 'k-', linewidth=2)
mass_marker, = ax1.plot([0], [line_y], 'rs', markersize=12)
ax1.set_title('Mass sliding on horizontal surface')

# Right top: velocity vs time
ax2 = plt.subplot2grid((2, 3), (0, 1), colspan=2)
ax2.set_xlim(0, t_stop)
ax2.set_ylim(-np.max(v_vals)*1.2, np.max(v_vals)*1.2)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (cm/s)')
ax2.set_title('Velocity vs Time')
line_v, = ax2.plot([], [], 'b-')

# Right bottom: position vs time
ax3 = plt.subplot2grid((2, 3), (1, 1), colspan=2)
ax3.set_xlim(0, t_stop)
ax3.set_ylim(0, np.max(x_vals)*1.2)
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Position (cm)')
ax3.set_title('Position vs Time')
line_x, = ax3.plot([], [], 'r-')

plt.tight_layout()

def init():
    line_v.set_data([], [])
    line_x.set_data([], [])
    mass_marker.set_data([0], [line_y])
    return line_v, line_x, mass_marker

def update(frame):
    mass_marker.set_data([x_vals[frame]], [line_y])  
    line_v.set_data(t[:frame], v_vals[:frame])
    line_x.set_data(t[:frame], x_vals[:frame])
    return line_v, line_x, mass_marker

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)

HTML(ani.to_jshtml())

