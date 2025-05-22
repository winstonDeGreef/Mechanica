# Many-Body System

We have seen that we could reduce the two-body problem of sun-earth to a single body question via the concept of reduced mass. But that this strategy does not work for 3, 4, 5, ... bodies.

## Linear Momentum

We can, however, find some basic features of $N$-body problems. In the figure, a collection of $N$ interacting particles is drawn.

```{figure} images/ManyParticles.jpg
---
name: fig:ManyParticles.jpg
width: 150px
align: center
---
Many particle system.
```

Each particle has mass $m_i$ and is at position $x_i(t)$. For each particle, we can set up N2:

$$
m_i \ddot{\vec{x}}_i = \vec{F}_{i, ext} + \sum_{i \neq j} \vec{F}_{ji.}
$$

Summing over all particles and using that all mutual interaction forces form "action = -reaction pairs", we get:

$$
\sum_i m_i \ddot{\vec{x}}_i = \sum_i \vec{F}_{i, ext} \Leftrightarrow \sum_i \dot{\vec{p}}_i = \sum_i \vec{F}_{i, ext}
$$

The second part can be writen as:

$$
\frac{d\vec{P}}{dt} = \sum_i \vec{F}_{i, ext} \text{    with    } \vec{P} \equiv \sum_i \vec{p}_i
$$

In other words: the total momentum changes due to external forces. If there are no external forces, then the total momentum is conserved. This happens quite a lot actually, if you consider e.g. collisions or scattering.

## Center of Mass

Analogous to the two-particle case, we see from the total momentum that we can pretend that there is a particle of total mass $M=\sum_i m_i$ that has momentum $\vec{P}$, i.e., it moves at velocity $\vec{V} \equiv\frac{\vec{P}}{M}$ and is located at position:

$$
\vec{V} = \frac{d\vec{R}}{dt} =\frac{\sum m_i \frac{d\vec{x}_i}{dt}}{\sum m_i} \Rightarrow \vec{R} = \frac{\sum m_i \vec{x}_i}{\sum m_i}
$$

Continuing with the analogy, we define relative coordinates:

$$
\vec{r}_i \equiv \vec{x}_i - \vec{R}
$$

and have a similar rule constraining the relative positions:

$$
\sum m_i \vec{r}_i  = 0
$$

## Energy

In terms of relative coordinates, we can write the kinetic energy as a part associated with the center of mass and a part that describes the kinetic energy with respect to the center of mass, i.e., 'an internal kinetic energy'.

$$
\begin{split}
E_{kin} &\equiv \sum \frac{1}{2} m_i v_i^2 \\
        &= \frac{1}{2} M \dot{\vec{R}}^2 + \sum \frac{1}{2} m_i \dot{\vec{r}}_i^2 \\
        &= E_{kin,cm} + E'_{kin}
\end{split}
$$

For the potential energy, we may write:

$$
V = \sum V_i + \frac{1}{2} \sum_{i \neq j} \left ( V_{ij} + V_{ji} \right )
$$

with $V_i$ the potential related to the external force on particle $i$ and $V_{ij}$ the potential related to the mutual interaction force from particle $i$ exerted on particle $j$ (assuming that all forces are conservative).

## Angular Momentum

The total angular momentum is, like the total momentum, defined as the sum of the angular momentum of all particles:

$$
\vec{L} = \sum \vec{l}_i = \sum \vec{x}_i \times \vec{p}_i
$$

We can write this in the new coordinates:

$$
\vec{L} = \vec{R} \times \vec{P} + \sum \vec{r}_i \times \vec{p}_i = \vec{L}_{cm} + \vec{L}'
$$

Again, we find that the total angular momentum can be seen as the contribution of the center of mass and the sum of the angular momentum of all individual particles as seen from the center of mass.

The N-body problem is, of course, even more complex than the three-body problem. If we can solve it, it will be under very specific conditions only. However, a numerical approach can be done with great success. Moreover, current computers are so powerful that the system can contain hundred, thousands of particles up to billions depending on the type or particle-particle interaction. 

All kind of computational techniques have been developed and various averaging techniques are employed in statistical techniques are introduced from the start. the reason is often, that a particular 'realisation' of all positions and velocities of all particles is needed nor sought for. A system is at its macro level described by averaged properties, the exact location of the individual atoms is not needed. You will find applications in cosmology all the way to molecular dynamics, trying to simulate the behavior of proteins or pharmaceuticals. 

## Exercises ##

```{exercise-start}
:label: 11.1
```
Thee masses are forming an equilateral triangle with sides of 2m. Mass 1 (10kg) is positioned at $(x_1,y_1) = (-1m,0))$. Mass 2 (6kg) is at $(x_2,y_2) = (1m,0))$, while mass 3 (2kg) is at $(x_3,y_3) = (0,\sqrt{3})$.

* Calculate the position of the center of mass.

```{exercise-end}
```

```{exercise-start}
:label: 11.2
```
Four particles are moving over the line $y=y_0$. The particles have mass $m_1 = 4m, m_2 = 3m, m_3 = 2m, m_4 = m$ and velocity $v_1 = v, v_2 = 2v, v_3 = 3v, v_4 = 4v$. These velocities are constant and parallel to the $x$-axis. At $t=0$ all particles are at location $(x,y) = (0,y_0)$.

```{figure} images/FourParticles.png
---
name: fig:FourParticles.png
width: 250px
align: center
---
Four particles moving on a line.
```

* Calculate the velocity of the center of mass.
* Calculate the position of the center of mass as a function of time.
* Calculate the total angular momentum.
* Calculate the angular momentum associated with the center of mass and show that in this case this is equal to the total angular momentum.

```{exercise-end}
```

```{exercise-start}
:label: 11.3
```

Eight point particles (each mass $m$) are attached to a massless wheel of radius $R$.

```{figure} images/Wheel8Masses.png
---
name: fig:Wheel8Masses.png
width: 250px
align: center
---
Eight particles on a wheel.
```

The wheel is moving with a velocity $V$ while it is rotating at the same time with angular velocity $\omega$.

Calculate the total kinetic energy of this system. Hint: use the CM frame and connect that to the lab frame.


```{exercise-end}
```

```{exercise-start}
:label: 11.4
```
A container of volume $V_c$ and mass $M_c$ contains Nitrogen gas. The number of molecules, $N$, is on the order of $10^{23}$. The container is dropped from a height $H$. Gravity is acting on the molecules. Friction on the container is ignored.

Show that the container falls with the acceleration of gravity $g$.

```{exercise-end}
```

```{exercise-start}
:label: 11.5
```
We consider a 2-dimensional problem: $N=30$ particles move in the $xy$-plane. Each particle has a fixed velocity $(v_x^i, v_y^i )$ with $i = 1 ..N$. The particle velocities have a magnitude ranging from 1 to 5 (m/s) randomly chosen for each particle. The direction of each velocity vector is also randomly chosen from 0 to 2$\pi$.
The particles move inside a box with sides $L$=50m. Particles do not collide with each other, but they do collide with the walls of the container. The result of a collision is that the particle motion gets reflected.

* Write a python program that generates N particles starting all at $(x,y)=(0,0)$. 
* Compute the position of all particles after 1 second and compute the velocity and position of the center of mass.
* Write a loop that updates the particle velocities after a time step $dt$ and recompute the velocity and position of the center of mass. 
* Run the loop $M$ times and plot the position of the center of mass in the $xy$-plane as a function of time.

* What happens if you change the number of particles from 30 to 3 or to 300?
```{exercise-end}
```

## Answers ##

```{solution-start} 11.1
:class: dropdown
```
The position of the center of mass is

$$\vec{R} \equiv \frac{\sum_i m_i \vec{x}_i}{\sum_i m_i} = \frac{(m_1 x_1) \hat{x} + (m_2 x_2) \hat{x} + (m_3 y_3) \hat{y}}{m_1 + m_2 + m_3} = -\frac{2}{9}[m] \hat{x} + \frac{1}{9}[m]\hat{y} $$

where $[m]$ indicates that the unit is meters.

Note: $\hat{x}$ and $\hat{y}$ do not carry units!

```{solution-end}
```

```{solution-start} 11.2
:class: dropdown
```

```{figure} images/FourParticlesVectors.png
---
name: fig:FourParticlesVectors.png
width: 350px
align: center
---
Four particles moving on a line.
```

* Velocity of the center of mass: 
$$\vec{V} = \frac{\sum_i m_i \vec{v}_i}{\sum_i m_i} $$
Since the velocities are all parallel to the $x$-axis, we can drop the vector notation. Substituting the data for mass and velocity, gives:

$$ V_x = \frac{4mv + 6mv + 6mv + 4mv}{4m + 3m + 2m + m} = 2v $$
* Position of the center of mass:
$$ \vec{V} = \frac{d\vec{R}}{dt} \rightarrow \vec{R}(t) = 2vt \hat{x} +\vec{c} $$
At $t=0$ all particles at location $(0,y_0)$. Thus, we find

$$ \vec{R}(t) = 2vt \hat{x} + y_0\hat{y} $$

* Total angular momentum:

$$\begin{split}
\vec{L_{tot}} &= \sum_i \vec{l}_i \\
&= y_0 \cdot 4mv \hat{z} +y_0 \cdot 3m\cdot 2v \hat{z} + y_0 \cdot 2m\cdot 3v \hat{z} + y_0 \cdot m \cdot 4v \hat{z} \\
& = 20mvy_0 \hat{z} 
\end{split}$$ 
* Angular momentum associated with the center of mass:

$$ \vec{L} = \vec{R} \times M\vec{V} = y_0 10m \cdot 2v \hat{z} = 20mvy_0 \hat{z}$$

which is indeed the same as the total angular momentum. This is in this case to be expected as the angular momentum seen from the CM frame is $\vec{L}' = 0$ as in the CM frame the position vector and momentum vector are parallel for all four particles.

```{solution-end}
```

```{solution-start} 11.3
:class: dropdown
```
We split the kinetic energy in the kinetic energy associated with the center of mass and the kinetic energy as seen from the CM frame:

$$ E_{kin} = \frac{1}{2}MV^2 + E'_{kin}$$

Due to symmetry, the center of mass velocity is $V$.

In the CM frame, all particles rotate with $\omega$ and thus have a velocity of magnitude $v' = \omega R$. As all particles have the same mass, we have $M = 8m$. The kinetic energy is:

$$ E_{kin} = \frac{1}{2}8V^2 + 8 \cdot \frac{1}{2}m \omega^2 R^2 = 4mV^2 +4mR^2 \omega^2$$

```{solution-end}
```

```{solution-start} 11.4
:class: dropdown
```
All nitrogen molecules feel gravity and have interaction with each other and with the wall of the container. If we write down the equation of motion for all molecules (labelled $i$) and the container we get:

$$\begin{split}
M_c \ddot{\vec{x}_c} &= M_c \vec{g} + \sum_i \vec{F}_{molecule \; i \; on \; vessel \; wall} \\
m_i \ddot{\vec{x}_i} & = -m_i \vec{g} + \vec{F}_{ vessel \; wall \;on \; molecule \; i} +\sum_{j\neq i} \vec{F}_{ji}
\end{split}$$

with $\vec{F}_{molecule \; i \; on \; vessel \; wall}$ the force of molecule $i$ on the vessel wall and $\vec{F}_{ji}$ the force from molecule $j$ on molecule $i$. All these forces are internal forces and when summing over all particles (including the vessel) will cancel each other as they all obey N3.

Thus is we add the equations, we find:

$$\frac{d}{dt} \left ( M_c \dot{\vec{x}_c} + \sum_i m_i \dot{\vec{x}_i} \right ) = \left ( M_c + \sum m_i\right ) \vec{g}$$

On the left side, we recognize the total momentum which we can write in terms of the center of mass: $M_c \dot{\vec{x}_c} + \sum_i m_i \dot{\vec{x}_i} = M\vec{V}$.

And on the right hand side we see the total mass $M = M_c + \sum m_i$. 

Thus, we conclude:

$$M\dot{\vec{V}} = M\vec{g} \rightarrow \dot{V} = -g$$ 
The entire container drops with acceleration $-g$.
```{solution-end}
```

```{solution-start} 11.5
:class: dropdown
```

```{figure} images/Dustparticles_animation.gif

---
name: fig:Dustparticles_animation.gif
width: 350px
align: center
---
30 particles: left motion of the center of mass, right motion of all particles.
```


```{solution-end}
```