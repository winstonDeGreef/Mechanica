# Exercises, examples & solutions
## Exercises


Here are some exercises that deals with oscillations. Make sure you practice IDEA.

```{exercise}
:label: ex_9.1

A massless spring (spring constant $k$) is suspended from the ceiling. The spring has an unstretched length $l_0$. At the other end is a point particle (mass $m$).

* Make a sketch of the situation and define your coordinate system.

* Find the equilibrium position of the mass $m$.

* Set up the equation of motion for $m$.

* Solve it for the initial condition that at $t=0$ the mass $m$ is at the equilibrium position and has a velocity $v_0$.

```

```{exercise}
:label: ex_9.2

Same question, but now two springs are used. Spring 1 has spring constant $k$; spring 2 has $2k$. Both have the same unstretched length $l_0$.

* The two springs are used in parallel, i.e., both are connected to the ceiling, and $m$ is at the joint other end of the springs.

* Both springs are in series, i.e., spring 1 is suspended from the ceiling, and the other one is attached to the free. The particle is fixed to the free end of the second spring.

```

````{exercise}
:label: ex_9.3

A mass $m$ is attached to two springs. The other ends of the springs are fixed and can not move. The distance between these point is $2l_0$. The mass can move only in the horizontal direction and there is no gravity. See the figure below for a sketch. 

```{figure} images/TwoHorSprings1.png
:name: fig:TwoHorSprings1.png
:width: 150px
:align: center
 

```
The springs are identical: both have rest length $l_0$ and spring constant $k$. Based on symmetry, we take the origin in the center of the figure.

We are going to repeat the same analysis as in the previous exercises.

* Make a sketch of the situation and define your coordinate system.
* Find the equilibrium position of the mass $m$.
* Set up the equation of motion for $m$.
* Solve it for the initial condition that at $t=0$ the mass $m$ is at the equilibrium position and has a velocity $v_0$.


````

````{exercise}
:label: ex_9.4

The same as above, but now the length between the two point where the spring are attached to is $l_0$ instead of $2l_0$.
```{figure} images/TwoHorSprings2.png
:name: fig:TwoHorSprings2.png
:width: 150px
:align: center
 

```
Note: in the figure $k, l_0$ denotes the characteristics of the springs. 

* Make a sketch of the situation and define your coordinate system.
* Find the equilibrium position of the mass $m$.
* Set up the equation of motion for $m$.
* Solve it for the initial condition that at $t=0$ the mass $m$ is at the equilibrium position and has a velocity $v_0$.


````
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### Answers

````{solution} ex_9.1
:class: dropdown

Sketch; $z=0$ is when the mass is $l_0$ below the ceiling.

```{figure} images/HangendeVeer1.png
:name: fig:HangendeVeer1.png
:width: 150px
:align: center
 

```
Equilibrium position of the mass $m$: 

$$\sum F = 0 \rightarrow F_v - mg = 0$$

Force of the spring: $F_v = -k(l-l_0) = -kz$. Thus

$$-kz_{eq} - mg = 0 \rightarrow z_{eq} = - \frac{mg}{k}$$

Equation of motion for $m$: set up N2

$$m\frac{dv}{dt} = -kz -mg$$


Solution with $z(0) = z_{eq}$ and $v(0) = v_0$:

homogeneous part of the equation: $m\frac{dv}{dt} + kz=0$

$$z_{hom}(t) = A \cos \omega_0 t + B \sin \omega_0 t $$

with $\omega_0^2 = \frac{k}{m}$

special solution: $z_s = - \frac{mg}{k}$

general solution:

$$z(t) = z_{hom}(t) + z_s(t) = z_{hom}(t) = A \cos \omega_0 t + B \sin \omega_0 t - \frac{mg}{k}$$

initial conditions: 
$$z(0) = z_{eq} = - \frac{mg}{k} \rightarrow A=0$$
and
$$v(0) = v_0 \rightarrow v_0 = \omega_0 B \rightarrow B=\frac{v_0}{\omega_0}$$

Thus, the solution is

$$ z(t) = -\frac{mg}{k} + \frac{v_0}{\omega_0} \sin \omega_o t$$
````


````{solution} ex_9.2
:class: dropdown

Sketch; $z=0$ is when the mass is at $l_0$ below the ceiling. Now we have 2 springs, one with spring constant $k_1$, the other with $k_2$. Both have the same rest length $l_0$

```{figure} images/HangendeVeer2.png
:name: fig:HangendeVeer2.png
:width: 150px
:align: center
 

```
Equilibrium position of the mass $m$: 

$$\sum F = 0 \rightarrow F_{v1} + F_{v2} - mg = 0$$

Forces of the springs: $F_{v1} = -k_1(l-l_0) = -k_1 z$ and $F_{v2} = -k_2(l-l_0) = -k_2 z$. Thus

$$-k_1 z_{eq} - k_2 z_{eq} - mg = 0 \rightarrow z_{eq} = - \frac{mg}{k_1 +k_2}$$

Equation of motion for $m$: set up N2

$$m\frac{dv}{dt} = -(k_1 + k_2) z -mg$$

Thus we conclude, that the exercise is basically the same: all we have to do is replace $k$ by $K_{tot} = k_1 + k_2$

$$m\frac{dv}{dt} = -k_{tot} z -mg$$

The solution with $z(0) = z_{eq}$ and $v(0) = v_0$ is thus

$$ z(t) = -\frac{mg}{k_{tot}} + \frac{v_0}{\omega_0} \sin \omega_o t$$

with $ \omega_0^2 = \frac{k_{tot}}{m}$

````


````{solution} ex_9.3
:class: dropdown

```{figure} images/TwoHorSprings1Sol.png
:name: fig:TwoHorSprings1Sol.png
:width: 200px
:align: center
 

```

Again, we have two springs acting on the mass. However, they are no on opposite sides. We expect on symmetry arguments that the equilibrium will be in the middle, i.e at $x=0$.

If the mass is positioned to the right of $x=0$, spring 1 is extended beyond its rest length and will pull in the negative $x$-direction:

$$F_{v1} = -k(l-l_0) = -kx$$

Spring 2 will than be shorter than its rest length and will push to the negative $x$-direction:

$$F_{v2} = k(l-L_0) = -kx$$

Thus, equilibrium is reached when

$$\sum F = F_{v1} + F_{v2} = 0 \rightarrow -2kx=0 \rightarrow x_{eq}=0$$

as we anticipated.

Equation of motion for $m$: set up N2

$$m\frac{dv}{dt} = -kx - kx = -2kx$$

Thus we conclude, that the exercise is basically the same: all we have to do is replace $k$ by $k_{tot} = 2k$

$$m\frac{dv}{dt} = -2kx$$

General solution $x(t) = A \sin \omega_0 t + B \cos \omega_0 t$ with $\omega_0^2 = \frac{2k}{m}$.

Like in the previous exercises, it is now a matter of specifying the initial conditions and finding $A$ and $B$.

````

````{solution} ex_9.4
:class: dropdown

```{figure} images/TwoHorSprings2Sol.png
:name: fig:TwoHorSprings2Sol.png
:width: 200px
:align: center
 

```

Again, we have two springs acting on the mass. Now they don't fit both with their rest length. The will be compressed and try to lengthen. However, based on symmetry we still do expect that $x=0$ is the equilibrium position.

If the mass is positioned to the right of $x=0$, spring 1 stille too short and will push to the right:

$$F_{v1} = -k(l-l_0) = -k \left (\frac{l_0}{2} + x -l_0 \right ) = k \left ( \frac{l_0}{2} - x \right )$$

Spring 2 will than be even shorter and will push to the negative $x$-direction:

$$F_{v2} = k \left (\frac{l_0}{2}-x-l_0 \right ) = -k \left (\frac{l_0}{2} + x \right )$$

Thus, equilibrium is reached when

$$\sum F = F_{v1} + F_{v2} = 0 \rightarrow k \left ( \frac{l_0}{2} - x \right ) -k \left (\frac{l_0}{2} + x \right ) = -2kx =0 \rightarrow x_{eq}=0$$

as we anticipated.

Equation of motion for $m$: set up N2

$$m\frac{dv}{dt} = -kx - kx = -2kx$$

Thus we conclude, $k_{tot} = 2k$, which is identical to the previous exercise! 
````


````{experiment} Mass spring
Find a rubber band and use nothing but a mass (that you are not allowed to weigh) that you can tie one way or the other to the spring, a ruler, and the stopwatch/clock on your mobile.

Set up an experiment to find the mass $m$, the spring constant $k$, and the damping coefficient $b$.

Don't forget to make a physics analysis first, a plan of how to find both $m$ and $k$.


```{figure} images/MassSpringDIY.png
:name: fig:MassSpringDIY.jpg
:width: 50%
 
From Wikimedia Commons: [bands](https://commons.wikimedia.org/wiki/File:Rubber_bands_20210918_142044.jpg), CC-SA 4.0; [apple](https://commons.wikimedia.org/wiki/File:Red_Apple.jpg), CC-BY 2.0, ; [phone](https://commons.wikimedia.org/wiki/File:IPhone_Dynamic_Island.jpg), PD; [ruler](https://commons.wikimedia.org/wiki/File:Ruler_illustration.svg), CC-BY 4.0.
```

````



## Jupyter labs

1. Mass-spring system
	[Exercise4.ipynb](resources/ClassicalMechanicsSpecialRelativity-Ex4.ipynb)
