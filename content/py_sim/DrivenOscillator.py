import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec
from IPython.display import HTML

# Parameters
m = 1
k = 2
b = 0.5
F0 = 20
nu = 4
l0 = 200
dx = 0.28 * l0

# Derived parameters
w0 = np.sqrt(k / m)
w = np.sqrt(w0**2 - (b / (2 * m))**2)
phi = np.arctan(-nu * b / m / (nu**2 - w0**2))
xmax = F0 / m / np.sqrt((nu**2 - w0**2)**2 + (b * nu / m)**2)

A = dx - xmax * np.cos(phi)
B = (1 / w) * (-A * b / (2 * m) + xmax * nu * np.sin(phi))

# Time setup
t_stop = 20
fps = 30
dt = 1 / fps
t_vals = np.arange(0, t_stop, dt)

# Position function
def position(t):
    transient = A * np.exp(-b / (2 * m) * t) * np.cos(w * t) + B * np.exp(-b / (2 * m) * t) * np.sin(w * t)
    steady = xmax * np.cos(nu * t - phi)
    return l0 + transient + steady

x_vals = position(t_vals)

# Steady-state amplitude over range of driving frequencies
nu_range = np.linspace(0, 10, 400)
xmax_range = F0 / m / np.sqrt((nu_range**2 - w0**2)**2 + (b * nu_range / m)**2)

# Set up figure and gridspec
fig = plt.figure(figsize=(16, 4))
gs = GridSpec(1, 3, width_ratios=[1, 1.5, 1.5])
ax_anim = fig.add_subplot(gs[0])
ax_xt = fig.add_subplot(gs[1])
ax_amp = fig.add_subplot(gs[2])

# --- Animation axis setup ---
ax_anim.set_xlim(0, 500)
ax_anim.set_ylim(-50, 50)
mass_dot, = ax_anim.plot([], [], 'ro', markersize=15)
spring_line, = ax_anim.plot([], [], 'k-', lw=1.5)
# Horizontal L0 line from wall to equilibrium position
l0_line, = ax_anim.plot([0, l0], [0, 0], linestyle='--', color='gray', label='$L_0$')
ax_anim.legend(loc='upper right', fontsize=8, frameon=False)
time_text = ax_anim.text(0.02, 0.95, '', transform=ax_anim.transAxes)
ax_anim.set_xticks([])
ax_anim.set_yticks([])

# --- x(t) axis setup ---
xt_line, = ax_xt.plot([], [], 'b-')
ax_xt.set_xlim(0, t_stop)
ax_xt.set_ylim(np.min(x_vals) - 10, np.max(x_vals) + 10)
ax_xt.set_xlabel("$t$ (s)")
ax_xt.set_ylabel("$x$")
ax_xt.set_title("x(t) — Position over Time")
ax_xt.set_xticks([])
ax_xt.set_yticks([])

# --- Steady-state amplitude axis setup ---
amp_line, = ax_amp.plot(nu_range, xmax_range, 'g-')
nu_line = ax_amp.axvline(nu, color='red', linestyle='--', label='$\\nu$')
w0_line = ax_amp.axvline(w0, color='green', linestyle='--', label='$\\omega_0$')
ax_amp.set_xlim(0, 10)
ax_amp.set_ylim(0, np.max(xmax_range) * 1.1)
ax_amp.set_xlabel("Driving Frequency $\\nu$ (Hz)")
ax_amp.set_title("Steady-State Amplitude vs $\\nu$")
ax_amp.legend(loc='upper right', fontsize=8, frameon=False)
ax_amp.set_yticklabels([])
# Function to draw spring as a zig-zag between 0 and x
def get_spring_coords(x, num_zigs=12, amplitude=10, end_offset=7):
    x_end = x - end_offset  # shorten to avoid overshooting the mass
    xs = np.linspace(0, x_end, num_zigs + 1)
    ys = np.zeros_like(xs)
    ys[1:-1:2] = amplitude
    ys[2::2] = -amplitude
    return xs, ys

def init():
    mass_dot.set_data([], [])
    spring_line.set_data([], [])
    time_text.set_text('')
    xt_line.set_data([], [])
    return mass_dot, spring_line, time_text, xt_line, nu_line, w0_line

def animate(i):
    x = x_vals[i]
    mass_dot.set_data([x], [0])

    # Update spring line with zig-zag
    xs, ys = get_spring_coords(x)
    spring_line.set_data(xs, ys)

    time_text.set_text(f"$t$ = {t_vals[i]:.2f} s")
    xt_line.set_data(t_vals[:i], x_vals[:i])
    return mass_dot, spring_line, time_text, xt_line, nu_line, w0_line

ani = FuncAnimation(fig, animate, frames=len(t_vals), init_func=init, blit=True, interval=1000*dt)

HTML(ani.to_jshtml())
