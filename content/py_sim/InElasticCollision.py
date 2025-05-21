import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import atan2, degrees
from IPython.display import HTML

# -------------------------------
# Adjustable Parameters
# -------------------------------
m1 = 1        # mass of particle 1
m2 = 1        # mass of particle 2
v1x = 1       # x velocity of particle 1
v1y = 1       # y velocity of particle 1
v2x = 0       # x velocity of particle 2 (fixed)
v2y = 1       # y velocity of particle 2
e = 0.5       # coefficient of restitution

# -------------------------------
# Constants and Initial Velocities
# -------------------------------
dt = 0.05
t_stop = 6
tcoll = 3
scale = 40

v1 = np.array([v1x, v1y], dtype=float)
v2 = np.array([v2x, v2y], dtype=float)

# -------------------------------
# Compute Inelastic Collision Result
# -------------------------------
def compute_inelastic_collision(m1, m2, v1, v2, e):
    Vcg = (m1 * v1 + m2 * v2) / (m1 + m2)
    u1 = v1 - Vcg
    u2 = v2 - Vcg

    # Rotation matrix to align with u1 direction
    angle = atan2(u1[1], u1[0])
    R = np.array([[np.cos(angle), np.sin(angle)],
                  [-np.sin(angle), np.cos(angle)]])
    
    u1_rot = R @ u1
    u2_rot = R @ u2

    # 1D inelastic collision along x-axis in rotated frame
    wac1x = (m1 * u1_rot[0] + m2 * u2_rot[0] - e * m2 * (u1_rot[0] - u2_rot[0])) / (m1 + m2)
    wac2x = wac1x + e * (u1_rot[0] - u2_rot[0])

    wac1 = np.array([wac1x, 0])
    wac2 = np.array([wac2x, 0])

    # Rotate back to original frame
    R_inv = np.linalg.inv(R)
    w1 = R_inv @ wac1 + Vcg
    w2 = R_inv @ wac2 + Vcg

    return w1, w2

w1, w2 = compute_inelastic_collision(m1, m2, v1, v2, e)

# Angle outputs (rounded to nearest 10 degrees)
alpha_1 = round(degrees(atan2(w1[1], w1[0])) / 10,1) * 10
alpha_2 = round(degrees(atan2(w2[1], w2[0])) / 10,1) * 10

# Initial positions so particles collide at origin at t = tcoll
x1_init = -v1 * (t_stop - tcoll)
x2_init = -v2 * (t_stop - tcoll)
x1_coll = x1_init + v1 * tcoll
x2_coll = x2_init + v2 * tcoll

# -------------------------------
# Set Up Plot
# -------------------------------
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.set_aspect('equal')
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid()

p1, = ax.plot([], [], 'ro')
p2, = ax.plot([], [], 'bo')
path1, = ax.plot([], [], 'r--', lw=1)
path2, = ax.plot([], [], 'b--', lw=1)
angle_text = ax.text(0.02, 0.02, '', transform=ax.transAxes)

traj1, traj2 = [], []

# -------------------------------
# Animation Functions
# -------------------------------
def init():
    p1.set_data([], [])
    p2.set_data([], [])
    path1.set_data([], [])
    path2.set_data([], [])
    angle_text.set_text('')
    return p1, p2, path1, path2, angle_text

def update(frame):
    t = frame * dt
    if t < tcoll:
        pos1 = x1_init + v1 * t
        pos2 = x2_init + v2 * t
    else:
        pos1 = x1_coll + w1 * (t - tcoll)
        pos2 = x2_coll + w2 * (t - tcoll)

    traj1.append(pos1.copy())
    traj2.append(pos2.copy())

    # Set current positions
    p1.set_data([scale * pos1[0]], [scale * pos1[1]])
    p2.set_data([scale * pos2[0]], [scale * pos2[1]])

    # Extract x and y lists separately for paths
    traj1_x = [p[0] for p in traj1]
    traj1_y = [p[1] for p in traj1]
    traj2_x = [p[0] for p in traj2]
    traj2_y = [p[1] for p in traj2]

    path1.set_data(scale * np.array(traj1_x), scale * np.array(traj1_y))
    path2.set_data(scale * np.array(traj2_x), scale * np.array(traj2_y))

    if abs(t - t_stop) < dt:
        angle_text.set_text(f"α₁ = {alpha_1}°, α₂ = {alpha_2}°")

    return p1, p2, path1, path2, angle_text


# -------------------------------
# Run Animation
# -------------------------------
ani = FuncAnimation(fig, update, frames=int(t_stop / dt), init_func=init, blit=True, interval=50)
HTML(ani.to_jshtml())
