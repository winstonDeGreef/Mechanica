---
kernelspec:
  name: python3
  display_name: 'Python 3'
---


# Collisions

## What are collisions?
In daily life we do understand what a collision is: the bumping of two objects into each other. From a physics point of view, we see it slightly different. The objects don't have to touch. It is sufficient if they undergo a mutual interaction *'with a beginning and an end'*. What do we mean by this? 

```{figure} ../images/collision.png
:label: fig:collision.png
:width: 50%

Collision of two particles.
```

Firstly, the mutual interaction means that the objects interact with each other through a mutual force, i.e. a force (pair) that obeys Newton's third law.  
Secondly, we assume that this force works over a small distance only. Or re-phrased we will only consider the situation before the objects feel the force and compare that to after they have felt it. We don't bother about the details of the motion of the objects *during* their interaction. Hence, when we depict a collision as in {numref}`fig:collision.png`, we usually draw the situation before the collision, then some kind of 'comic way' of showing the collision and finally we draw the outcome of the collision, so after the interaction. In many cases, people leave the middle part out of their drawing.

There are two principle types of collisions to distinguish: *elastic* and *inelastic* collisions. For an elastic collision the kinetic energy is conserved, whereas for an inelastic that is not the case. In the latter case, energy can be converted into deformation or heat.

Since the objects interact under the influence of their mutual interaction, we have conservation of momentum:
$$
\sum_i \vec{p}_i^{before} = \sum_i \vec{p}_i^{after}
$$

Why? No external forces implies constant total momentum.


## Elastic Collisions

For an elastic collision the kinetic energy is conserved by definition (next to the conservation of momentum). That is the sum of the kinetic energy before the collision is the same as the sum after the collision. This type of collision is also called *hard-ball collision*: as with colliding billiard balls no energy is dissipated into heat or deformation.

```{iframe} https://trinket.io/embed/glowscript/44e9d32f7951
:label: Vpyt_col
```

For elastic collisions the interaction force needs to be conservative. Then, a potential energy exists. And this energy is such that the objects have the same potential energy before as after the collision. Consequently energy conservation leads to: 

$$ E_{kin, before} + V_{before} = E_{kin, after} +\underbrace{V_{after}}_{= V_{before}} \Rightarrow E_{kin, before} = E_{kin, after} $$


### Solving collision problems

Given a collision experiment where the initial situation before the collision is known, how do we compute the situation after the collision? What will the velocities of the object be? 

Consider a head-on collision of two point particles on a line as shown in {numref}`fig:collision2.png`. One particle with mass $3m$ is initially at rest ($u=0$), the other with mass $2m$ has velocity $2v$. What are the velocities $v',u'$ of the particles after the collision?

```{figure} ../images/collision2.png
:label: fig:collision2.png
:width: 320px
:align: center
 
Example of a 1D elastic collision.
```

We can write down two equations using conservation of momentum and kinetic energy before and after the collision

$$
\begin{array}{rcl}
2m(2v)+0 &=& 2mv' + 3mu' \quad (*)\\
\frac{1}{2}2m(2v)^2 + 0 &=& \frac{1}{2}2mv'^2 + \frac{1}{2} 3mu'^2
\end{array}
$$

We have two equations and two unknowns $(v',u')$, therefore we can in principle solve this problem. The question is, what is the best strategy to do so? A strategy is needed especially since one equation involves the square of the velocity. 

We first bring the velocities $v,v'$ and $u,u'$ to the same side.

$$
\begin{array}{rcl}
\label{eq1} 2m(2v-v')&=& 3mu'\\
\label{eq2} \frac{1}{2}2m(4v^2-v'^2)  &=& \frac{1}{2}3mu'^2
\end{array}
$$

Now we divide the two equations (verify yourselves!), this makes the solution very easy as the squares of the velocities always divide out.

$$
\Rightarrow 2v+v'=u' \quad (**)
$$

We can use this to find both unknowns by smartly adding equations $(*)$ and $(**)$. Smartly in the sense that we can multiply either of the equations with a scalar in such way that one quantity can be discarded.

$$\begin{array}{lcl}
\begin{split}
    4v&=2v'+3u' \\
    2v&=-v'+u'|* 2 \\
    \hline
    8v&=5u' \\ &\Rightarrow u'=\frac{8}{5}v  
  \end{split} &&
\begin{split}
    4v&=2v'+3u' \\
    2v&=-v'+u'| *-3 \\
    \hline
    -2v&=5v' \\ &\Rightarrow v'=-\frac{2}{5}v  
  \end{split}  
\end{array}$$

This solution strategy always works. NB: you need to practice this. Although it is conceptually easy, we often see that students have problems when actually solving for the 2 unknowns.

```{figure} ../images/sol_col.jpg
:width: 80%

Solving 
```

```{tip} Vpython simulation
Above we provided a {ref}`Vpython <Vpyt_col>` simulation. Change the code in order to verify the above solution.

```

Actually, now we think about this strategy: isn't it strange, the kinetic energy equation is squared in our unknowns. Shouldn't we expect 2 solutions? 

The answer is yes: there ought to be 2 solutions. Where is the second one?
Note that when dividing the two equations, we have to make sure that we do not divide by 0. It is very well possible that we do so: suppose $u' = 0$, then also $2v-v' = 0$ and we can not do the division. But what does that mean: $u'=0$ and $2v-v'=0$? Well, of course, then we have after the collision that the incoming particle $2m$ still has velocity $2v$ and the other particle $3m$ is still at rest. 

In retrospect: of course this must be one of the solutions to the problem. We haven't specified anything about the interaction force. But suppose it is absent, that is, the particles don't interact at all. Then of course the situation before the collision (a bit strange calling this a collision, but anyway), will still be present after the 'collision'. If nothing happens to the particles, then obviously the sum of the momentum as well as of the kinetic energy stays the same. This actually provides a great check of your work: do you recover the initial conditions?


### Collisions in a plane

Consider now a 2D elastic collision such that the two particles collide in the origin, {numref}`fig:2Dcollision1.png`.


```{figure} ../images/2Dcollision1.png
:label: fig:2Dcollision1.png
:width: 250px
:align: center
 
Example of a 2D elastic collision.
```

If we write down the equation of conservation of momentum (in $x,y$ components) and of kinetic energy, we get

$$
\begin{array}{lcr}
2m(2v)+0 &=& 2mv'_x + 3mu'_x \\
0+ 3mv &=& 2mv'_y + 3mu'_y \\
\frac{1}{2}2m(2v)^2 + \frac{1}{2}3mv^2 &=& \frac{1}{2}2m v'^2 + \frac{1}{2}3mu'^2  
\end{array}
$$

Now we have **4** unknowns ($v'_x, v'_y, u'_x, u'_y$) but only **3** equations. The outcome seems not to be determined by the initial condition... Of course, that cannot be the case (Think shortly why?). The outcome is fully determined by the initial conditions, but we did not set up the equations in the best way because we did not first transform the problem into a 1D problem such that the collision is head-on.

We can use a Galilean Transformation to put one particle at rest. Here we set the blue particle to rest by subtracting $-2v$ from its velocity, that is we move with the blue particle (prior to the collision). The corresponding Galilean Transformation is

$$
\begin{array}{rcl}
x' &=& x-2vt\\
y' &=& y
\end{array}
$$

The red particle now has velocity $(-2v,v)$. The problem is still 2D.

```{figure} ../images/2Dcollision2.png
:label: fig:2Dcollision2.png
:width: 250px
:align: center
 
Applying the Galilean Transformation.
```

Next, we can rotate the coordinate system, to obtain a 1D head-on collision that we can solve as above. 

```{figure} ../images/2Dcollision3.png
:label: fig:2Dcollision3.png
:width: 250px
:align: center
 
Rotating the coordinate system.
```

We see that we now have a 1-dimensional elastically collision with a particle of mass $3m$ coming in over the $x"$-axis with velocity $-\sqrt{5}v$. It will collide with a particle of mass $2m$ which is at rest. We know how to solve this problem and find the velocities of both particles after the collision. If we do this, we find that after the collision the velocity of the blue particle is $U^{''}_{x^{''}} = -\frac{6}{5}\sqrt{5}v$ and of the red particle $V^{''}_{x^{''}} = -\frac{1}{5}\sqrt{5}v$. Note that we have specified these velocity in the $(x",y")$ coordinate system.

Next steps would be to convert the velocities back to the initial coordinate frame. That is a bit cumbersome, but again conceptually easy. The final answer in the original frame of reference is: 

$$\begin{array}{lll}
2m: &v'_x = -\frac{2}{5}v, &v'_y = \frac{6}{5}v\\
3m: &u'_x = \frac{8}{5}v, &u'_y = \frac{1}{5}v
\end{array}$$


```{iframe} https://www.youtube.com/embed/kYB8IZa5AuE?si=I9Mz-o4_fcMM-6Mu

The 3Blue1Brown series on linear algebra describes the linear transformations above in a mathematical way. Using linear algebra, above computations will become easier.
```

## Collisions in the Center of Mass frame

There is a special frame of reference: the Center of Mass (CM) frame. Its origin is defined with respect to the *lab frame* as 

$$\vec{R}=\frac{\sum m_i \vec{x}_i}{\sum m_i}$$ 

We will introduce this formally in the next chapter.

As the mass is conserved during a collision we have 
1) $\sum m_i=const$ and 
2) as the momentum is conserved $\sum m_i \dot{\vec{x}}_i=const$, 

we see that the velocity of the CM does not change before and after collision

$$
\dot{\vec{R}}_{before}=\dot{\vec{R}}_{after}
$$

Instead of working in the lab frame we can use the CM frame. A sketch of the coordinates and vectors is given in the figure below.

```{figure} ../images/CMsketch.png
:label: fig:CMsketch.png
:width: 250px
:align: center
 
Center of mass.
```

For the relative coordinates $\vec{r}_i$ it holds that $\sum m_i \vec{r}_i =0$. Considering two particles: The relative distance $\vec{r}=\vec{r}_1-\vec{r}_2 = \vec{x}_1 -\vec{x}_2$ is Galilei invariant.

Using this property we express the vectors $\vec{r}_1$ and $\vec{r}_2$ in terms of the relative distance vector $\vec{r}$ for $\vec{r}_1=\frac{\mu}{m_1}\vec{r}$ and $\vec{r}_2=-\frac{\mu}{m_2}\vec{r}$ with $\mu$ the so-called reduced mass (see next chapter). Therefore

$$
\begin{array}{lcr}
m_1\vec{r}_1 &=& \mu \dot{\vec{r}}_1\\
m_2\vec{r}_2 &=& -\mu \dot{\vec{r}}_2
\end{array}
$$

This means the momenta of both particles are *always* equal in magnitude and opposed in direction in the CM frame. Only the orientation of the pair $\dot{\vec{r}}_{1,2}$ can change from before to after the collision.


```{figure} ../images/CMmomentum.png
:label: fig:CMmomentum.png
:width: 320px
:align: center
 
Collision in center of mass frame.
```

```{exercise} 

Add to the {ref}`vpython code <Vpyt_col>` the center of mass and show that the velocity of the center of mass does not change.

```

## Computational
```{figure} ../images/coll_eq_2D
:width: 70%
```

UITWERKEN FREEK



## Inelastic Collisions

For inelastic collisions only the *momentum is conserved*, but *not the kinetic energy*. The kinetic energy after the collision is always less than before the collision. As the total energy is conserved, some kinetic energy is converted to deformation or heat.

The amount of "inelasticity" or loss of energy can be quantified by the *coefficient of restitution* $e$

$$
e\equiv \frac{v_{rel,after}}{v_{rel,before}}
$$

$$
e^2 \equiv \frac{E_{kin,after}}{E_{kin,before}} \text{ in CM frame}
$$

For $e=0$ the collision is fully inelastic, for $e=1$ it is fully elastic.



### INTERMEZZO MET Q=CMDT 

UITWERKEN FREEK
