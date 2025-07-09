import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parameters
m1 = 1.0  # Red block mass
g_values = {"moon": 1.62, "earth": 9.813, "jupiter": 24.79}
M_values = [0.2, 1.0, 5.0]  # Grey block mass

# User selection
g = g_values[input('Choose: moon/earth/jupiter')]   # Options: "moon", "earth", "jupiter"
M = float(input('Choose: 0.2/1.0/5.0 kg'))        # Options: 0.2, 1.0, 5.0

# Physics
acc = M / (m1 + M) * g  # Net acceleration
t_stop = 1.5
dt = 0.02
t_vals = np.arange(0, t_stop, dt)

# Pixel scaling factor: 25 px per (m/s² * s²), as in JS
scale_factor = 25

# Initial positions
x0 = 40
y0 = 210

# Canvas setup
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 900)
ax.set_ylim(500, 0)
ax.axis('off')

# Static elements
ax.fill_between([20, 320], 180, 190, color='black')  # floor
pulley = plt.Circle((320, 180), 15, color='grey')
ax.add_patch(pulley)

# Graph axes
ax.plot([450, 450], [20, 470], color='black')   # y-axis
ax.plot([450, 800], [420, 420], color='black')  # x-axis
ax.text(408, 170, "x (m)", fontsize=12)
ax.text(780, 440, "t (s)", fontsize=12)

# Labels
for i, y in enumerate(range(125, 426, 75)):
    ax.text(423, y, f"{(4 - i):.1f}", fontsize=10)
for i, x in enumerate([540, 640, 740]):
    ax.text(x, 440, f"{0.5 * (i + 1):.1f}", fontsize=10)

# Grid lines
for i in range(24):
    ax.plot([450, 800], [420 - 15 * (i + 1)] * 2, color='grey', linewidth=0.5)
for i in range(17):
    ax.plot([450 + 20 * (i + 1)] * 2, [60, 420], color='grey', linewidth=0.5)

# Objects
red_block = Rectangle((x0, 150), 30, 30, color='red')
grey_block = Rectangle((320, y0), 30, 30, color='grey')
ax.add_patch(red_block)
ax.add_patch(grey_block)
cord1, = ax.plot([], [], color='black')
cord2, = ax.plot([], [], color='black')
trace, = ax.plot([], [], color='blue')
x_trace, y_trace = [], []

def update(frame):
    t = frame * dt
    disp = scale_factor * 0.5 * acc * t**2  # consistent with JS

    x = min(x0 + disp, 270)
    y = min(y0 + disp, 440)

    red_block.set_xy((x, 150))
    grey_block.set_xy((320, y))
    cord1.set_data([x + 30, 320], [165, 165])
    cord2.set_data([335, 335], [180, y])

    # Stop x-t trace when red block reaches pulley
    if x < 270:
        x_trace.append(450 + (200 * t))
        y_trace.append(420 - 1.53 * (x - x0))
        trace.set_data(x_trace, y_trace)

    return red_block, grey_block, cord1, cord2, trace


ani = FuncAnimation(fig, update, frames=len(t_vals), blit=True, interval=dt * 1000)
HTML(ani.to_jshtml())

