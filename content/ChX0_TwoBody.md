# Two Body Problem: Kepler revisited #

Newton must have realized that his analysis of the Kepler laws was not 100% correct. After all, the sun is not fixed in space and even though its mass is much larger than any of the planets revolving it, it will have to move under the influence of the gravitational force by the planets. Take for example, the sun and earth as our system. By the account of Newton's third law, the Earth exerts also a force on the Sun. Therefore, the Sun has to move as well; thus, we must revisit the Earth-Sun analysis and incorporate that the Sun isn't fixed in space.  


```{figure} images/TwoParticles.jpg
---
name: fig:TwoParticles
width: 250px
align: center
---
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

It is now logical to assign the total mass $M=m_1+m_2$ to this fictitious particle. It has momentum $\vec{p}_1+\vec{p}_2$ which we can also couple to its mass $M$ and assign a velocity $\vec{V}$ to it such that $\vec{P}=M\vec{V}$. Furthermore, if this fictitious mass has velocity $\vec{V}$, we can also assign a position to it. Afterall, $\vec{V} = \frac{d\vec{R}}{dt}$, which gives us the recipe for the position $\vec{R}$.

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

Where, in general is the position $\vec{R}$? <br> That can be easily seen from the figure below.

```{figure} images/CM_r1r2.png
---
name: fig:TCM_r1r2.png
width: 350px
align: center
---
Center of Mass and relative coordinates.
```

We rewrite the definition of $\vec{R}$:

$$ \vec{R} \equiv \frac{m_1 \vec{x}_1 + m_2 \vec{x}_2}{m_1 + m_2} = \vec{x}_1 + \frac{m_2}{m_1 + m_2} \left ( \vec{x}_2 - \vec{x}_1\right )$$

Thus, the last part of the above equation tells us: first go to $m_1$ and then, 'walk' a fraction $\frac{m_2}{m_1 + m_2} $ of the line connecting $m_1$ and $m_2$. If you have done that, you are at position $\vec{R}$.<br>
Note: if $m_1 = m_2$ this recipe indeed brings us right between the two particles.<br>
Further note: the position of $M$ is always on the line from $m_1$ to $m_2$. If $m_1$ is much larger than $m_2$, it will be located close to $m_1$ and vice versa. 

We call this position the <b>center of mass</b>, or CM for short. Reason: if we look at the response of our two particle system to the forces, it is as if there is a particle $M$ at position $\vec{R}$ that has all the momentum of the system.


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


```{figure} images/KeplerRevisited.jpg
---
name: fig:KeplerRevisited.jpg
width: 350px
align: center
---
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


```{figure} images/EarthSunCoG.jpg
---
name: fig:EarthSunCoG.jpg
width: 250px
align: center
---
Position of CM in the sun-earth system.
```


We can easily find the center of mass of the Earth-Sun system. Chose the origin on the line through the Sun and the Earth (see fig.)

<br/>

$$
R = \frac{m_s x_s + m_e x_e }{m_s + m_e} = x_s + \frac{m_e}{m_s + m_e} (x_e - x_s)\approx x_s + 450km
$$

In other words: the Sun and Earth rotate in an ellipsoidal trajectory around the center of mass that is 450 km out of the center of the Sun. Compare that to the radius of the Sun itself: $R_s = 7 \cdot 10^5$ km. No wonder Kepler didn't notice. The common CM and rotation point is called <a href="https://en.wikipedia.org/wiki/Barycenter">Barycenter</a> in astronomy.

### Exoplanets

However, in modern times, this slight motion of stars is a way of trying to find orbiting planets around distant stars. Due to this small ellipsoidal trajectory, sometimes a star moves away from us, and sometimes it comes towards us. This moving away and towards us changes the apparent color of the light emission of molecules or atoms  by the [Doppler effect](doppler.md). This is a periodic motion, which lasts a 'year' of that solar system. Astronomers started looking out for periodic changes in the apparent color of the light of stars. One can also look for periodic changes in the brightness of a star (which is much, much harder than looking at spectral shifts of the light). If a planet is directly between the star and us, the intensity of the starlight decreases a bit. And they found one, and another one, and more and hundreds... Currently, more than <a href="https://exoplanets.nasa.gov/">5,000 exoplanets</a> have been found.

* Changing color of star light due to a period motion induced by a planet orbiting the star (<a href="https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/#/1">movie from NASA </a>).

<a href="movies/RadialVelocity.mp4">

```{figure} images/RadialVelocity.png
---
name: fig:RadialVelocity.jpg
width: 350px
align: center
---
Finding planets via periodic changes in the velocity of a star (from NASA).
```
</a>


* Changing intensity of star light due to a period passage of a planet orbiting the star (<a href="https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/#/2">(movie from NASA</a>).


<a href="movies/TransientMethodSinglePlanet.mp4">

```{figure} images/TransientMethodSinglePlanet.png
---
name: fig:RadialVelocity.jpg
width: 350px
align: center
---
Finding planets via a periodic change in intensity of a star (from NASA).
```
</a>


* Changing intensity of star light due to a period passage of more than one planet orbiting the star (<a href="https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/#/2">movie from NASA</a>).

<a href="movies/TransientMethodMultiplePlanets.mp4">
 <!-- linking movies this way does not work in Jupyter Book-->
 <!-- movies can be embedded when they are located in _static folder -->
 <!-- movies are also not in the movies folder -->

```{figure} images/TransientMethodMultiplePlanets.png
---
name: fig:RadialVelocity.jpg
width: 350px
align: center
---
Finding multiple planets via a change in intensity of a star (from NASA).
```
</a>


### Exercises ###

```{exercise-start}
:label: 10.1
```
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

```{exercise-end}
```

```{exercise-start}
:label: 10.2
```

Two particles $m_1 = m$ and $m_2 = 2m$ are traveling both along the $x$-axis. At $t=0$ the particles have both velocity $v_0>0$. Their positions at $t=0$ are $x_1(0) = x_{10}$ and $x_2(0) = x_{20}$ with $x_{10}<x_{20}$.  They repel each other with a force $F_r = \frac{k}{(x_2-x_1)^2}$. Moreover, a constant external force $F_e$ is acting on them. The problem is 1-dimensional.

* Find the velocity of the center of mass for $t>0$
* Find the position of the center of mass for $t>0$.


```{exercise-end}
```

```{exercise-start}
:label: 10.3
```

Two particles $m_1$ = 3kg and $m_2$ = 2kg are connected via a massless rod of length $L$=50cm.

* Find the position of the center of mass of the system, measured from $m_1$
* Calculate the reduced mass of the two-particle system.

```{exercise-end}
```

```{exercise-start}
:label: 10.4
```

Two bumper cars are approaching each other in a straight line. The two cars will collide head-on. The mass of car 1 (including the driver) is 200 kg, that of car 2 300kg. Car 1 has a velocity of 8m/s; car 2 of -4m/s.

* What is the velocity of the center of mass of the system?
* What is the reduced mass of the system?
* Transform the velocities of both carts to the center-of-mass frame.

```{exercise-end}
```

```{exercise-start}
:label: 10.5
```
Two carts on a frictionless track move toward each other:

Cart 1: mass $m_1$ = 2kg, velocity $v_1$ = 4m/s <br>
Cart 2: mass $m_2$ = 3kg, velocity $v_2$ = -2m/s 
* What is the total kinetic energy in the lab frame?
* What is the velocity of the center of mass?
* What is the total kinetic energy in the center-of-mass frame?
* Verify that the CM frame kinetic energy equals the kinetic energy due to relative motion using the reduced mass.

```{exercise-end}
```

### Answers ###

```{solution-start} 10.1
:class: dropdown
```

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

```{solution-end}
```

```{solution-start} 10.2
:class: dropdown
```
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

```{solution-end}
```

```{solution-start} 10.3
:class: dropdown
```
The center of mass of two point masses is on the line connecting $m_1$ and $m_2$. We denote this line as the $x$-axis, with $m_1$ as the origin.

* The center of mass is than given by (with $m_1$ = 3kg, $m_2$ = 2kg, $x_1$=0 and $x_2 = x_1 + L$ = 0.5m):

$$x_{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2} = 0.2m$$

* The reduced mass is given by:

$$\mu \equiv \frac{m_1 m_2}{m_1 + m_2} = \frac{6}{5} kg$$

```{solution-end}
```

```{solution-start} 10.4
:class: dropdown
```
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

```{solution-end}
```

```{solution-start} 10.5
:class: dropdown
```
Cart 1: mass $m_1$ = 2kg, velocity $v_1$ = 4m/s <br>
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

```{solution-end}
```

## Rutherford & the atom ##

### Atomic theory ###
The idea that matter is made of atoms is old. However, the notion of atoms as we have now is relatively young. 

In the ancient Greek world, it was as early as the fifth century B.C. that Leucippus and later one of his pupils Democritus proposed that the world, i.e. matter, is made up of tiny, indivisible particles -which he called atoms, derived from the Greek word 'atomos', which means uncuttable. These particles float in a vacuum, that was called void by Democritus. We currently have a view that is remarkably close, but at the same time quite different from these first ideas.

In ancient India even earlier (records go back to the eighth' century B.C.) philosophers like Uddalaka Aruni talk about matter being made up of tiny particles. They did not use terms like atoms, but instead referred to the 'building blocks' of matter as 'kana' which means particles. In the Islamic world, atomic theories were developed in e.g. the Asharite school by Al Ghazali (1058-1111). In his thinking, atoms are the only material things that live forever. Everything else, any event or interaction is due to God's intervention.

Although these early thoughts point at atoms as the underlying elements of matter and as such resemble our current understanding of matter, they also differ quite a bit. The early ideas are based on philosophy and the notion that matter is either a continuum that can always be cut in smaller parts that still maintain all characteristics or that at some point a further splitting in smaller pieces is no longer possible with at least losing some of the characteristics.

In more recent history, the notion of atoms as elementary building blocks is guided by experiments. The English physicist and chemist John Dalton (1766-1844) did ground braking work. For instance, he noticed that water, when decomposed, always resulted in the same elements: hydrogen and oxygen. Moreover, the relative weights of these two was always the same. Furthermore, he came to the conclusion that there is a uniques atom for each element. More chemists noted that many substances were made of the elements in very specific ratio's. In our modern view we would say: water is formed in a 1 to 2 ratio of oxygen and hydrogen, never in 1 to 2.1 or any other non-integer number. 

Although the evidence from chemistry was clear, the notion of atoms as the building blocks remained controversial. One generally accepted the laws of definite proportion (e.g. water is decomposed in a fixed ratio in hydrogen and oxygen), but the hypothesis that everything was made of atoms was not. As a consequence, the work of Ludwig Boltzmann (1844-1906) on statistical thermodynamics that is entirely based on an atomic (or molecular) view was not accepted during Boltzmann's life.

In the second half of the nineteenth century William Thomson (1824-1907) -later Lord Kelvin- proposed the so-called vortex theory of the atom. Based on the discoveries by chemists of only a few different atoms that made up the rest of matter, Thomson proposed that atoms are stable vortices, not in an ordinary fluid like water, but in the omni-present luminiferous aether. 

Stable vortices have the shape of rings with no beginning or end. In air they are easily made and made visible with smoke and are indeed surprisingly stable. According to the vortex theory, atoms are vortices in aether. The simplest one is a single ring, which was hydrogen. More complicated forms, called knots represented the other elements. 

<table style="border:0 ;margin-left:auto;margin-right:auto;">
<td>

```{figure} images/VortexKnots.png
---
name: fig:VortexKnots.png
width: 350px
align: center
---
Various vortex knots, each represents another element. From [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:English_for_unknot.svg), public domain.
```
</td>
<td>

```{figure} images/LordKelvin.jpg
---
name: fig:LordKelvin.jpg
width: 150px
align: center
---
Lord Kelvin (1824-1907). From [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Sir_William_Thomson,_Baron_Kelvin,_1824_-_1907._Scientist,_resting_on_a_binnacle_and_holding_a_marine_azimuth_mirror.jpg), public domain.
```

</td>
</table>

At the end of the nineteenth century, in 1897, Joseph John Thomson discovered the electron. It allowed him to further refine the scientific model of the atom and it made an end to the vortex theory. In Thomson's view, an atom had internal structure: the electrons were moving in it. As electrons have a negative charge and atoms are neutral, there must be a balancing positive charge in an atom as well. Thomson had no idea what that would be and he figured that the positive charge was everywhere in the atom (that he thought of as being a sphere), with the electrons moving inside that sphere as tiny particles. From this picture, the Thomson model got its name: the plum pudding model, although it is a bit misleading as the idea was that the positively charged sphere was more a liquid in which the electrons 'float' than a solid. 

<table style="border:0 ;margin-left:auto;margin-right:auto;">
<td>

```{figure} images/PlumPuddingModel.png
---
name: fig:PlumPuddingModel.png
width: 150px
align: center
---
Plum pudding model according to Joseph Thomson. From [Wikimedia Commons](https://simple.m.wikipedia.org/wiki/File:Plum_pudding_atom.svg), public domain.
```
</td>
<td>

```{figure} images/JJThomson.jpg
---
name: fig:JJThomson.jpg
width: 150px
align: center
---
Joseph John Thomson (1856-1940). From [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:J.J_Thomson.jpg), public domain.
```

</td>
</table>

The model did not hold very long as we will see in the next paragraph. Nevertheless, it marks the start of physicist becoming really interested in an atom theory.


### Rutherford's scattering experiment  ###
#### Introduction ####

<table style="border:0 ">
<td width="500px">
The plum pudding model was abandoned in 1911. That year Ernest Rutherford (1871-1937), a former student of Joseph Thomson, performed a ground-breaking experiment. Rutherford had been working on the newly discovered radio-activity of certain elements. He discovered that there were two types of radiation that were different from the X-rays. He called them 'alpha' and 'beta' rays and later proved that 'alpha' rays consisted of He-nuclei. Rutherford in cooperation with Frederick Soddy was the first one to prove Marie Curie's conjecture that radioactivity was an atomic phenomenon, which could lead to changes in the atom itself, from one element to another. Prior to that, the atom was seen as the ultimate, indestructible form of matter: atoms could not change from one form (element) to another.
</td>
<td>

```{figure} images/Mariecurie.jpg
---
name: fig:MarieCurie.jpg
width: 200px
align: center
---
Marie Curie (1867-1934). From [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Marie_Curie_c._1920s.jpg), public domain.
```

</td>
</table>

Rutherford in cooperation with Hans Geiger (one of the inventors of what we now call the Geiger counter) and Ernest Masden, built an apparatus that could count the alpha particles. Moreover, he could show that the alpha particles were He-nuclei with a positive charge of 2e. In 1917 he showed that Nitrogen could become Oxygen by bombarding it with the alpha particles. This was the first time that someone succeeded in artificially changing one element into another.

#### Scattering at a gold foil ####
As mentioned Rutherford is responsible for overthrowing the plum pudding model and replacing it by our modern view: an atom is made of a tiny, positively charged nucleus with the electrons orbiting around it. 

The start was formed by Rutherford's observation that some of the alpha-particles were deflected by a thin metal sheet in front of his alpha-counter. This puzzled him as the plum pudding model could not explain this. Hence, Rutherford, Geiger and Marsden set up an experiment in which they led the alpha particles scatter at a very thin gold foil. 

The Source would emit $\alpha$-particles through a small diaphragm onto the gold foil. The diaphragm made sure that all $\alpha$-particles were traveling on the same line. After moving through the gold foil, the particles could be detected by looking via a microscope at the tiny light flashes an $\alpha$-particle caused when hitting the detection screen. The microscope & detection screen could be placed under an angle with the original trajectory of the $\alpha$-particles. By measuring at all possible angles, the scattering of the $\alpha$-particles by the gold foil could be completely mapped and quantified. 


<table style="border:0 ;margin-left:auto;margin-right:auto;">
<td>

```{figure} images/RutherfordExperimentalSetup.png
---
name: fig:RutherfordExperimentalSetup.png
width: 250px
align: center
---
Experimental Setup of $\alpha$-scattering at a gold foil.
```
</td>
<td>

```{figure} images/ErnestRutherford.jpg
---
name: fig:ErnestRutherford.jpg
width: 150px
align: center
---
Ernest Rutherford (1871-1937). From [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Sir_Ernest_Rutherford_LCCN2014716719_-_restoration1.jpg), public domain.
```

</td>
</table>


The story goes, that Rutherford's students would, together with Geiger, do the measurements as an assignment of their studies. The principle is simple: set the microscope under a know angle and, for a given period in time, count the number of hits. Repeat this for the next angle of the microscope. Obviously, the first measurements where all done on the side of the foil opposite to the $\alpha$-emitter. One was expecting small deviations from the undisturbed trajectory.

When the experiments were basically done, so goes the story, still a student was left over that also needed an assignment. One of Rutherford's assistant suggested that this student would then measure with the microscope at the same side of the foil as the $\alpha$-emitter. They did not expect anything to see, but they needed an assignment for this student. Whether the story of the student assignments is true or not, fact is that the team found also hits on the detector for angles of about 180$^\circ$. That is, some $\alpha$-particles seem to bounce back from the foil!

There is no way that the plum pudding model could explain this. The argumentation to show that, goes as follows. 
<ol>
<li> The size of the atoms of gold is known: they are on the order of 

$r_0 \approx 10^{-10}$m. <br>
This value can be found from the density of gold, the mass of a gold atom and the mass and volume of the gold foil (or any other amount of gold). By treating the atoms as small spheres that are stacked back to back, the size of the atom is easily found. </li>
<li> An $\alpha$-particle has a charge of 2e and is deflected by a gold atom due to the charge of the gold atom. As gold has number 79 in the periodic table, we know that the charge of a gold atom is +79e in the 'plum pudding' and -79e of all electrons floating in the pudding.<br>
However, an $alpha$-particle is much heavier than an electron. Hence in the Coulomb interaction between the $\alpha$ -particle and an electron, the acceleration (of deflection) of the 'heavy' $\alpha$-particle is negligible: the electrons are pushed out of the way (or actually attracted); they don't influence the trajectory of the $\alpha$-particle.<br>
It is the positive charge of the pudding itself, that does the deflection. The atom (i.e. the pudding) can not move out of the way as it is part of the gold foil which is many orders of magnitude heavier than the incoming particle. <br><br>

Rutherford knew the theory of Maxwell for Electro-Magnetism and could estimate The force an $\alpha$-particle would feel from the atom. He deduced that the force on the $\alpha$-particle is always smaller than:

$$ F_c \leq \frac{q_\alpha Q_g}{4 \pi \epsilon_0} \frac{1}{r_0^2} $$ 

with $Q$ the charge of the atom (i.e. +79e), $q_\alpha$ the charge (+2e) of the $\alpha$-particle, $\epsilon_0$ the permittivity of vacuum ($\frac{1}{4 \pi \epsilon} = 9 \cdot 10^9 Nm^2/C^2$) and $r_0$ the radius of a gold atom.

The deflection of the particle is biggest if the Coulomb force is perpendicular to the trajectory. So, we take that for our estimate. The true effect, when passing through the atom, will be smaller.</li>

<li>It is easiest to compute the change of momentum. The particle comes in with a know momentum $p$. If the change in momentum 

$\Delta p$ is much smaller than $p$ itself, the deflection will be small.

```{figure} images/RutherfordDeltaP.png
---
name: fig:RutherfordDeltaP.png
width: 250px
align: center
---
Relation of angle of deflection and change in momentum.
```
$$\tan \phi = \frac{\Delta p}{p} \Rightarrow \phi \approx \frac{\Delta p}{p} \text{ if } \phi \ll 1$$
</li>
<li> The momentum change is due to the force $F_c$ working for a time period 

$\Delta t$ on the particle:

$$ dP = Fdt -\rightarrow \Delta p \approx F_c \Delta t$$

The time the particle is in the atom is estimated as follows. The particle has a velocity $v_0$ and it has to travel a distance $2r_0$ through the atom, thus $\Delta t \approx \frac{2r_0}{v_0} $. We assume that the change in momentum is small, so that we can still use $v_0$ as an estimate of the velocity with which the $\alpha$-particle travels.
</li>
<li> If we put everything together, we find:

$$ \frac{\Delta p}{p} \ll \frac{q_\alpha Q_g}{4 \pi \epsilon_0} \frac{1}{r_0^2} \cdot \frac{2r_0}{v_0} = \frac{q_\alpha Q_g}{2 \pi \epsilon_0} \frac{1}{r_0 v_0} \ll 1$$

We have used the know charge of a gold atom (79e) and that of the $\alpha$-particle, the radius of the gold atom and the incoming velocity of the $\alpha$-particle, $v_0 \approx 1.6 \cdot 10^{7}$m/s.
</li>
</ol>

With this estimate and the fact that Rutherford's gold foil was about 400 atoms thick, there is no way that we can explain $\alpha$-particles bouncing back.

Rutherford and his colleagues, had no other option than to conclude that the positive charge of the gold atom must be confined to a much smaller part of space. After all, the only parameter in our estimate that is not measured is $r_0$. That was estimated based on the plum pudding model.

They redid the calculation, but now with $r_0$ as a free parameter to be backed out of the calculation. They changed the requirement of small scattering angles (i.e. small deviation from the original path) to the experimental finding that scattering angles of about 180$^\circ$ were possible. That gave that $r_0$ is on the order of $10^{-14}$m. 

Conclusion: the atom has a nucleus that is much smaller than the size of the atom that contains all positive charge. The electrons must orbit this nucleus as a mini-solar system. These electrons 'define' the size of the atom.

```{figure} images/RutherfordAtom.png
---
name: fig:RutherfordAtom.png
width: 200px
align: center
---
Rutherford's model of an atom.
```
This new model would spark a whole new set of questions, setting up one of the biggest changes in physics: Quantum Theory.

#### Collapse of matter? ####
An immediate consequence of this new view on atoms and matter came from the analogy with Newton's work on the solar system and the Kepler Laws. In the case of the sun and planets, the interaction force is gravity: $\vec{F}_g = - G \frac{m_1 m_2}{r_{12}^2}\hat{r_{12}}$. When dealing with a nucleus with its orbiting electrons the interaction force is the Coulomb force: $ \vec{F}_C = \frac{1}{4\pi \epsilon_0} \frac{q_1 q_2}{r_{12}^2}\hat{r_{12}} $.

As both Gravity and Coulombs forces are central, conservative forces and are inversely proportional to the square of distance from the two interacting particles the motion of a 'tiny' planet around the 'massive' sun is mathematically completely analogous to that of a 'tiny' electron around its 'massive' nucleus.

Thus an electron orbits the nucleus in an ellipse. Consequently, it is in a permanent state of acceleration. However, from Maxwell's theory of Electro-Magnetism it is well known (already in the times of Rutherford as the theory of Maxwell dates back to around 1860) that accelerating charged particles radiate energy in the form of electro-magnetic waves. This means that the electron constantly looses energy and thus moves to an elliptical orbit closer to the nucleus until, eventually, its orbit collapses onto the nucleus. This process would go very fast and matter in its present form could not exist. Now we know, that the idea of an atom being a miniature solar system is wrong. But out of questions and dilemma's as these grew very quickly quantum mechanics opening a whole new world and a completely different picture of things at the small scales. A world with new rules and new consequences, where our intuition based on daily life and large scale structures composed of many, many atoms fails.

#### Scattering Theory  ####
The work of Rutherford and co-workers forms the start of a new branch of physics: nuclear physics. By using radiation in the form of X-rays (i.e. high energy photons) and electrons or protons, physicists are able to probe the internal properties of molecules, atom, nuclei and even elementary particles (or at least, what we once thought were elementary particles).

The idea is to send high energy particles towards the object of investigation and look at the scattering that is a consequence of the interaction between the object and the incoming particles. The internal structure of the object dictates the scattering. Thus, by measuring the scattering features and back tracing the underlying physical interaction can be found.

It is done with facilities of a very large scale to research particles at the smallest scales. For instance, in CERN researchers accelerate particles (protons, electrons, etc) to velocities almost the speed of light. Then, they let these particles collide, that is undergo interactions involving enormous amounts of energy, and measure the fragments and all kind of exotic particles that result from these collisions. 

```{figure} images/AirPictureOfCERN.jpg
---
name: fig:RutAirPictureOfCER.png
width: 350px
align: center
---
Circular Accelerator of CERN depicted in its environment. ESO/[José Francisco](josefrancisco.org), licensed under CC-BY 4.0.
```

The principles used in scattering can be illustrated by revisiting Rutherford's experiment. 

```{figure} images/ScatteringPrinciple.png
---
name: fig:ScatteringPrinciple.png
width: 350px
align: center
---
Scattering of an incoming particle at a fixed source.
```

Consider fig.(7.7): a particle of mass $m$ and velocity $v$ is moving towards a fixed second particle. The latter is fixed in the origin and act like a force-source. The force is central, i.e. works along the direction of the red line in fig.(7.7). In the drawing the forces is repelling and the incoming particle will deviate from its straight line. Eventually it will continue moving over a straight line, when the influence of the force is no longer felt. The angle of the new direction with the incoming one, is $\theta$, the scattering angle. We are looking for the relation between $b$, the distance at which the incoming particle would have passed by the origin if there was no force and the scattering angle $\theta$.


```{figure} images/Scattering2D3D.png
---
name: fig:Scattering2D3D.png
width: 450px
align: center
---
left: scattering in 2D, right: scattering in 3D.
```

In fig.(7.8) scattering in a 2D world and in the 3D world is schematically depicted. In the 3-dimensional world the scattering takes place in the solid angle $d\theta$. Like the 2d equivalent, where the scattering angle can go from 0 to $2\pi$ (that is the full circle), in 3d it goes from 0 to $4\pi$ reflecting that it is now a full sphere.


## Three body Problem ###

Now that we have reduced a two-particle system to a single particle problem, the question arises: can we repeat this 'trick' and turn a three-body problem in a two body problem, that in its turn can be reduced to a single particle problem?

The answer is: no. There is no general strategy to reduce a three body problem two a two body-one. 

The three body problem is an old one. Already Newton himself worked on it. Its importance stems e.g. from navigation on see. It would be of great help if the position of the moon could be predicted in advance with great accuracy. Then sailors in the 17$^{th}$, 18$^{th}$ and 19$^{th}$ could have found much better their position at full sea. But no one succeeded in providing a closed solution in basic functions. 

The king of Sweden, Oscar II, announced, as celebration of his 60$^{th}$ birthday, a competition with the price awarded to the one that came up with a general solution. But it took a different course. The price went to the French mathematician and physicist Henri Poincaré. 

```{figure} images/HenriPoincare.jpg
---
name: fig:20SolutionsThreeBodyProblem.gif
width: 250px
align: center
---
<a href="https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9"> Click here for the Wikipedia page of Poincaré.</a>
```

He showed that it was impossible to find such a solution as he reached the conclusion that the three body problem showed chaotic features. It led Poincaré to develop a whole new field: dynamic systems and what we call now *deterministic chaos*.  
The work of Poincaré was the trigger of yet another 'revolution' in our understanding of the universe. 


It doesn't mean that there are no known solutions of specific cases of the three body problem. On the contrary, in the movie below 20 solutions are given. Notice that they all have a high degree of symmetry. 

```{figure} images/20SolutionsThreeBodyProblem.gif
---
name: fig:20SolutionsThreeBodyProblem.gif
width: 350px
align: center
---
<a href="https://upload.wikimedia.org/wikipedia/commons/5/5a/5_4_800_36_downscaled.gif">Click here to see some exact solutions of the three body problem</a> (By Perosello - Uploaded by Author, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=133294338).
```


### Alpha Centauri A, Alpha Centauri B and Alpha Centauri C ###
The three body problem can also be studied by numerical means. As the equations of motion are easily set up and put into a computer code, this allows us to investigate for instance the three stars of the Alpha Centauri system: Alpha Centauri A, Alpha Centauri B and Alpha Centauri C. This system is a little over 4 million light years away from us: these stars are our closest (star) neighbors. Although they form a three body system, it is stable due to the much smaller mass op Alpha Centauri C compared to the other two. Alpha Centauri A and Alpha Centauri B are of similar mass, that is 1.1 and 0.9 the mass of our sun, respectively. Alpha Centauri C, on the other hand has a mass of only 0.12 of that of the sun.

<a href="https://towardsdatascience.com/modelling-the-three-body-problem-in-classical-mechanics-using-python-9dc270ad7767">Gaurav Deshmukh</a> has written a nice python-based web-page on this system. Below we show some examples of the simulations, that you can do yourself with the code given by Deshmukh.


First, we ignore Alpha Centauri C and used that A and B have about the same mass. The two stars start rotating around each other in ellipsoidal orbits, as we already know from the two body problem.

```{figure} images/TwoBody_animation.gif
---
name: fig:TwoBody_animation.gif
width: 320px
align: center
--- 
Alpha Centauri A and B circling each other.
```

Then, we add third small one object (not Centauri C, but one with a much smaller mass): $m_A$ = 1.1, $m_B$ = 0.907 (both actual relative masses), $m_C$ = 0.001.

$m_C$ tries to orbit its closest star, but at some point comes under the influence of the second star and gets 'tossed around'.

```{figure} images/ThreeBody_animation_long.gif
---
name: fig:ThreeBody_animation_long.gif
width: 320px
align: center
--- 
Alpha Centauri A and B circling each other with a third object.
```
If we let the simulations run for a much longer time, we see that at some point the conditions for our small star are such that it is 'shot' into space and disappears for ever.

```{figure} images/ThreeBody_animation_long.png
---
name: fig:ThreeBody_animation_long.png
width: 320px
align: center
--- 
Alpha Centauri A and B circling each other with a third object. The third 'planet' is finally escaping into space.
```

Note: this is a chaotic system and computations need great care. 