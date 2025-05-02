# Potential Energy

## Conservative force ##

Work done on $m$ by $F$ during motion from 1 to 2 over a prescribed trajectory, is defined as:
$$
	W_{12} = \int_1^2 \vec{F} \cdot d\vec{r} 
$$

In general, the amount of work depends on the path followed. That is, the work done when going from $ \vec{r}_1 $ to $ vec{r}_2 $ over the red path in the figure below, will be different when going from  $ \vec{r}_1 $ to $ \vec{r}_2 $ over the blue path. Work depends on the specific trajectory followed.

```{figure} images/Path12.jpg
---
name: fig:Path12.jpg
width: 70%
align: center
---
Two different paths.
```


However, there is a certain class of forces for which the path does not matter, only the start and end point do. These forces are called conservative forces. As a consequence, the work done by a conservative force over a closed path, i.e start and end are the same, is always zero. No matter which closed path is taken.

```{math}
:label: eq:5.1

\text{conservative force } \Leftrightarrow \oint \vec{F} \cdot d\vec{r} = 0 \text{ for }\textbf{ALL}\text{ closed paths}                                          
```

## Stokes' Theorem ##
It was George Stokes who proved an important theorem, that we will use to turn the concept of conservative forces into a new and important concept.

```{figure} images/GeorgeStokes.jpg
---
name: fig:GeorgeStokes.jpg
width: 70%
align: center
---
Sir George Stokes (1819-1903). From [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Ggstokes.jpg), public domain.
```

His theorem reads as: 

$$
	\oint \vec{F} \cdot d\vec{r} = \iint \vec{\nabla} \times \vec{F} \cdot d\vec{\sigma} 
$$

In words: the integral of the force over a closed path equals the surface integral of the curl of that force. The surface being 'cut out' by the close path. The term $\vec{\nabla} \times \vec{F}$ is called the curl of $F$: it is a vector. The meaning of it and some words on the theorem are given below.

````{admonition} Intermezzo: intuitive proof of Stokes' Theorem 
:class: note

Consider a closed curve in the $xy$-plane. We would like to calculate the work done when going around this curve. In other words: what is $\oint \vec{F} \cdot d\vec{r}$ if we move along this curve?<br>

We can visualize what we need to do: we cut the curve in small part; compute $\vec{F} \cdot d\vec{r}$ for each part (i.e. the red, green, blue, etc. in fig.(\ref{Stokes2.jpg}) and sum these to get the total along the curve. If we make the parts infinitesimally small, we go from a (Riemann) sum to an integral. 

```{figure} images/Stokes2.jpg
---
name: fig:Stokes2.jpg
width: 70% 
align: center
--- 
Closed path on a grid.
```

We are going to compute much more: take a look at {numref}`fig:Stokes2.jpg`. We have put a grid in the $xy$-plane over a closed curve $\Gamma$. Hence, the interior of our curve is fool op squares. We are not only computing the parts along the curve, but also along the sides of alle curves. This will sound like way too much work, but we will see that it actually is a very good idea.

See {numref}`fig:Stokes2.jpg`: we calculate $\oint \vec{F} \cdot d\vec{r}$ counter clockwise for the green square. Than we have at least the green part of our $\oint \vec{F} \cdot d\vec{r}$ done in the right direction. Hence, we compute $\int \vec{F} \cdot d\vec{r}$ along the right side of the green square. We do that from bottom to top as we go counter clockwise along the green square. Let's call that $\int_g \vec{F} \cdot d\vec{r}$.<br>

Then we move to the blue square and repeat in counter clockwise direction our calculation. But this means that we compute along the left side of blue the square from top to bottom. We will call this $\int_b \vec{F} \cdot d\vec{r}$.<br>

Note that we will add all contributions. Thus we get $\int_g \vec{F} \cdot d\vec{r} + \int_b \vec{F} \cdot d\vec{r}$. But these two cancel each other as they are exactly the same but done in opposite directions. Thus if we use that $\int_1^2 f dx = - \int_2^1 f dx$ for any integration, it becomes obvious that  $\int_g \vec{F} \cdot d\vec{r} + \int_b \vec{F} \cdot d\vec{r} = 0$.<br>

Note that this will happen for all side of the squares that are in the interior of our curve. Thus, the integral over all squares is exactly the integral along the curve $\Gamma$.<br>

It seems, we do a lot of work for nothing. But there is another way of looking at the path-integrals along the squares. If we make the square small enough, the calculation along one square can be approximated:

$$ \begin{split}
\oint_{square} \vec{F} \cdot d\vec{r} &\approx F_x(x,y) dx + F_y(x+dx,y) dy - F_x (x,y+dy) dx - F_y(x,y) dy \\
& \approx \frac{F_x(x,y) - F_x (x,y+dy)}{dy} dxdy + \frac{F_y(x+dx,y) - F_y(x,y) }{dx} dxdy \\
& \approx \left ( \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right ) dx dy
\end{split} $$

The results get more accurate the smaller we make the square.

If we now sum up all squares and make these squares infinitesimally small, the sum becomes an integral, but now an integral over the surface enclosed by the curve:

$$
\oint_{\Gamma} \vec{F} \cdot d\vec{r} = \iint \left ( \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right ) dx dy
$$

The right hand side of the above equation is an surface integral of the 'vector' $\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}$. Obviously, we did not provide a rigorous proof, but only an intuitive one. For a mathematical proof, see your calculus classes.<br>

Moreover, we only worked in the $xy$-plane. If we would extend our reasoning to a closed curve in 3 dimensions, we would get Stokes theorem, which reads as:

$$ \oint_{\Gamma} \vec{F} \cdot d\vec{r} = \iint \vec{\nabla} \times \vec{F} \cdot d\vec{\sigma} $$

Here, $d\vec{\sigma}$ is a small element out of the surface. Note that it is a vector: it has size and directions. The latter is perpendicular to the surface element itself. Furthermore, we have the vector $\vec{\nabla} \times \vec{F}$. This is the cross-product of the nabla-operator and our vector field $\vec{F}$. The nabla operator is a strange kind of vector. Its components are: partial differentiation. In a Cartesian coordinate system this can be written as:

$$
\vec{\nabla} \equiv \frac{\partial}{\partial x} \hat{x} + \frac{\partial}{\partial y} \hat{y} + \frac{\partial}{\partial z} \hat{z}
$$

or if you prefer a column notation:

$$
\vec{\nabla} \equiv \left ( \begin{matrix} \frac{\partial}{\partial x} \\ \frac{\partial}{\partial y} \\ \frac{\partial}{\partial z} \end{matrix} \right )
$$

The curl of $F$ can be found from e.g.

$$
\vec{\nabla} \times \vec{F} =  \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_x & F_y & F_z  \end{vmatrix} 
= \left ( \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} \right ) \hat{x} + \left ( \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} \right ) \hat{y} + \left ( \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right ) \hat{z}
$$

Note of warning: do be careful with the nabla-operator. It is not a standard vector. For instance, ordinary vectors have the property $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$. This does not hold for the nabla-operator.<br>

Second note of warning: the representation of the nabla-operator does change quite a bit when using other coordinate systems like cylindrical or spherical. For instance, in cylindrical coordinates it is <b><em>not</em></b> equal to $\left ( \begin{matrix} \frac{\partial}{\partial r} \\ \frac{\partial}{\partial \phi} \\ \frac{\partial}{\partial z} \end{matrix} \right )$. This can be easily seen as both $r, z$ have units length, i.e. meters, but $\phi$ has no units.
````

````{admonition} Example 5.1
:class: important

Suppose we need to calculate the integral of the vectorfield $\vec{F}(x,y) = y \hat{x} - x \hat{y}$ over the closed curve formed by a square from $(0,0)$ to $(1,0)$, $(1,1)$, $(0,1)$ and back to $(0,0)$.

```{figure} images/StokesTheoremExample.jpg
---
name: fig:StokesTheoremExample.jpg
width: 70%
align: center
---
Integrating along the unit square.
```

We go counter clockwise. 

$$ \begin{split}
\oint \vec{F} \cdot d\vec{r} &= \int_{x=0}^1 F_x(x,y=0) dx + \int_{y=0}^1 F_y(x=1,y) dy + \\
& \;\; + \int_{x=1}^0 F_x(x,y=1) dx + \int_{y=1}^0 F_y(x=0,y) dy \\
&= \int_0^1 0 dx + \int_0^1 -1 dy + \int_1^0 1 dx + \int_1^0 -0 dx  \\
&= 0 - [y]_0^1 + [x]_1^0 - 0 \\
&= -2 
\end{split} $$

Now we try this using Stokes' Theorem:

$$
\oint \vec{F} \cdot d\vec{r} = \iint \vec{\nabla} \times \vec{F} \cdot d\vec{\sigma}
$$

We first calculate $\vec{\nabla} \times \vec{F}$:

$$
\vec{\nabla} \times \vec{F} =  \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_x & F_y & F_z  \end{vmatrix} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
y & -x & 0  \end{vmatrix} = \left ( \frac{\partial (-x)}{\partial x}  - \frac{\partial (y)}{\partial y} \right ) \hat{z} = -2 \hat{z}
$$

Thus, in this example $\vec{\nabla} \times \vec{F}$ has only a $z$-component. 

An elementary surface element of the square is: $d\vec{\sigma} = dx dy \hat{z}$.
This also has only a $z$-component. Note that it points in the positive $z$-direction. This is a consequence of the counter clockwise direction that we use to go along the square.

According to Stokes Theorem, we this find:

$$
\oint \vec{F} \cdot d\vec{r} = \iint \vec{\nabla} \times \vec{F} \cdot d\vec{\sigma} = \int_{x=0}^1 \int_{y=0}^1 (-2) dxdy = -2
$$

Indeed, we find the same outcome.
````

## Conservative force and $\vec{\nabla} \times \vec{F}$ ##

For a conservative force the integral over the closed path is zero for any closed path. Consequently, $ \vec{\nabla} \times \vec{F} = 0 $ everywhere. How do we know this? Suppose $ \vec{\nabla} \times \vec{F} \neq 0 $ at some point in space. Then, since we deal with continuous differentiable vector fields, in the close vicinity of this point, it must also be non-zero. Without loss of generality, we can assume that in that region $ \vec{\nabla} \times \vec{F} \cdot d\vec{\sigma}> 0 $. Next, we draw a closed curve around this point, in this region. We now calculate the $\oint \vec{F} \cdot d\vec{r}$ along this curve. That is, we invoke Stokes Theorem. But we know that $ \vec{\nabla} \times \vec{F} \cdot d\vec{\sigma} > 0 $ on the surface formed by the closed curve. Consequently, the outcome of the surface integral is non-zero. But that is a contradiction as we started with a conservative force and thus the integral should have been zero. <br>
The only way out, is that $ \vec{\nabla} \times \vec{F} = 0 $ everywhere.

Thus we have:

$$
\text{conservative force  } \Leftrightarrow \vec{\nabla} \times \vec{F} = 0 \text{ everywhere}
$$
<br>


## Potential Energy ##
 A direct consequence of the above is:<br>

 if $ \vec{\nabla} \times \vec{F} = 0 $ everywhere, a function $ V (\vec{r})) $ exists such that $ \vec{F} = -\vec{\nabla}V $
          
$$
	\text{conservative force } \Leftrightarrow \vec{\nabla} \times \vec{F} = 0  \text{ everywhere } \\
	\big\Updownarrow \\
	\vec{F} = -\vec{\nabla}V \Leftrightarrow V(\vec{r}) = -\int_{ref} \vec{F} \cdot d\vec{r} 
$$
       

where in the last integral, the lower limit is taken from some, self picked, reference point. The upper limit is the position $ \vec{r} $.<br>

This function V is called the potential energy or the potential for short. It has a direct connection to work and kinetic energy.

$$
	E_{kin,2} - E_{kin,1} = W_{12} = \int_1^2 \vec{F} \cdot d\vec{r} = V(\vec{r}_2) - V(\vec{r}_1)
$$

or rewritten:

$$
	E_{kin,1} + V(\vec{r}_1)  = E_{kin,2} + V(\vec{r}_2) 
$$ 

In words: **for a conservative force, the sum of kinetic and potential energy stays constant**.<br><br>

### Energy versus Newton's Second Law ###
We, starting from Newton's Laws, arrived at an energy formulation for physical problems. <br>
Question: can we also go back? That is: suppose we would start with formulating the energy rule for a physical problem, can we then back out the equation of motion?<br>
Answer: yes, we can!

It goes as follows. Take a system that can be completely described by its kinetic plus potential energy. Then: take the time-derivative and simplify, we will do it for a 1-dimensional case first.

$$\begin{split}
&\frac{1}{2}mv^2 + V(x) = E_0 \Rightarrow \\
&\frac{d}{dt} \left [ \frac{1}{2}mv^2 + V(x) \right ] = \frac{dE_0}{dt} = 0 \Rightarrow \\
&mv\dot{v} + \frac{dV}{dx}\underbrace{\frac{dx}{dt}}_{=v} = 0 \Rightarrow \\
&v \left (m\dot{v} + \frac{dV}{dx} \right ) = 0
\end{split}$$

The last equation must hold for all times and all circumstances. Thus, the term in brackets must be zero.

$$ m\dot{v} + \frac{dV}{dx} = 0 \Rightarrow m\ddot{x} = -\frac{dV}{dx} = F $$

And we have recovered Newton's second law.

In 3 dimensions it is the same procedure. What is a bit more complicated, is using the chain rule. In the above 1-d case we used $\frac{dV}{dt} = \frac{dV(x(t))}{dt} = \frac{dV}{dx}\frac{dx(t)}{dt}$. In 3-d this becomes: 

$$\frac{dV}{dt} = \frac{dV(\vec{r}(t))}{dt} = \frac{dV}{d\vec{r}}\cdot \frac{d\vec{r}(t)}{dt} = \vec{\nabla} V \cdot \vec{v} $$

Thus, if we repeat the derivation, we find: 

$$\begin{split}
&\frac{1}{2}mv^2 + V(\vec{r}) = E_0 \Rightarrow \\
&\frac{d}{dt} \left [ \frac{1}{2}mv^2 + V(\vec{r}) \right ] = 0 \Rightarrow \\
&m\vec{v} \cdot \dot{\vec{v}} + \vec{\nabla} V \cdot \vec{v} = 0 \Rightarrow \\
&v \left (m\vec{a} + \vec{\nabla} V \right ) = 0 \Rightarrow \\
&m\vec{a} = -\vec{\nabla} V = \vec{F}
\end{split}$$

And we have recovered the 3-dimensional form of Newton's second Law.
This is a great result. It allows us to pick what we like: formulate a problem in terms of forces and momentum, i.e. Newton's second law, or reason from energy considerations. It doesn't matter: they are equivalent. It is a matter of taste, a matter of what do you see first, understand best, find easiest to start with. Up to you!


## Stable/Unstable Equilibrium ##
A particle (or system) is in equilibrium when the sum of forces acting on it is zero. Then, it will keep the same velocity, and we can easily find an inertial system in which the particle is at rest, at an equilibrium position. <br>
The equilibrium position (or more general state) can also be found directly from the potential energy.

Potential energy and (conservative) forces are coupled via: 

$$ \vec{F} = - \vec{\nabla}V $$

The equilibrium positions $\left ( \sum_i \vec{F}_i = 0 \right )$ can be found by finding the extremes of the potential energy:

$$
\text{equilibrium position } \Leftrightarrow \vec{\nabla}V = 0
$$
Once we find the equilibrium points, we can also quickly address their nature: is it a stable or unstable solution? That follows directly from inspecting the characteristics of the potential energy around the equilibrium points.

For a stable equilibrium, we require that a small push or a slight displacement will result in a force pushing back such that the equilibrium position is restored (apart from the inertia of the object that might cause an overshoot or oscillation).

However, an unstable equilibrium is one for which the slightest push or displacement will result in motion away from the equilibrium position.

The second derivative of the potential can be investigated to find the type of extremum. For 1D functions that is easy, for scalar valued functions of more variables that is a bit more complicated. Here we only look at the 1D case $V(x): \mathbb{R} \rightarrow \mathbb{R}$

$$
\text{equilibrium: } \vec{\nabla}V = 0 
	\begin{cases}
	\text{stable: } & \frac{d^2V}{dx^2} > 0 \\
	\text{unstable: } & \frac{d^2V}{dx^2} < 0
	\end{cases} 
$$
 
Luckily, the definition of potential energy is such that these rules are easy to visualize in 1D and remember, see fig.(?.?).

```{figure} images/PotentialStableUnstable.jpg
---
name: fig:PotentialStableUnstable.jpg
width: 70%
align: center
---
Stable and unstable position of a particle in a potential.
```

A valley is stable; a hill top is unstable. <br>
NB: Now the choice of the minus sign in the definition of the potential is clear . Otherwise a hill would be stable, but that does not feel natural at all.

It is also easy to visualize what will happen if we distort that particle from the equilibrium state:

<ul>
<li>The valley, i.e., the stable system, will make the particle move back to the lowest point. Due to inertia, it will not stop but will continue to move. As the lowest position is one of zero force, the particle will 'climb' toward the other end of the valley and start an oscillatory motion.</li>
<li>The top, i.e., the unstable point, will make the particle move away from the stable point. The force acting on the particle is now pushing it outwards, down the slope of the hill.</li>
</ul>
<br>


### Taylor Series Expansion of the Potential ###

The Taylor expansion or Taylor series is a mathematical approximation of a function in the vicinity of a specific point. It uses an infinite series of polynomial terms with coefficients given by value of the derivative of the function at that specific point: the more terms you use, the better the approximation. If you use all terms, then it is exact. Mathematically, it reads for a 1D scalar function $f: \mathbb{R} \rightarrow \mathbb{R}$:

$$
 f(x) \approx f(x_0) + \frac{1}{1!} f'(x_0) (x-x_0 ) + \frac{1}{2!} f''(x_0) (x-x_0)^2 + \frac{1}{3!} f'''(x_0) (x-x_0)^3 + ...
$$
 
For our purpose here, it suffices to stop after the second derivative term:

 $$
 f(x) \approx f(x_0) + f'(x_0) (x-x_0 ) + \frac{1}{2} f''(x_0) (x-x_0)^2 + \mathcal{O}(x^3)
 $$
 
A way of understanding why the Taylor series actually works is the following.<br>
Imagine you have to explain to someone how a function looks around some point $x_0$, but you are not allowed to draw it. One way of passing on information about $f(x)$ is to start by giving the value of $f(x)$ at the point $x_0$:

$$
 f(x) \approx f(x_0)
$$
 
Next, you give how the tangent at $x_0$ is; you pass on the first derivative at $x_0$. The other person can now see a bit better how the function changes when moving away from $x_0$:

$$
 f(x) \approx f(x_0) + f'(x_0) (x-x_0 ) 
$$

Then, you tell that the function is not a straight line but curved, and you give the second derivative. So now the other one can see how it deviates from a straight line:

$$
 f(x) \approx f(x_0) + \frac{1}{1!} f'(x_0) (x-x_0 ) + \frac{1}{2!} f''(x_0) (x-x_0)^2 
$$
 
Note that the prefactor is placed back. But the function is not necessarily a parabola; it will start deviating more and more as we move away from $x_0$. Hence we need to correct that by invoking the third derivative that tells us how fast this deviation is. And this process can continue on and on.

Important to note: if we stay close enough to $x_0$ the terms with the lowest order terms will always prevail as higher powers of $(x-x_0)$ tend to zero faster than a lower powers (for instance: $0.5^4 << 0.5^2$).

Here is a
<a href="https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=29s"> youtube movie </a>
that explains the 1D Taylor series nicely (for physicists).

For scalar valued functions as our potentials $V(\vec{r}): \mathbb{R}^3 \rightarrow \mathbb{R}$ the extension of the Taylor series is not too difficult. If we expand the function around a point 

$$\begin{split}
 V(\vec{r}) &\approx V(\vec{r}_0) + \vec{\nabla}V(\vec{r}_0) \cdot (\vec{r}-\vec{r}_0 ) \\
 &+ \frac{1}{2} (\vec{r}-\vec{r}_0 ) \cdot (\partial^2 V)(\vec{r}_0) \cdot (\vec{r}-\vec{r}_0 ) + \mathcal{O}(r^3)
\end{split}$$
 
The second derivative of the potential indicated by $\partial^2 V$ is the Hessian matrix.

Conceptually the extrema of the function are again the hills and valleys. The classification of the extrema has next to hills and valleys also saddle points etc. In this course we will not bother about these more dimensional cases, but only stick to simple ones.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

### Examples & Exercises ###
```{admonition} Example 5.2
:class: important
   
Is gravity $ \vec{F}_g = m\vec{g} $ a conservative force? If yes, what is the corresponding potential energy?

To find the answer we can do two things:

&nbsp;&nbsp;&nbsp;a. Show $ \vec{\nabla} \times m\vec{g} = 0 $ </li><br>
&nbsp;&nbsp;&nbsp;b. Find a $V$ that satisfies $ -m\vec{g} = -\vec{\nabla} V $ 

```
```{admonition} Solution Example 5.2
:class: tip, dropdown

&nbsp;&nbsp;&nbsp;a. $ \vec{\nabla} \times m\vec{g} = 0 $? How to compute it? For <b>Cartesian</b> coordinates there is an easy to remember rule: 
$$ \vec{\nabla} \times \vec{F} = \begin{vmatrix}\hat{x}&\hat{y}&\hat{z}\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\F_x&F_y&F_z\end{vmatrix} $$
If we chose our coordinates such that $ \vec{g} = -g \hat{z} $ we get:
        $$\vec{\nabla} \times \vec{F}_g = \begin{vmatrix}\hat{x}&\hat{y}&\hat{z}\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\0&0& -mg\end{vmatrix} = 0$$
        Thus $ \vec{F}_g $ is conservative.


&nbsp;&nbsp;&nbsp;b. Secondly: does $ -m\vec{g} = -\vec{\nabla} V $ have a solution for V? Let's try, using the same coordinates as above.
    $$\begin{split}
	-\vec{\nabla}V &= - m\vec{g} \Rightarrow \\
    \frac{\partial V}{\partial x} &= 0 \rightarrow V(x,y,z) = f(y,z) \\
    \frac{\partial V}{\partial y} &= 0 \rightarrow V(x,y,z) = g(x,z) \\
    \frac{\partial V}{\partial z} &= mg \rightarrow V(x,y,z) = mgz + h(x,y) 
	\end{split} $$
          
f,g,h are unknow functions. But all we need to do, is find one $V$ that satisfies $ -m\vec{g} = -\vec{\nabla} V $.<br> 
		 
So, if we take $ V(x,y,z) = mgz $ we have shown, that gravity in this form is conservative and that we can take $ V(x,y,z) = mgz $ for its corresponding potential energy.<br>
          
By the way: from the first part (curl F = 0), we know that the force is conservative and we know that we could try to find V from 
 
$$ \begin{split}
V(x,y,z) &= -\int_{ref} m\vec{g} \cdot d\vec{r} 
= \int_{ref} mg \hat{z} \cdot d\vec{r} \\
&= \int_{ref} mg dz = mgz + const 
\end{split} $$

```
```{exercise-start}
:label: 51
```

A simple model for the frictional force experienced by a body sliding over a horizontal, smooth surface is $ F_f = -\mu F_g $ with $ F_g $ the gravitational force on the object.The friction force is opposite the direction of motion of the object.

<ul>
	<li>Show that this frictional force is not conservative (and, consequently, a potential energy associated does not exist!).</li>
</ul>

Hint: think of two different trajectories to go from point 1 to point 2 and show that the amount of work along these trajectories is not the same.
```{exercise-end}
```

```{exercise-start}
:label: 52
``` 

A force is given by: $ \vec{F} = x\hat{x} + y\hat{y} + z\hat{z} $ 

<ol type="a">
	<li>Show that this force is conservative.</li>
	<li>Find the corresponding potential energy.</li>
</ol>

A second force is given by: $ \vec{F} = y\hat{x} + x\hat{y} + z\hat{z} $

<ol type = "a">
	<li>Show that this force is also conservative.</li>
	<li>Find the corresponding potential energy.</li>
</ol>


```{exercise-end}
```

```{exercise-start}
:label: 53
```

Another force is given by: $ \vec{F} = y\hat{x} - x\hat{y} $

<ol type="a">
	<li>Show that this frictional force is not conservative.</li>
	<li>Compute the work done when moving an object over the unit circle in the xy-plane in an anti-clockwise direction.<br>
            Hint: use Stokes theorem.</li>
	<li>Discuss the meaning of your answer: is it positive or negative? And what does that mean in terms of physics?</li>
</ol>


```{exercise-end}
```

```{exercise-start}
:label: 54
```

Given a potential energy $ E_{pot} = xy$. <br>
&nbsp;&nbsp;&nbsp;a. Find the corresponding force (field).<br>
&nbsp;&nbsp;&nbsp;b. Make a plot of $ \vec{F} $ as a function of (x,y,z).<br>
&nbsp;&nbsp;&nbsp;c. Describe the force and comment on what the potential itself already reveals about the force.
  

```{exercise-end}
```

```{exercise-start}
:label: 55
```

Given a force field $ \vec{F} = -xy \hat{x} + xy \hat{y} $. A particle moves from $ (x,y) = (0,0) $ over the x-axis to $ (x,y) = (1,0) $ and then parallel to the y-axis to $ (x,y) = (1,1) $. In a second motion, the same particle goes from $ (x,y) = (0,0) $ over the y-axis to $ (x,y) = (0,1) $ and then parallel to the x-axis to end also in $ (x,y) = (1,1) $.

<ol type="a">
	<li>Show that not necessarily the work done over the two paths is equal.</li>
	<li>Compute the amount of work done over each of the paths.</li>
</ol>


```{exercise-end}
```

```{exercise-start}
:label: 56
```

A particle of mass m is initially at position $ x=0$. It has zero velocity. <br>
On the particle a force is acting. The force can be described by $ F = F_0 \sin \frac{x}{L} $ with $ F_0 $ and $ L $ positive constants.
 
&nbsp;&nbsp;&nbsp;a. Show that this force is conservative and find the corresponding potential. Take as reference point for the potential energy $ x = \frac{\pi}{2} L $.<br>
&nbsp;&nbsp;&nbsp;b. The particle gets a tiny push, such that it starts moving in the positive x-direction. Its initial velocity is so small that, for all practical calculations, it can be set to zero. Under the influence of the force, the particle will move. Why did the particle get its tiny push?<br>
&nbsp;&nbsp;&nbsp;c. Find the maximum velocity that the particle can get. At which location(s) will this take place?.
</ol>

Note: this is a 1-dimensional problem.
   
```{exercise-end}
```



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### Answers ###

```{solution-start} 51
:class: dropdown
```

Click for the solution <a href="Solutions/ExerciseFrictionNotConservative.pdf"> Friction Not Conservative</a>.

```{solution-end}
```
```{solution-start} 52
:class: dropdown
```

Click for the solution <a href="Solutions/ExerciseConservativeForce1.pdf">Conservative Force</a>.<br>
<br>

```{solution-end}
```
```{solution-start} 53
:class: dropdown
```
Click for the solution <a href="Solutions/ExerciseConservativeForce2.pdf">Non-Conservative Force</a>.<br>
<br>

```{solution-end}
```
```{solution-start} 54
:class: dropdown
```
Click for the solution <a href="Solutions/PotentialEnergyxy.pdf">Potential energy & Force</a>.<br>
<br>

```{solution-end}
```
```{solution-start} 55
:class: dropdown
```
Click for the solution <a href="Solutions/ForceField.pdf">Force Field</a>.<br>
<br>


```{solution-end}
```
```{solution-start} 56
:class: dropdown
```
Click for the solution <a href="Solutions/ForceSin.pdf">Sinusoidal Force Field</a>.<br>
<br>
```{solution-end}
```



