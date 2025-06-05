import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from IPython.display import HTML

# Parameters (initial)
k = 1.5   # Spring constant
b = 0.5   # Damping constant
m = 1.0   # Mass
l0 = 200  # Natural length of the spring (in arbitrary units)
dx = 0.28 * l0  # Initial displacement
dt = 0.05
t_max = 10

# Derived quantities
w0 = np.sqrt(k / m)
Discr = b**2 - 4 * m * k

# Amplitude constants
if Discr < 0:
    w = np.sqrt(k/m - (b**2) / (4 * m**2))
    A = dx
    B = (1 / w) * (-A * b / (2 * m))
else:
    w = np.sqrt((b**2) / (4 * m**2) - k / m)
    A = dx
    B = 0  # Not used

# Time array
t_vals = np.arange(0, t_max, dt)

# Displacement function
def displacement(t):
    if Discr < 0:
        return A * np.exp(-b / (2*m) * t) * np.cos(w * t) + B * np.exp(-b / (2*m) * t) * np.sin(w * t)
    else:
        return (A/2) * np.exp((-b/(2*m) + w) * t) + (A/2) * np.exp((-b/(2*m) - w) * t)

x_vals = displacement(t_vals)
x_spring = 60
x_mass_vals = x_spring + l0 + x_vals

# Zigzag spring function
def zigzag_spring(x1, x2, y=140, n=10, amplitude=10):
    """Returns x and y coordinates of a zigzag spring from x1 to x2"""
    zigzag_x = [x1]
    zigzag_y = [y]
    dx = (x2 - x1) / (2 * n)
    direction = 1

    for _ in range(2 * n):
        x_next = zigzag_x[-1] + dx
        y_next = y + direction * amplitude
        zigzag_x.append(x_next)
        zigzag_y.append(y_next)
        direction *= -1

    zigzag_x.append(x2)
    zigzag_y.append(y)
    return zigzag_x, zigzag_y

# Plot setup
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 900)
ax.set_ylim(0, 500)
ax.set_aspect('equal')
ax.axis('off')

# Draw fixed wall
wall = plt.Rectangle((50, 50), 10, 180, fc='lightblue', ec='black')
ax.add_patch(wall)

# Line for spring
spring_line, = ax.plot([], [], 'k-', lw=2)

# Mass
mass = Circle((0, 140), 15, color='red')
ax.add_patch(mass)

# Graph axes
ax.plot([430, 430], [10, 490], 'k-')
ax.plot([430, 880], [250, 250], 'k-')
x_graph_vals, y_graph_vals = [], []
graph_line, = ax.plot([], [], 'r-')

# Annotation
D_text = ax.text(50, 300, f"D = {round(Discr, 2)} kg²/s²", fontsize=12)

# Animation function
def update(i):
    t = t_vals[i]
    x = x_mass_vals[i]

    # Zigzag spring
    spring_x, spring_y = zigzag_spring(x_spring, x)
    spring_line.set_data(spring_x, spring_y)

    # Mass
    mass.center = (x, 140)

    # Graph
    x_graph_vals.append(430 + 350 * t / t_max)
    y_graph_vals.append(250 - 4 * (x - x_spring - l0))
    graph_line.set_data(x_graph_vals, y_graph_vals)

    return spring_line, mass, graph_line

ani = FuncAnimation(fig, update, frames=len(t_vals), interval=dt*1000, blit=True)

# Display animation
HTML(ani.to_jshtml())
