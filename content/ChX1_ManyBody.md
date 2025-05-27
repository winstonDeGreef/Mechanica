## Many-Body System

We have seen that we could reduce the two-body problem of sun-earth to a single body question via the concept of reduced mass. But that this strategy does not work for 3, 4, 5, ... bodies.

### Linear Momentum

We can, however, find some basic features of $N$-body problems. In the figure, a collection of $N$ interacting particles is drawn.

```{figure} images/ManyParticles.jpg
:label: fig:ManyParticles.jpg
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

### Center of Mass

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

### Energy

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

### Angular Momentum

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

