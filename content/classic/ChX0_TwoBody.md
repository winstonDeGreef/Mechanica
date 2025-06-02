# Two Body Problem: Kepler revisited

Newton must have realized that his analysis of the Kepler laws was not 100% correct. After all, the sun is not fixed in space and even though its mass is much larger than any of the planets revolving it, it will have to move under the influence of the gravitational force by the planets. Take for example, the sun and earth as our system. By the account of Newton's third law, the Earth exerts also a force on the Sun. Therefore, the Sun has to move as well; thus, we must revisit the Earth-Sun analysis and incorporate that the Sun isn't fixed in space.  


```{figure} ../images/TwoParticles.png
:label: fig:TwoParticles
:width: 250px
:align: center

Two-particle system, with an action/reaction pair of forces.
```

The *two-body problem* is stated hereby as:

Particle $m_1$ feels an external force $\vec{F}_1$ and an interaction force from particle two, $\vec{F}_{21}$. Similarly for particle $m_2$: it feels an external force $\vec{F}_2$ and an interaction force from particle one, $\vec{F}_{12}$.

Consider the situation in the figure:

$$
m_1 \ddot{\vec{x}}_1 = \vec{F}_1 + \vec{F}_{21}
$$

$$
m_2 \ddot{\vec{x}}_2 = \vec{F}_2 + \vec{F}_{12}
$$

Add the two equations and use N3: $\vec{F}_{12} = - \vec{F}_{21}$:

$$
m_1 \ddot{\vec{x}}_1 + m_2 \ddot{\vec{x}}_2 = \vec{F}_1 + \vec{F}_{2} \Leftrightarrow
$$

$$
\dot{\vec{P}} = \vec{F}_{1} + \vec{F}_2
$$

with $\vec{P} \equiv \vec{p}_1 + \vec{p}_2$. In words, it is as if a particle with (total) momentum $\vec{P}$ responds to the external forces but does not react to internal forces (the mutual interaction).

## Center of Mass

It is now logical to assign the total mass $M=m_1+m_2$ to this fictitious particle. It has momentum $\vec{p}_1+\vec{p}_2$ which we can also couple to its mass $M$ and assign a velocity $\vec{V}$ to it such that $\vec{P}=M\vec{V}$. Furthermore, if this fictitious mass has velocity $\vec{V}$, we can also assign a position to it. After all, $\vec{V} = \frac{d\vec{R}}{dt}$, which gives us the recipe for the position $\vec{R}$.

Its velocity $\vec{V}$ and position $\vec{R}$ then follow as:

$$
\begin{split}
\vec{V} &= \frac{m_1 \vec{v}_1 + m_2 \vec{v}_2 }{m_1 + m_2} \\
&= \frac{m_1 \frac{d\vec{x}_1}{dt} + m_2 \frac{d\vec{x}_2}{dt} }{m_1 + m_2}\\
\\
\Rightarrow \vec{R} &= \frac{m_1 \vec{x}_1 + m_2 \vec{x}_2}{m_1 + m_2} +\vec{C}
\end{split}
$$

In the last equation, we have an integration constant in the form of a vector, $\vec{C}$. We are free to choose it as we want: its precise value does not affect the velocity $\vec{V}$ nor the momentum $\vec{P}$ of our fictitious particle. 

It makes sense, to choose: $\vec{C} = 0$ and thus define as position of the particle:

$$ \vec{R} = \frac{m_1 \vec{x}_1 + m_2 \vec{x}_2}{m_1 + m_2} $$

Why?

We have a few arguments: 
1)  if the particles are actually each half of a real particle, we obviously require that $\vec{R}$ is the position of the real particle.
2)  If the particles are separate by a small distance, we would like to have the fictitious particle somewhere in between the two. Moreover, if the two particles are identical, it makes sense to have the fictitious particle right in between them: the system is symmetric.

Where, in general is the position $\vec{R}$?    That can be easily seen from the figure below.

```{figure} ../images/CM_r1r2.png
:label: fig:TCM_r1r2.png
:width: 350px
:align: center

Center of Mass and relative coordinates.
```

We rewrite the definition of $\vec{R}$:

$$ \vec{R} \equiv \frac{m_1 \vec{x}_1 + m_2 \vec{x}_2}{m_1 + m_2} = \vec{x}_1 + \frac{m_2}{m_1 + m_2} \left ( \vec{x}_2 - \vec{x}_1\right )$$

Thus, the last part of the above equation tells us: first go to $m_1$ and then, 'walk' a fraction $\frac{m_2}{m_1 + m_2} $ of the line connecting $m_1$ and $m_2$. If you have done that, you are at position $\vec{R}$.  
Note: if $m_1 = m_2$ this recipe indeed brings us right between the two particles.  
Further note: the position of $M$ is always on the line from $m_1$ to $m_2$. If $m_1$ is much larger than $m_2$, it will be located close to $m_1$ and vice versa. 

We call this position the **center of mass**, or CM for short. Reason: if we look at the response of our two particle system to the forces, it is as if there is a particle $M$ at position $\vec{R}$ that has all the momentum of the system.


It turns out to be convenient to define relative coordinates with respect to the center of mass position (see also the figure above):

$$
\vec{r}_1 \equiv \vec{x}_1 - \vec{R} \text{ and } \vec{r}_2 \equiv \vec{x}_2 - \vec{R}
$$

Via the external forces, we can 'follow' the motion of the center of mass position, i.e. $\vec{R}$. From the CM as new origin, we can find the position of the two particles.

A helpful rule is found from:

$$
\begin{array}{l}
            m_1 \vec{r}_1 + m_2 \vec{r}_2 = \\
            =m_1 \left ( \vec{x}_1 - \vec{R} \right ) + m_2 \left ( \vec{x}_2 - \vec{R} \right ) \\
            =m_1  \vec{x}_1 + m_2 \vec{x}_2 - (m_1 + m_2 ) \vec{R} = 0
            \end{array}
$$

$$
\Rightarrow m_1 \vec{r}_1 + m_2 \vec{r}_2 = 0 
$$

This has an important consequence: if we know $\vec{r}_1$, we know $\vec{r}_2$, and vice versa. Note: the directions of $\vec{r}_1$ and $\vec{r}_2$ are always opposed and the center of mass $\vec{R}$ is located somewhere on the connecting line between $m_1$ and $m_2$.

Note 2: in the case of no external forces $\vec{F}_1=\vec{F}_2=0$ and only internal forces $\vec{F}_{12} \neq 0$ the CM moves according to N1 with constant velocity $(\dot{\vec{P}}=0)$.

## Energy

In terms of relative coordinates, we can write the kinetic energy as a part associated with the CM and a part that describes the kinetic energy with respect to the CM, i.e., 'an internal kinetic energy.'

$$
\begin{array}{rcl}
            E_{kin} &\equiv &\frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 \\
                    &= &\frac{1}{2} m_1 \left ( \dot{\vec{r}}_1 + \dot{\vec{R}} \right )^2 + \frac{1}{2} m_2 \left ( \dot{\vec{r}}_2 + \dot{\vec{R}} \right )^2 \\
                    &= &\frac{1}{2} M \dot{\vec{R}}^2 + \frac{1}{2} m_1 \dot{\vec{r}}_1^2 + \frac{1}{2} m_2 \dot{\vec{r}}_2^2
            \end{array}
$$

For the potential energy, we may write:

$$
V = \sum V_i + \frac{1}{2} \sum_{i \neq j} \left ( V_{ij} + V_{ji} \right )
$$

With $V_i$ the potential related to the external force on particle $i$ and $V_{ij}$ the potential related to the mutual interaction force from particle $i$ exerted on particle $j$ (assuming that all forces are conservative).

## Angular Momentum

The total angular momentum is, like the total momentum, defined as the sum of the angular momentum of the two particles:

$$
\vec{L} = \vec{l}_1 + \vec{l}_2 = \vec{x}_1 \times \vec{p}_1 + \vec{x}_2 \times \vec{p}_2
$$

We can write this in the new coordinates:

$$
\vec{L} = \vec{R} \times \vec{P} + \vec{r}_1 \times \vec{p}_1 + \vec{r}_2 \times \vec{p}_2 = \vec{L}_{cm} + \vec{L}'
$$

We find: that the total angular momentum can be seen as the contribution of the CM and the sum of the angular momentum of the individual particles as seen from the CM.

## Reduced Mass

Suppose that there are no external forces. Then the equation of motion for both particles reads as:

$$
\begin{array}{rcl}
          m_1 \ddot{\vec{x}_1} &= & \vec{F}_{12}\\
          m_2 \ddot{\vec{x}_2} &= & \vec{F}_{21} = -\vec{F}_{12}
          \end{array}
$$

If we divide each equation by the corresponding mass and subtract one from the other we get:

$$
\frac{d^2}{dt^2} ( \vec{x}_1 - \vec{x}_2 ) = \left ( \frac{1}{m_1} + \frac{1}{m_2} \right ) \vec{F}_{12}
$$

Note that the interaction force $\vec{F}_{12}$ is a function of the relative position of the particles, i.e., $\vec{x}_1 - \vec{x}_2 = \vec{r}_1 - \vec{r}_2$.

Introduce $\vec{r}_{12} \equiv \vec{r}_1 - \vec{r}_2 = \vec{x}_1 - \vec{x}_2$, then we obtain:

$$
\frac{d^2}{dt^2}  \vec{r}_{12}  = \left ( \frac{1}{m_1} + \frac{1}{m_2} \right ) \vec{F}_{12}(\vec{r}_{12})
$$

As a final step, we introduce the *reduced mass* $\mu$:

$$
\frac{1}{\mu} \equiv \frac{1}{m_1} + \frac{1}{m_2} \Leftrightarrow \mu = \frac{m_1 m_2}{m_1 + m_2} 
$$

And we can reduced the two-body problem to a single-body problem, by writing down the equation of motion for an imaginary particle with reduced mass.
 
$$
\mu \frac{d^2 \vec{r}_{12}}{dt^2} = \vec{F}_{12}  
$$

If $m_1 \gg m_2 $ we have $\mu \rightarrow m_2$. This is not surprising: when $m_1$ is much larger than $m_2$, it will look like $m_1$ is not changing its velocity at all. Or seen from the CM: is appears to be not moving. In this case, we can ignore particle 1 and replace it by a force coming out of a fixed position.

### Back to the Two-Body Problem

Once we solved the problem for the reduced mass, it is straightforward to go back to the two particles. It holds that:

$$
m_1 \vec{r}_1 + m_2 \vec{r}_2 = 0 
$$

$$
\vec{r}_2 = - \frac{m_1}{m_2} \vec{r}_1 \quad\&\quad
\vec{r}_2 = \vec{r}_1 - \vec{r}_{12}
$$

$$
\begin{array}{rcl}
          \vec{r}_1 &= &\frac{m_1}{m_1 + m_2} \vec{r}_{12} \\
          \vec{r}_2 &= &-\frac{m_1}{m_1 + m_2} \vec{r}_{12}
          \end{array} 
$$

Thus, if we have solved the motion of the reduced particle, then we can quickly find the motion of the two individual particles (seen from the CM frame).


## Kepler Revisited


```{figure} ../images/KeplerRevisited.png
:label: fig:KeplerRevisited.png
:width: 350px
:align: center

Kepler revisited.
```


Now that we have seen how to deal with the two-body problem, we can return to the motion of the Earth around the Sun. This is obviously not a two-body problem, but a many-body problem with many planets.

However, we can approximate it to a two-body problem: we ignore all other planets and leave only the Sun and Earth. Hence, there are no external forces. Consequently, the CM of the Earth-Sun system moves at a constant velocity. And we can take the CM as our origin.

We have to solve the reduced mass problem to find the motion of both the Earth and the Sun:

$$
\mu \frac{d^2 \vec{r}_{12}}{dt^2} = -\frac{Gm_e m_s}{r_{12}^2} \hat{r}_{12}
$$

Note: this equation is almost identical to the original Kepler problem. All that happened is that $m_e$ on the left hand side got replaced by $\mu$.

Everything else remains the same: the force is still central and conservative, etc.

### Where is the CM located?


```{figure} ../images/EarthSunCoG.png
:label: fig:EarthSunCoG.png
:width: 250px
:align: center

Position of CM in the sun-earth system.
```


We can easily find the center of mass of the Earth-Sun system. Chose the origin on the line through the Sun and the Earth (see fig.)

<br/>

$$
R = \frac{m_s x_s + m_e x_e }{m_s + m_e} = x_s + \frac{m_e}{m_s + m_e} (x_e - x_s)\approx x_s + 450km
$$

In other words: the Sun and Earth rotate in an ellipsoidal trajectory around the center of mass that is 450 km out of the center of the Sun. Compare that to the radius of the Sun itself: $R_s = 7 \cdot 10^5$ km. No wonder Kepler didn't notice. The common CM and rotation point is called [Barycenter](https://en.wikipedia.org/wiki/Barycenter) in astronomy.

### Exoplanets

However, in modern times, this slight motion of stars is a way of trying to find orbiting planets around distant stars. Due to this small ellipsoidal trajectory, sometimes a star moves away from us, and sometimes it comes towards us. This moving away and towards us changes the apparent color of the light emission of molecules or atoms by the [Doppler effect](doppler.md). This is a periodic motion, which lasts a 'year' of that solar system. Astronomers started looking out for periodic changes in the apparent color of the light of stars. One can also look for periodic changes in the brightness of a star (which is much, much harder than looking at spectral shifts of the light). If a planet is directly between the star and us, the intensity of the starlight decreases a bit. And they found one, and another one, and more and hundreds... Currently, more than [5,000 exoplanets](https://exoplanets.nasa.gov/) have been found.

* Changing color of star light due to a period motion induced by a planet orbiting the star ([movie from NASA ](https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/#/1)).



```{figure} ../images/radial_velocity.mp4
:width: 80%

with figure from nasa
```
         
```{figure} ../images/transit_method_single_planet.mp4
:width: 80%

from nasa
```



```{figure} ../images/RadialVelocity.png
:label: fig:RadialVelocity.jpg
:width: 350px
:align: center

Finding planets via periodic changes in the velocity of a star (from NASA).
```


* Changing intensity of star light due to a period passage of a planet orbiting the star ([(movie from NASA](https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/#/2)).


```{iframe} https://exoplanets.nasa.gov/5_ways_content/vid/transit_method_single_planet.mp4

video from nasa, does it work?
```

<a href="movies/TransientMethodSinglePlanet.mp4">

```{figure} ../images/TransientMethodSinglePlanet.png
:label: fig:RadialVelocity.jpg
:width: 350px
:align: center

Finding planets via a periodic change in intensity of a star (from NASA).
```
</a>


* Changing intensity of star light due to a period passage of more than one planet orbiting the star ([movie from NASA](https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/#/2)).

<a href="movies/TransientMethodMultiplePlanets.mp4">
 <!-- linking movies this way does not work in Jupyter Book-->
 <!-- movies can be embedded when they are located in _static folder -->
 <!-- movies are also not in the movies folder -->

```{figure} ../images/TransientMethodMultiplePlanets.png

:width: 350px
:align: center

Finding multiple planets via a change in intensity of a star (from NASA).
```
</a>


### Exercises

```{exercise}
:label: 10.1

In the table below, the mass and distance from the sun of the planets in our solar system are given (in terms of the earth mass and distance from the earth to the sun). Compute for each planet-sun pair the distance from the center of mass to the center of the sun.
Given: distance CM to center of sun for the earth-sun system is 450km.
<table align="center">
        <tr>
                <td>planet</td><td>relative mass</td><td>relative distance to the sun</td>
        </tr>
        <tr>
                <td>Mercurius</td><td align="right">0.06</td><td align="right">0.39</td>
        </tr>
        <tr>
                <td>Venus</td><td align="right">0.82</td><td align="right">0.72</td>
        </tr>
        <tr>
                <td>Earth</td><td align="right">1.00</td><td align="right">1.00</td>
        </tr>
        <tr>
                <td>Mars</td><td align="right">0.11</td><td align="right">1.52</td>
        </tr>
        <tr>
                <td>Jupiter</td><td align="right">317.8</td><td align="right">5.20</td>
        </tr>
        <tr>
                <td>Saturnus</td><td align="right">095.2</td><td align="right">9.54</td>
        </tr>
        <tr>
                <td>Uranus</td><td align="right">14.6</td><td align="right">19.22</td>
        </tr>
        <tr>
                <td>Neptunus</td><td align="right">17.2</td><td align="right">30.06</td>
        </tr>
</table>


```

```{exercise}
:label: 10.2


Two particles $m_1 = m$ and $m_2 = 2m$ are traveling both along the $x$-axis. At $t=0$ the particles have both velocity $v_0>0$. Their positions at $t=0$ are $x_1(0) = x_{10}$ and $x_2(0) = x_{20}$ with $x_{10}<x_{20}$.  They repel each other with a force $F_r = \frac{k}{(x_2-x_1)^2}$. Moreover, a constant external force $F_e$ is acting on them. The problem is 1-dimensional.

* Find the velocity of the center of mass for $t>0$
* Find the position of the center of mass for $t>0$.


```

```{exercise}
:label: 10.3


Two particles $m_1$ = 3kg and $m_2$ = 2kg are connected via a massless rod of length $L$=50cm.

* Find the position of the center of mass of the system, measured from $m_1$
* Calculate the reduced mass of the two-particle system.

```

```{exercise}
:label: 10.4


Two bumper cars are approaching each other in a straight line. The two cars will collide head-on. The mass of car 1 (including the driver) is 200 kg, that of car 2 300kg. Car 1 has a velocity of 8m/s; car 2 of -4m/s.

* What is the velocity of the center of mass of the system?
* What is the reduced mass of the system?
* Transform the velocities of both carts to the center-of-mass frame.

```

```{exercise}
:label: 10.5

Two carts on a frictionless track move toward each other:

Cart 1: mass $m_1$ = 2kg, velocity $v_1$ = 4m/s   
Cart 2: mass $m_2$ = 3kg, velocity $v_2$ = -2m/s 
* What is the total kinetic energy in the lab frame?
* What is the velocity of the center of mass?
* What is the total kinetic energy in the center-of-mass frame?
* Verify that the CM frame kinetic energy equals the kinetic energy due to relative motion using the reduced mass.

```

### Answers

```{solution} 10.1
:class: dropdown

<table align="center">
        <tr>
                <td>planet</td><td>relative mass</td><td>relative distance to the sun</td><td>distance CM to center of sun (km)</td>
        </tr>
        <tr>
                <td>Mercurius</td><td align="right">0.06</td><td align="right">0.39</td><td align="right">10</td>
        </tr>
        <tr>
                <td>Venus</td><td align="right">0.82</td><td align="right">0.72</td><td align="right">265</td>
        </tr>
        <tr>
                <td>Earth</td><td align="right">1.00</td><td align="right">1.00</td><td align="right">450</td>
        </tr>
        <tr>
                <td>Mars</td><td align="right">0.11</td><td align="right">1.52</td><td align="right">75</td>
        </tr>
        <tr>
                <td>Jupiter</td><td align="right">317.8</td><td align="right">5.20</td><td align="right">$743 \cdot 10^3$</td>
        </tr>
        <tr>
                <td>Saturnus</td><td align="right">095.2</td><td align="right">9.54</td><td align="right">$409 \cdot 10^3$</td>
        </tr>
        <tr>
                <td>Uranus</td><td align="right">14.6</td><td align="right">19.22</td><td align="right">$126 \cdot 10^3$</td>
        </tr>
        <tr>
                <td>Neptunus</td><td align="right">17.2</td><td align="right">30.06</td><td align="right">$234 \cdot 10^3$</td>
        </tr>
</table>

```

```{solution} 10.2
:class: dropdown

We set up the equation of motion for the particles:

$$\begin{split}
m_1: m_1 \dot{v}_1 &= F_e - F_r \\
m_1: m_2 \dot{v}_2 &= F_e + F_r 
\end{split}$$

Add these two equations:

$$M\dot{V} = m_1 \dot{v}_1 + m_2 \dot{v}_2 = 2F_e \rightarrow \dot{V} = \frac{2F_e}{m_1+m_2} = \frac{2F_e}{3m}$$

As expected, we see that the repelling mutual force has no effect on the center of mass.
We can solve this equation, using the initial condition the $MV(0) = m_1v_1(0) + m_2 v_2(0) \rightarrow V(0) = \frac{mv_0 + 2mv_0}{m+2m} = v_0$

$$V(t) = \frac{2F_e}{3m} t + C_1 = \frac{2F_e}{3m} t + v_0$$

As the next step we calculate $R(t)$:

$$\dot{R} \equiv V = v_0 + \frac{2F_e}{3m} t \rightarrow R(t) = v_0 t + \frac{F_e}{3m} t^2 + C_2$$

The initial condition is: $R(0) = \frac{m_1 x_1(0) + m_2 x_2(0)}{m_1+m_2} = \frac{1}{3}x_{10} + \frac{2}{3}x_{20}$.

This gives

$$R(t) = \frac{1}{3}x_{10} + \frac{2}{3}x_{20} + v_0 t + \frac{F_e}{3m} t^2$$

```

```{solution} 10.3
:class: dropdown

The center of mass of two point masses is on the line connecting $m_1$ and $m_2$. We denote this line as the $x$-axis, with $m_1$ as the origin.

* The center of mass is than given by (with $m_1$ = 3kg, $m_2$ = 2kg, $x_1$=0 and $x_2 = x_1 + L$ = 0.5m):

$$x_{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = 0.2m$$

* The reduced mass is given by:

$$\mu \equiv \frac{m_1 m_2}{m_1 + m_2} = \frac{6}{5} kg$$

```

```{solution} 10.4
:class: dropdown

This is a 1-dimensional problem.

* The velocity of the center of mass is:

$$V_{cm} = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2} = \frac{4}{5}m/s$$

* The reduced mass is given by:

$$\mu \equiv \frac{m_1 m_2}{m_1 + m_2} = 120 kg$$

* In the CM frame the velocities of the cars are:

$$\begin{split}
v_1' & = v_1 - V_{cm} = 7.2m/s \\
v_2' & = v_2 - V_{cm} = -4.8m/s
\end{split}$$

```

```{solution} 10.5
:class: dropdown

Cart 1: mass $m_1$ = 2kg, velocity $v_1$ = 4m/s   
Cart 2: mass $m_2$ = 3kg, velocity $v_2$ = -2m/s 
* The total kinetic energy in the lab frame is

$$E_{kin} = \frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2 = 22 J$$

* The velocity of the center of mass is

$$ V_{cm} \equiv \frac{m_1v_1 + m_2 v_2}{m_1 + m_2} = 0.4 m/s$$

* The total kinetic energy in the center-of-mass frame is

$$ E_{kin,CM} = \frac{1}{2}m_1v_1'^2 + \frac{1}{2}m_2v_2'^2$$ 

with

$$\begin{split}
v_1' &= v_1 - V_{cm} = 3.6 m/s \\
v_2' &= v_2 - V_{cm} = -2.4 m/s
\end{split}$$

Thus

$$ E_{kin,CM} = 21.6 J$$

* The reduced mass is

$$\mu \equiv \frac{m_1 m_2}{m_1 + m_2} = 1.2 kg $$

The relative velocity is

$$ v_{rel} \equiv v_1 - v_2 = 6 m/s $$

The kinetic energy associated with the motion of the reduced mass (i.e. the kinetic energy in the CM frame) is:

$$ E_{kin, rel} \equiv \frac{1}{2} \mu v_{rel}^2 = 21.6J $$

as we expected.

```

## Many-Body System

We have seen that we could reduce the two-body problem of sun-earth to a single body question via the concept of reduced mass. But that this strategy does not work for 3, 4, 5, ... bodies.

### Linear Momentum

We can, however, find some basic features of $N$-body problems. In the figure, a collection of $N$ interacting particles is drawn.

```{figure} ../images/ManyParticles.png
:label: fig:ManyParticles.png
:width: 150px
:align: center

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

### Exercises

```{exercise-start}
:label: ex11.1
```
Thee masses are forming an equilateral triangle with sides of 2m. Mass 1 (10kg) is positioned at $(x_1,y_1) = (-1m,0))$. Mass 2 (6kg) is at $(x_2,y_2) = (1m,0))$, while mass 3 (2kg) is at $(x_3,y_3) = (0,\sqrt{3})$.

* Calculate the position of the center of mass.

```{exercise-end}
```

```{exercise-start}
:label: 11.2
```
Four particles are moving over the line $y=y_0$. The particles have mass $m_1 = 4m, m_2 = 3m, m_3 = 2m, m_4 = m$ and velocity $v_1 = v, v_2 = 2v, v_3 = 3v, v_4 = 4v$. These velocities are constant and parallel to the $x$-axis. At $t=0$ all particles are at location $(x,y) = (0,y_0)$.

```{figure} ../images/FourParticles.png
:label: fig:FourParticles.png
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

```{figure} ../images/Wheel8Masses.png
:label: fig:Wheel8Masses.png
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

### Answers

```{solution-start} ex11.1
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

```{figure} ../images/FourParticlesVectors.png
:label: fig:FourParticlesVectors.png
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

```{figure} ../images/Dustparticles_animation.gif

:label: fig:Dustparticles_animation.gif
width: 350px
align: center
---
30 particles: left motion of the center of mass, right motion of all particles.
```


```{solution-end}
```

