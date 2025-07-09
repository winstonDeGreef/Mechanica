import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Adjustable Parameters
Fgirl = int(input('F_girl (N) (Can range from 5 to 25)'))  # N (can range from 5 to 25)
Delta = int(input('$\\Delta$ (cm) (Can range from 1 to 5)'))  # cm (can range from 1 to 5)
Lrope = 5  # meters

# Force calculations
Fboys_y = Fgirl / 2
Fboys_x = Lrope / (4 * Delta * 1e-2) * Fgirl
Fboys = np.sqrt(Fboys_x**2 + Fboys_y**2)

# Arrow scaling parameters
max_arrow_len = 3  # meters max arrow length
max_force = 40  # expected max force in Newtons
arrow_scale = max_arrow_len / max_force  # meters per Newton

# Setup the figure
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(-1, 6)
ax.set_ylim(-0.5, 7.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('auto')
ax.grid(True)

# Rope and dots with explicit zorder for layering
line, = ax.plot([], [], 'r-', lw=4, zorder=1)  # rope behind everything
girl_dot, = ax.plot([], [], 'ko', markersize=10, label='Girl', zorder=4)
boy1_dot, = ax.plot([0], [0], 'bo', markersize=12, label='Boy (Left)', zorder=4)
boy2_dot, = ax.plot([5], [0], 'bo', markersize=12, label='Boy (Right)', zorder=4)

# Legend
ax.legend(loc='upper right')

# To track dynamic force arrows and text
force_artists = []

def rope_straight(y_middle):
    x = [0, 2.5, 5]
    y = [0, y_middle, 0]
    return x, y

def init():
    line.set_data([], [])
    girl_dot.set_data([], [])
    return line, girl_dot

def update(frame):
    global force_artists

    # Remove previous arrows and labels
    for artist in force_artists:
        artist.remove()
    force_artists = []

    y_middle = Delta if frame == 1 else 0
    x, y = rope_straight(y_middle)

    # Rope and girl dot
    line.set_data(x, y)
    girl_dot.set_data([2.5], [y_middle])

    if frame == 1:
        # Calculate scaled arrow lengths based on forces
        girl_len = min(arrow_scale * Fgirl, max_arrow_len)
        boy_len = min(arrow_scale * Fboys, max_arrow_len)

        # Girl's upward force arrow and label
        ag = ax.arrow(2.5, y_middle, 0, girl_len, head_width=0.1, color='k',
                      length_includes_head=True, zorder=5)
        tg = ax.text(2.5, y_middle + girl_len + 0.1, f'{Fgirl} N', ha='center', fontsize=10, zorder=5)
        force_artists += [ag, tg]

        # Boys’ forces along rope
        dx = -2.5
        dy = -y_middle
        vec_len = np.sqrt(dx**2 + dy**2)
        ux, uy = dx / vec_len, dy / vec_len  # unit vector along rope

        # Left boy arrow and label
        ab1 = ax.arrow(2.5, y_middle, boy_len * ux, boy_len * uy,
                       head_width=0.1, color='b', length_includes_head=True, zorder=5)
        tb1 = ax.text(2.5 + boy_len * ux * 1.1, y_middle + boy_len * uy * 1.1,
                      f'{Fboys:.1f} N', ha='right', fontsize=10, color='b', zorder=5)

        # Right boy arrow and label
        ab2 = ax.arrow(2.5, y_middle, -boy_len * ux, boy_len * uy,
                       head_width=0.1, color='b', length_includes_head=True, zorder=5)
        tb2 = ax.text(2.5 - boy_len * ux * 1.1, y_middle + boy_len * uy * 1.1,
                      f'{Fboys:.1f} N', ha='left', fontsize=10, color='b', zorder=5)

        force_artists += [ab1, ab2, tb1, tb2]

    return line, girl_dot

# Animation: only two frames
ani = FuncAnimation(fig, update, frames=[0, 1],
                    init_func=init, blit=False, repeat=True)

HTML(ani.to_jshtml())
