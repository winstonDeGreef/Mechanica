import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML, Math
import ipywidgets as widgets

# Constants
m1_init = 1
m2_init = 1
v1x_init = 1
v1y_init = 0
v2x_init = 0
v2y_init = 1

x1_init = -1
y1_init = 0
x2_init = 0
y2_init = -1


# Time setup
dt = 0.05
time_max = 1
times_neg = np.arange(-time_max, dt, dt)
times_pos = np.arange(dt, time_max, dt)
times = np.arange(-time_max, time_max, dt)
Ntimes = len(times_neg) + len(times_pos)

# Widget slider mass 1
mass1_slider = widgets.FloatSlider(
    value=1,
    min=1,
    max=5,
    step=1,
    description='m1:',
    continuous_update=False
)

# Widget slider mass 2
mass2_slider = widgets.FloatSlider(
    value=1,
    min=1,
    max=5,
    step=1,
    description='m2:',
    continuous_update=False
)

# Widget slider velo v1x
velocity1x_slider = widgets.FloatSlider(
    value=1,
    min=1,
    max=5,
    step=1,
    description='v1x:',
    continuous_update=False
)

# Widget slider velo
velocity1y_slider = widgets.FloatSlider(
    value=0,
    min=-3,
    max=3,
    step=1,
    description='v1y:',
    continuous_update=False
)

# Widget slider velo v2x
velocity2x_slider = widgets.FloatSlider(
    value=0,
    min=-3,
    max=1,
    step=1,
    description='v2x:',
    continuous_update=False
)

# Widget slider velo
velocity2y_slider = widgets.FloatSlider(
    value=1,
    min=1,
    max=3,
    step=1,
    description='v2y:',
    continuous_update=False
)

def CalcCol(m1_init,m2_init,v1x_init,v1y_init,v2x_init,v2y_init):
    #initiallise m's and v's
    v1x, v1y = v1x_init, v1y_init
    v2x, v2y = v2x_init, v2y_init
    m1, m2 = m1_init, m2_init
    cos_2 = v2x/np.sqrt(v2x*v2x+v2y*v2y)
    sin_2 = v2y/np.sqrt(v2x*v2x+v2y*v2y)
    
    # new velocities after collision
    # velo center of gravity
    Vcg_x=(m1*v1x+m2*v2x)/(m1+m2);
    Vcg_y=(m1*v1y+m2*v2y)/(m1+m2);
    #relative velos before coll in COG
    u1x=v1x-Vcg_x;
    u1y=v1y-Vcg_y;
    u2x=v2x-Vcg_x;
    u2y=v2y-Vcg_y;
    u1=np.sqrt(u1x*u1x+u1y*u1y);
    u2=np.sqrt(u2x*u2x+u2y*u2y);
    cos_1=u1x/u1;
    sin_1=u1y/u1;
    cos_2=u2x/u2;
    sin_2=u2y/u2;

	#rotation matrix to rotatate to 1D picture -> particles moving over x-axis
    A11=cos_1;
    A12=sin_1;
    A21=-sin_1;
    A22=cos_1;
    uac1x=A11*u1x+A12*u1y;
    uac1y=A21*u1x+A22*u1y;
    uac2x=A11*u2x+A12*u2y;
    uac2y=A21*u2x+A22*u2y;
    
    #new velos: do a 1D collision
    wac2x=((1-m1/m2)*uac2x+2*m1/m2*uac1x)/(1+m1/m2);
    wac1x=uac2x-uac1x+wac2x;
    wac1y=0;
    wac2y=0;
    #rotate back
    w1x=A11*wac1x-A12*wac1y;
    w1y=-A21*wac1x+A22*wac1y;
    w2x=A11*wac2x-A12*wac2y;
    w2y=-A21*wac2x+A22*wac2y;
    #transform back to lab frame
    vnew1_x=w1x+Vcg_x;
    vnew1_y=w1y+Vcg_y;
    vnew2_x=w2x+Vcg_x;
    vnew2_y=w2y+Vcg_y;
    if vnew1_x <0.0001:
        alpha_1 = 90
    else:
        alpha_1 = round(np.arctan(vnew1_y / vnew1_x)/np.pi*180/10)*10;
    if vnew2_x <0.0001:
        alpha_2 = 90
    else:
        alpha_2 = round(np.arctan(vnew2_y / vnew2_x)/np.pi*180/10)*10;

    return vnew1_x, vnew1_y, vnew2_x, vnew2_y, alpha_1, alpha_2
    
def generate_animation(m1_init,m2_init,v1x_init,v1y_init,v2x_init,v2y_init):
    v1x, v1y = v1x_init, v1y_init
    v2x, v2y = v2x_init, v2y_init
    x1 = v1x*(-time_max)
    x2 = v2x*(-time_max)
    y1 = v1y*(-time_max)
    y2 = v2y*(-time_max)
    
    m1, m2 = m1_init, m2_init

    u1_x, u1_y, u2_x, u2_y, a1, a2 = CalcCol(m1_init,m2_init,v1x_init,v1y_init,v2x_init,v2y_init)
    
    # Position history
    x1_list, y1_list = [], []
    x2_list, y2_list = [], []

    for t in times_neg:
        x1_t = v1x * t
        y1_t = v1y * t
        x1_list.append(x1_t)
        y1_list.append(y1_t)
        x2_t = v2x * t
        y2_t = v2y * t
        x2_list.append(x2_t)
        y2_list.append(y2_t)

    for t in times_pos:
        x1_t = u1_x * t
        y1_t = u1_y * t
        x1_list.append(x1_t)
        y1_list.append(y1_t)
        x2_t = u2_x * t
        y2_t = u2_y * t
        x2_list.append(x2_t)
        y2_list.append(y2_t)
    
    # Create figure and axes
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
#    ax.set_yticks([])
    ax.set_title("2D Elastic Collision")
    ax.plot([-6,6],[0,0], color='grey')
    ax.plot([0,0],[-6,6], color='grey')

    p1, = ax.plot([], [], 'ro', markersize=6, label='Particle 1')
    p2, = ax.plot([], [], 'bo', markersize=6, label='Particle 2')
    p1_line_f, = ax.plot((x1_list[0],x1_list[0]),(y1_list[0],y1_list[0]),'r-')
    p1_line_a, = ax.plot((0,0),(0,0),'r-')
    p2_line_f, = ax.plot((x2_list[0],x2_list[0]),(y2_list[0],y2_list[0]),'b-')
    p2_line_a, = ax.plot((0,0),(0,0),'b-')
    ax.grid()
    ax.legend(loc='upper right')

    def init():
        p1.set_data([], [])
        p2.set_data([], [])
        return p1, p2

    def update(i):
        p1.set_data([x1_list[i]], [y1_list[i]])
        p2.set_data([x2_list[i]], [y2_list[i]])
        if i < len(times_neg):
            p1_line_f.set_data((x1_list[0],x1_list[i]),(y1_list[0],y1_list[i]))
            p2_line_f.set_data((x2_list[0],x2_list[i]),(y2_list[0],y2_list[i]))
        else:
            p1_line_a.set_data((0,x1_list[i]),(0,y1_list[i]))
            p2_line_a.set_data((0,x2_list[i]),(0,y2_list[i]))
        return p1, p2

    
    ani = animation.FuncAnimation(fig, update, frames=Ntimes, init_func=init,
                                  interval=50, blit=True)

    plt.close(fig)
    return HTML(ani.to_jshtml())

# Show slider and link it to animation
widgets.interact(generate_animation, 
    m1_init = mass1_slider, m2_init = mass2_slider, 
    v1x_init = velocity1x_slider, v1y_init = velocity1y_slider, 
    v2x_init = velocity2x_slider, v2y_init = velocity2y_slider
    );


