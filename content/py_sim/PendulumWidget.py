import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parameters
L = 1.5         # Length pendulum (scaled)
g = 9.81        # Gravity (m/s^2)
phi0 = 1.6      # Initial angle (rad)
t_stop = 10     # Total time (s)
dt = 0.05       # Time step (s)

w0 = np.sqrt(g / L)

# Time array
t = np.arange(0, t_stop, dt)

# Numerical solution of pendulum using simple Euler method
phi_num = np.zeros_like(t)
w_num = np.zeros_like(t)
phi_num[0] = phi0
w_num[0] = 0
for i in range(1, len(t)):
    w_num[i] = w_num[i-1] - (g / L) * np.sin(phi_num[i-1]) * dt
    phi_num[i] = phi_num[i-1] + w_num[i] * dt

# Harmonic oscillator approx (small angle approx)
phi_harm = phi0 * np.cos(w0 * t)

# Green pendulum: fixed small angle 0.2 rad harmonic approx
phi_fixed = 0.2 * np.cos(w0 * t)

# Setup plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Left canvas: pendulum animation setup
ax1.set_xlim(-L*1.2, L*1.2)
ax1.set_ylim(-L*1.2, L*1.2)
ax1.set_aspect('equal')
ax1.set_title('Pendulum Animation')
ax1.axis('off')

rod_num, = ax1.plot([], [], 'r-', lw=3, label='Numerical Pendulum')
bob_num = ax1.plot([], [], 'ro', ms=10)[0]

rod_harm, = ax1.plot([], [], 'b-', lw=3, label='Harmonic Approx')
bob_harm = ax1.plot([], [], 'bo', ms=8)[0]

rod_fixed, = ax1.plot([], [], 'g-', lw=3, label='Fixed Small Angle')
bob_fixed = ax1.plot([], [], 'go', ms=8)[0]

ax1.legend(loc='upper right')

# Right canvas: angle vs time plots
ax2.set_xlim(0, t_stop)
ax2.set_ylim(-phi0 * 1.2, phi0 * 1.2)
ax2.set_title('Pendulum Angle vs Time')
ax2.set_xlabel('$t$ (s)')
ax2.set_ylabel('$\\phi$ (rad)')
line_num, = ax2.plot([], [], 'r-', label='Numerical')
line_harm, = ax2.plot([], [], 'b-', label='Harmonic')
line_fixed, = ax2.plot([], [], 'g-', label='Fixed 0.2 rad')
point_num, = ax2.plot([], [], 'ro')
point_harm, = ax2.plot([], [], 'bo')
point_fixed, = ax2.plot([], [], 'go')
ax2.legend()

def init():
    for artist in [rod_num, bob_num, rod_harm, bob_harm, rod_fixed, bob_fixed,
                   line_num, line_harm, line_fixed, point_num, point_harm, point_fixed]:
        artist.set_data([], [])
    return rod_num, bob_num, rod_harm, bob_harm, rod_fixed, bob_fixed, line_num, line_harm, line_fixed, point_num, point_harm, point_fixed

def update(frame):
    # Current angles
    phi_n = phi_num[frame]
    phi_h = phi_harm[frame]
    phi_f = phi_fixed[frame]

    # Coordinates for bobs (pendulum rods)
    x_num = L * np.sin(phi_n)
    y_num = -L * np.cos(phi_n)

    x_harm = L * np.sin(phi_h)
    y_harm = -L * np.cos(phi_h)

    x_fixed = L * np.sin(phi_f)
    y_fixed = -L * np.cos(phi_f)

    # Update pendulum rods and bobs
    rod_num.set_data([0, x_num], [0, y_num])
    bob_num.set_data([x_num], [y_num])

    rod_harm.set_data([0, x_harm], [0, y_harm])
    bob_harm.set_data([x_harm], [y_harm])

    rod_fixed.set_data([0, x_fixed], [0, y_fixed])
    bob_fixed.set_data([x_fixed], [y_fixed])

    # Update angle vs time lines (up to current frame)
    time_so_far = t[:frame+1]
    line_num.set_data(time_so_far, phi_num[:frame+1])
    line_harm.set_data(time_so_far, phi_harm[:frame+1])
    line_fixed.set_data(time_so_far, phi_fixed[:frame+1])

    # Update current points on the plots (wrap scalars in lists)
    point_num.set_data([t[frame]], [phi_num[frame]])
    point_harm.set_data([t[frame]], [phi_harm[frame]])
    point_fixed.set_data([t[frame]], [phi_fixed[frame]])

    return rod_num, bob_num, rod_harm, bob_harm, rod_fixed, bob_fixed, line_num, line_harm, line_fixed, point_num, point_harm, point_fixed

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=50)
HTML(ani.to_jshtml())

