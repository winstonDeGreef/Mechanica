# Oscillations 

## Periodic Motion

There are many, many examples of periodic systems. We see them in physics, like the orbit of planets around their star. We find them in biology (like the predator-prey systems), in chemistry (oscillating reactions like the [Belousov-Zhabotinsky reaction](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction)), and in economics (like demand-supply fluctuations). They show up in daily life: the day-night rhythm, the tides, children on a swing, your heart-beat. Periodic motions are by definition motions that repeat themselves after a fixed period of time, usually called 'the period'.

A specific class of periodic motion is known as oscillatory motion, or simply oscillations. All oscillations are periodic, but not all periodic motions are oscillations. An oscillation involves movement back and forth around an equilibrium position. It is typically caused by a restoring force: a force that acts to return the system to equilibrium (in case of the mass spring system: $\vec{F}=-k\vec{u}$). However, due to inertia, the system overshoots this position. The restoring force then reverses direction, pushing the system back again, leading to continued oscillation.

A few simple examples will illustrate the above. 

### The merry-go-round

The merry-go-round ({numref}`fig:HaMerryGoRound.jpg`) is a periodic motion, but not an oscillation. The seats go round in a circular, periodic motion but there is no back & forth. This is in contrast to a swing. That is also a periodic motion, but it has the back and forth as well as a restoring force, which in this case is gravity.

```{figure} images/MerryGoRound2.jpg
:name: fig:HaMerryGoRound.jpg
:width: 320px
:align: center
 
Spinning carousel. By Oxana Mayer, from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Spinning_around_-_geograph.org.uk_-_404365.jpg), licensed under CC BY-SA 2.0.
```

```{warning}
Extension of the physics of the merry go round needed. 
```

### Rabbits and Foxes

As an example of a dynamic system that is periodic, we will take a look at the so-called predator-prey systems. These are well-known in biology and provide an interesting case. The idea is simple: the populations of rabbits growth as they multiply quickly. The idea in the prey-predator model is that growth rate is proportional to the population itself. For the rabbits that means that the derivative of the population of rabbits (with respect to time) is positive. If there are no foxes, the rabbit population will grow exponentially. Of course, in the real world that doesn't happen as sooner or later, the rabbits will ran out of food, resulting in starvation. However, we will assume here, that food is not limiting: but the number of foxes is. They stop the rabbit population from unbounded increasing. The more rabbits there are, the easier the foxes find food and the more foxes will survive childhood. A simple model reads as follows:

$$\begin{split}
\frac{dr}{dt} &= \lambda_r r - \mu_r r \cdot f \\
\frac{df}{dt} &= - \lambda_f f + \mu_f r \cdot f
\end{split}$$

here $r$ and $f$ represent the rabbit and fox population, resp. $\lambda_r$ is the growth rate of the rabbits: the more rabbits, the larger the offspring. The higher $\lambda_r$ the more babies per rabbit. $\mu_r$, on the other hand, represents the effectiveness of the hunting foxes: the larger this value the more rabbits they kill. Of course: more rabbits, but also more foxes also means more kills. Similar arguments apply to $\lambda_f$ and $\mu_f$. Note that the term with $\lambda_f$ carries a negative sign: the net increase of the fox population is negative if there is insufficient food, that is, by itself more foxes die then that are born if there is no food.

This is clearly a coupled and dynamic system. It is non-linear due to the product $r \cdot f$, making it much more difficult to solve analytically then linear versions. In literature, this kind of system is known as Lotka-Volterra or prey-predator models. Below is a plot of the numerical solution of the rabbit and fox population (for $( \lambda_r, \mu_r,\lambda_f, mu_f) = (0.2, 0.03, 0.1, 0.01) $ and initial conditions ($r_0$, $f_0$) = (80, 2)).

```{figure} images/RabbitsAndFoxes.png
:name: fig:RabbitsAndFoxes.png
:width: 400px
:align: center
 
Periodic time evolution of the population of rabbits and foxes.
```

The solution is periodic. This can be illustrated better by plotting $f$ against $r$. The animation below shows this (this kind of plot is called a phase plot). 

```{figure} images/rf_animation.gif
:name: fig:rf_animation.gif
:width: 400px
:align: center
 
Phase plot of the rabbit-fox prey-predator model. The red dot shows the population at different times. Note that the number of rabbits quickly increases when there are very few foxes. However, at some point the number of foxes also goes up and soon the start reducing the rabbits, while increasing in numbers themselves. That is not sustainable and when the number of rabbits is brought down substantially, als the number of foxes decreases, until both are almost extinct and the cycle repeats.
```

#### Wilberforce Oscillator
As a second example we look at the Wilberforce pendulum. This is a spring, suspended vertically, to which a weight is fixed at the free end. The weight can go up and down but also rotate in a horizontal plane. A sketch is given below. 

```{figure} images/WilberforceSketch.png
:name: fig:WilberforceSketch.png
:width: 150px
:align: center
 
Wilberforce pendulum.
```

Image that we pull $m$ a little down and let go. The spring will try to restore the position of the mass to the equilibrium position it was in prior to us pulling $m$ down. Consequently, $m$ will start oscillating in the vertical direction. However, something peculiar happens: the mass $m$ also starts to rotate (around the vertical axis). And also this rotation turns out to be a back and forth oscillation. But that is not all: the two oscillations are coupled: they feed each other. If the vertical oscillation is at a maximum amplitude, the rotational motion is almost zero and vice-versa.

Click [Wilberforce](https://www.youtube.com/watch?v=WKySfr0e6P8) to see a youtube video of this oscillator.  

The system can be modeled with simple means. We will just postulate them. Later on, we will see where the terms come from.  
First, we note that the mass has kinetic energy, in two forms: due to the vertical motion ($\frac{1}{2}m\dot{z}^2$) and due to the rotational motion ($\frac{1}{2}I\dot{\theta}^2$). Don't worry about the exact meaning for now.  
Second, the mass has potential energy. We will ignore gravity (and pretend we do this experiment ins SpaceLab). A potential energy is associated with the vertical motion and is the spring energy: $V_z = \frac{1}{2}kz^2$, with $z$ the vertical position of the mass with respect to the equilibrium position, which we took as $z=0$. $k$ is the spring constant and represents the strength of the spring. We will come back to this later.  
Then, we have potential energy associated with the rotation: $V_\theta = \frac{1}{2} \delta \theta^2$. $\theta$ represent the rotation angle, where we have taken $\theta = 0$ in the equilibrium position. $\delta$ is the torsional spring constant: it represents how strongly the spring tries to push back against rotation.  
Finally, the vertical position and the rotation influence each other. That can be understood by realizing that if you shorten the spring, the spring material has to go somewhere. It can not only change its vertical length as that would mean that the total length of the spring would reduce. But that would compress the spring material and that is not possible for solid material (unless you apply incredibly large forces). The spring just increases its number of windings a bit. But that implies rotation. Similarly, if we only rotate the spring, it will try to adjust its length. As a consequence, there is also a potential energy involved in the influencing of $z$ and $\theta$ of each other. It can be modeled as $V_{z\theta} = \epsilon z \theta$.

If we ignore friction, then we have a system that can be described in terms of energy:

$$\frac{1}{2}m\dot{z}^2 + \frac{1}{2}I\dot{\theta}^2 + \frac{1}{2}kz^2 + \frac{1}{2}\delta \theta^2 + \epsilon z \theta = E_0 $$

From this, we can find 'N2', the equation of motion:

$$\begin{split}
m\ddot{z} &= -kz - \epsilon \theta \\
I\ddot{\theta} &= -\delta \theta - \epsilon z
\end{split}$$

Don't worry, if you don't follow this. The point here is, that we have a coupled system of two oscillators. This can be solved numerically.

We could use a simple numerical scheme like we have employed in Chapter 3. In the figure below $z(t)$ and $\theta (t)$ are shown using such a simple numerical scheme.


```{figure} images/WilberforceEuler.png
:name: fig:WilberforceEuler.png
:width: 450px
:align: center
 
Numerical solution of the Wilberforce pendulum using a (too) simple numerical method.
```

We indeed see the oscillating motion and that the vertical oscillation changes over to rotation and back again.

But there is something really disturbing: the amplitude of our oscillation is increasing and it seems to do so for every cycle. That cannot be true: It violates energy conservation. What did we do wrong? Well, our numerical method is just not good enough. If we use again a higher order method, we obtain the results in the figure below.


```{figure} images/WilberforceHigherOrder.png
:name: fig:WilberforceHigherOrder.png
:width: 450px
:align: center
 
Numerical solution of the Wilberforce pendulum using a higher-order numerical method.
```

Now the amplitude of the oscillations stays nicely constant, obeying conservation of energy.

In the figure below a small animation can be seen: the marker in both graphs shows $z$ and $\theta$ at the same time instant.

```{figure} images/Wilberforce_animation.gif
:name: fig:Wilberforce_animation.gif
:width: 450px
:align: center
 
Animation of the Wilberforce pendulum using a higher-order numerical method.
```

The Wilberforce pendulum is clearly periodic. Moreover, it is an oscillation as there is back and forth motion around an equilibrium.

But, it does give us a **big warning**: (numerical) solutions always have to be **assessed** against the features and principles of the problem at hand. In this case, our first numerical solution could not be right: **it violated energy conservation**. We were able, right from the start, to formulate the problem in terms of energy. SInce we only had kinetic energy and potential energy we **knew up front** that the motion must be bounded!   
That is why, we need a thorough understanding of physics. It is not sufficient to have the equations and put them in a 'solver'. It is the job of a physicist to understand and assess models, outcomes, etc against the laws of physics. Hence, we will dive into oscillations, starting from the beginning. 

## Harmonic Oscillation - archetype: Mass-Spring
The archetype of an oscillation is the mass-spring system. It is the simplest version (simpler than the pendulum as we will see). And it can be recognized in many systems. We consider the following: a mass is attached to a spring. The other end of the spring is fixed. The mass can only move in one direction: the $x$-direction. The spring has a natural or rest length $l_0$. That is the length of the sphere if no force is acting on it. It we pull the spring, it will exert a force that is proportional to the increase in length. Moreover, it is pointing in the direction opposite to the lengthening. In formula:

$$F_v = - k (l - l_0 ) = -k \Delta l $$

This is shown in the figure below.

```{figure} images/MassSpring.png
:name: fig:MassSpring.png
:width: 300px
:align: center
 
Mass-spring system: archetype of a (harmonic) oscillation.
```

The response of the spring is to exert a force on $m$ proportional to its elongation (which may be negative). It is clearly a restoring force: no matter what we do pulling or pushing, the spring will always counteract.

It is not difficult to set up N2 for the mass-spring. There is only one force and the system is 1-dimensional. If we define the origin at the position of the mass when the spring is at its rest length, then $\Delta l$ - the elongation of the spring - becomes $x$, the coordinate of the mass $m$. Thus N2 reads as:

$$ m\ddot{x} = -kx $$

Or 

$$ m\ddot{x} + kx = 0 $$

To solve this, we need two initial condition. Let's take $t=0: x(0) = x_0, v(0) = 0$. We need to find a function $x(t)$ that upon differentiating twice it spits itself back but with an opposite sign. We do know two functions that do so: $x(t) = \sin ( \omega_0 t)$ and $x(t) = \cos ( \omega_0 t)$. Thus, the general solution of the above equation is known.

<div style = "background-color: rgb(235,235,235); border: solid black; font-size: 21px; color:blue">

&nbsp;&nbsp;&nbsp;&nbsp;Harmonic Oscillator:

$$ m\ddot{x} + kx = 0 \Leftrightarrow x(t) = A \sin \omega_0 t + B \cos \omega_0 t$$

</hr>
</div>  

If we insert the solution, we find 
<div style = "background-color: rgb(235,235,235); border: solid black; font-size: 21px">

$$\omega_0^2 = \frac{k}{m} $$

</div>  

This is called the natural frequency of the oscillator. Note, that it does not depend on the initial conditions. No matter what, the mass will always oscillate with this frequency.

It does make sense that the frequency is inversely proportional to m: we expect a heavy object will response slow to a force. Similarly, if the spring is strong, that is has a high spring constant $k$, it will move the mass around quickly.

If we substitute the initial condition, we can completely solve the motion of the mass:

$$\begin{split}
&m\ddot{x} + kx = 0 \Rightarrow x(t) = A \sin \omega_0 t + B \cos \omega_0 t \Rightarrow \\
\\
&\begin{cases}
v(0 = \dot{x}(0) = 0 \rightarrow A \omega_0 \underbrace{\cos 0}_{=1} - B \omega_0 \underbrace{\sin 0}_{=0} = 0 \rightarrow A = 0 \\
x(0) = \Delta x \rightarrow B \cos 0 = \Delta x 
\end{cases} \\
\\
&\Rightarrow x(t) = \Delta x \cos \sqrt{\frac{k}{m}} t
\end{split}$$

A system is called a harmonic oscillator if and only if it obeys $m\ddot{x} + kx = 0$. You will find them in almost every branch of science and engineering. The reason why will become apparent in a moment.

### Potential energy of a spring
In the above, we have formulated the mass-spring system in Newton's second law. We can, however, also cast it in the form of energy. The force of the spring is conservative. We can easily prove this by finding the associated potential energy: $F_v = -\frac{dV}{dx}$.   
Since $F_v = -kx$ we need to find a function $V(x)$ that satisfies $\frac{dV}{dx} = kx$. Let's do it:

$$ \frac{dV}{dx} = kx \Rightarrow V(x) = \frac{1}{2} x^2 + C $$

We have the freedom to decide ourselves where we want the potential energy to be zero. Note: $V$ is quadratic.   
It does make sense, to set the minimum of the potential energy such that if the mass is at the equilibrium position, the potential energy is zero, that is - take $C=0$:

$$ V(x) = \frac{1}{2}kx^2 $$

Thus the mass-spring system can also be described by 

$$ \frac{1}{2}mv^2 + \frac{1}{2}kx^2 = E_0 $$

So, an other way of stating what a harmonic oscillator is: it is a system that obeys the above energy equation.

## Behavior around an equilibrium point and harmonic oscillators
Now we will go back to paragraph 5.5.1, where we discussed the Taylor series expansion of the function $f(x)$: 

$$
f(x) \approx f(x_0) + f'(x_0) (x-x_0 ) + \frac{1}{2} f''(x_0) (x-x_0)^2 + \mathcal{O}(x^3)
$$

We will apply it to a potential energy $V(x)$ of some system. We assume that the system has a stable equilibrium point at $x=x_0$, that is $\left [ \frac{dV}{dx} \right ]_{x=x_0} = 0$
and $\left [ \frac{d^2V}{dx^2} \right ]_{x=x_0} > 0$.  
Thus, we can expand the potential as follows:

$$
V(x) \approx V(x_0) +\frac{1}{2} \underbrace{\left [ \frac{d^2V}{dx^2} \right ]_{x=x_0}}_{=k} (x-x_0 )^2 + \mathcal{O} \left [ (x-x_0 )^3 \right ]
$$

If we plug this in, in the energy equation and cut off after the quadratic term, we find 

$$\frac{1}{2}mv^2 + V(x_0) +\frac{1}{2} \underbrace{\left [ \frac{d^2V}{dx^2} \right ]_{x=x_0}}_{=k} (x-x_0 )^2 = E_0 $$

or shortened by the abbreviation $\left [ \frac{d^2V}{dx^2} \right ]_{x=x_0} = k$

$$\frac{1}{2}mv^2 + V(x_0) +\frac{1}{2}k ((x-x_0)^2 = E_0$$

Move the constant $V(x_0)$ to the right hand side and change coordinate $ s \equiv x-x_0 \rightarrow \dot{s} = \dot{x} = v$. This gives us:

$$ \frac{1}{2}m\dot{s}^2 + \frac{1}{2}ks^2 = C $$

The harmonic oscillator!!! 
No wonder we find harmonic oscillators 'everywhere'. Any system that has a stable equilibrium point with a positive second derivative of its potential will start to oscillated as a harmonic one if we push it a little bit out of its equilibrium position. Doesn't matter how $V(x)$ exactly is. It doesn't have to be quadratic in $x$. But it will be pretty close to that, if we stay close enough to the equilibrium point. Hence, any small natural kick, any small amount noise will push a system out of its stable equilibrium point into an harmonic oscillating motion with a given, natural frequency given by $\omega_0^2 = \frac{\left [ \frac{d^2V}{dx^2} \right ]_{x=x_0}}{m}$.
    

## Examples of Harmonic Oscillators
### Torsion Pendulum
We take a straight metal wire. Suspend one end at the ceiling and attach a disc of radius $R$ and mass $m$ at the other end.

```{figure} images/TorsionPendulum.png
:name: fig:TorsionPenduluming.png
:width: 150px
:align: center
 
Torsion Pendulum.
```

The disk can rotate about a vertical axis. We call the rotation angle $\theta$. The equilibrium position is $\theta = 0$. If we rotate the disc over a small angle, the wire will resist and apply a torque $\Gamma$ on the disc trying to rotate the disc back to its equilibrium position, for which the torque, obviously is zero.

For small angles, the torque is proportional to the rotation angle and -of course -working in the direction opposite of the rotated angle. We can set up an angular momentum equation and find that it reads as:

$$ I \frac{d^2\theta}{dt^2} = - k_t \theta $$

In this equation, $I = \frac{1}{2}mR^2$ is the moment of inertia of the disc  and $k_t$ is the torsion constant of the wire. Don't worry about the exact meaning of the terms in the equation. For now, we focus on the equation itself:

$$ I \frac{d^2\theta}{dt^2} + k_t \theta = 0 \Rightarrow \theta (t) = A \sin \omega_0 t + B \cos \omega_0 t$$

The torsion pendulum is a harmonic oscillator, 
$\omega_0^2 = \frac{k_t}{I}$, completely analogous to the archetype, mass-spring. Obviously, we thus can also write this in terms of energy: 

$$ \frac{1}{2} I \omega^2 + \frac{1}{2}k_t \theta^2 = E_0 $$

with $\omega \equiv \frac{d\theta}{dt}$, the angular velocity.
  


### L-C circuit
In Electronics alternating current (AC) circuits are building blocks of many complex systems. One of these is the L-C circuit, in which an inductor, $L$, and a capacitor, $C$, are in series coupled. See {numref}`fig:LCcircuit.png`.

```{figure} images/LCcircuit.png
:name: fig:LCcircuit.png
:width: 150px
:align: center
 
L-C circuit.
```

We could charge the capacitor and then close the circuit. What would happen? The capacitor will try to discharge via the inductor. Hence a current, $I$, starts flowing. In response, the inductor builds up a potential difference that is directly proportional to the rate of change of the current through the inductor. 

Basic electronics shows that the voltage over the capacitor is coupled to the charge, $Q_C$, of the capacitor according to: $V_C = \frac{Q_C}{C}$. For the inductor we have: $ V_L = L \frac{dI_L}{dt}$.

According to Kirchhoff's laws the current through both elements must be the same: $I_C = I_L$ and the sum of the voltages across them must be equal to zero: $V_c + V_L = 0$. If we put everything together, we get - using $I_C = \frac{dQ_c}{dt}$:

$$\begin{split}
V_L + V_C &= 0 \Rightarrow \\
\frac{dV_L}{dt} + \frac{dV_C}{dt} &= 0 \Rightarrow \\
L \frac{d^2 I}{dt^2} + \frac{1}{C}I &= 0 \Rightarrow \\
\frac{d^2I}{dt^2} + \frac{1}{LC} I &= 0 \text{ Harmonic Oscillator!!!}
\end{split}$$

As we see, this LC-circuit will start to oscillate. In the animation below the current through the circuit and the voltage across the inductor are shown for $C = 1 \mu F$ and $L = 1 \mu H$.

```{figure} images/LC_animation.gif
:name: fig:LC_animation.gif
:width: 400px
:align: center
 
Harmonic oscillation of an LC-circuit.
```

### Musical Instruments

Musical instruments produce sound waves. In many cases they do that via vibrations of strings, like the guitar, the violin, harp or piano. The strings of these instruments are displaced out of their equilibrium position. Due to the tension in these strings, there is a restoring force that is proportional to the displacement. Consequently, the string will start to oscillate in an harmonic way. 

Not only strings, but also beams will exhibit this behavior, well-known example: a tuning fork. We will come back to waves at the end of this chapter.

## The pendulum

Another example of oscillatory motion is the pendulum. In its most simple for it is a point-mass $m$, attached to a massless rod of length $L$. The rod is fixed to a pivotal point that allows it to swing freely.

```{figure} images/Pendulum.png
:name: fig:Pendulum.png
:width: 200px
:align: center
 
Sketch of a pendulum by Huygens (public domain).
```

On the mass, gravity is acting vertically downwards. Also the rod exerts a force on the mass. This force is always parallel to the rod and points to the pivotal point. It is the response of the rod to the component of gravity  parallel to the rod (the dark blue arrow in {numref}`fig:Pendulum.png`). It is good to realize, that this force makes sure that the distance from $m$ to the pivotal point is always $L$. In other words, this force is a consequence of the fixed length $L$ of the rod. It is the physics translation of the constraint: $L$ is constant.

### N2 for the pendulum: Equation of motion via N2

We will set up Newton's second Law for $m$. 

$$ m\frac{d\vec{v}}{dt} = -mg\hat{z} + \vec{F}_t $$

As stated above, the blue, parallel part of gravity is balanced by a tensional force in the rod. So, we don't need to worry about motion of $m$ parallel to the rod. That leaves us with the direction perpendicular of the rod. In that direction only the red arrow works on $m$. 

In the other direction only the red, perpendicular component of gravity acts on $m$. This component is equal to $-mg \sin \phi $. The velocity component in this direction is $v = r\frac{d\phi}{dt}$. Thus we get:

$$ m L \frac{d^2 \phi}{dt^2} = -mg \sin \phi $$

Or rewritten 

$$ m L \frac{d^2 \phi}{dt^2} + mg \sin \phi =0 $$

We do know from experience that the pendulum will swing back and forth in a periodic way. However, as we see from the above equation of motion: it is not a harmonic oscillator. The term with the sin prevents that.

But for small values of the angle $\phi$, that is for small oscillations around the stable equilibrium $\phi_{eq} = 0$, we can approximate the sinus via a Taylor series and write: 

$$ \begin{split}
\phi \ll 1 \Rightarrow\sin \phi &\approx \sin 0 + \frac{1}{1!} \cos 0 \: \phi - \frac{1}{2!} \sin 0 \: \phi^2 + ...  \\
&\approx \phi
\end{split} $$

Thus within this approximation we can write for the equation of motion of the pendulum:

$$m L \frac{d^2 \phi}{dt^2} + mg \phi =0 \Rightarrow \frac{d^2 \phi}{dt^2} + \frac{g}{L} \phi =0$$

and that describes a harmonic oscillator.

We conclude that for small amplitudes of the oscillation, the pendulum is an harmonic oscillator and swings in a sin or cos way back and forth. Moreover, the oscillation has a frequency 

$$ \omega_{pendulum}  = \sqrt{\frac{g}{L}}$$

Further, note that under this assumption, the period of the pendulum does not depend on the amplitude of the oscillation. That was already noted by Galileo Galileï. 

### N2 for the pendulum: Equation of motion via Angular Momentum

Before we continue with the analysis of the pendulum, we will derive the equation of motion also via angular momentum considerations. On $m$ gravity exerts a torque: $\Gamma = \vec{r} \times \vec{F}_g$ It has a magnitude $-Lmg \sin \phi$ and points into the screen. The angular momentum of $m$ is given by $\vec{L} = \vec{r} \times \vec{p}$. This has magnitude $ mL^2\frac{d\phi}{dt}$ and also points into the screen.

Thus N2 for angular momentum gives us:

$$ \frac{d\vec{L}}{dt} = \vec{\Gamma} \Rightarrow mL^2\frac{d^2\phi}{dt^2} = -Lmg \sin \phi$$

Thus, angular momentum leads to the same equation of motion.


### The Pendulum via energy conservation

Alternatively, we can also use energy conservation to derive the equation governing the motion of the pendulum. There are, as discussed above, two forces acting on $m$. The first one is gravity, which is a conservative force with associated potential energy. We can write for this case $V_g = mgz$, taking $V_g (z=0) = 0$. 

The second one is the force from the rod. But this one always acts perpendicular to the motion of $m$. Hence, it does not do any work and, thus, we don't need to worry about an associated potential.

We conclude that for the pendulum it holds that:

$$ \frac{1}{2}mv^2 + mgz = E_0 $$

To solve this, we change from $z$ to $\phi$. $z$ is, in terms of $\phi$: $L - L\cos\phi$, see {numref}`fig:PendulumEnergy.png`.

```{figure} images/PendulumEnergy.png
:name: fig:PendulumEnergy.png
:width: 250px
:align: center
 
Potential energy of a pendulum.
```

Thus, our energy equation reads as:

$$\frac{1}{2}m v_\phi^2 + mgL \left (1 - \cos \phi \right ) = E_0 $$

or 

$$\frac{1}{2}m v_\phi^2 - mgL \cos \phi = E_0 - mgL $$

Take the time-derivative and use $v_\phi = L\frac{d\phi}{dt}$ and we get

$$ \begin{split}
mv_\phi \frac{dv_\phi}{dt} + mgL \sin \phi \frac{d\phi}{dt} &= 0 \Rightarrow \\
mL \frac{d\phi}{dt} \frac{d}{dt} \left ( L \frac{d\phi}{dt} \right ) + mgL \sin \phi \frac{d\phi}{dt} &= 0 \Rightarrow \\
\frac{d^2\phi}{dt^2} + \frac{g}{L} \sin \phi &= 0
\end{split} $$

And we have recovered the same equation of motion.

### Pendulum for not so small angles

In the above we have frequently used the approximation $\sin \phi \approx \phi $ for $\phi \ll 1$. What about the general case? Then we need to solve 

$$ \begin{split}
\frac{d^2\phi}{dt^2} + \frac{g}{L} \sin \phi &= 0 \\
\text{ with i.c. } \phi(0) = \phi_0 \text{ and } \frac{d\phi}{dt} = \dot{\phi}_0
\end{split} $$

This equation is much more difficult to solve analytically and we will, therefore, use a numerical approach here. The animation below compares the motion of the pendulum numerically simulated to that of the pendulum when using the small amplitude approximation. 

The animation shows: a green mass, that is the pendulum with a (fixed) small amplitude in the approximation $\sin \phi = \phi$. The blue one uses the same approximation even though  $\phi$ is not small. Notice, that blue and green oscillate with exactly the same frequency. This is, of course, trivial as they obey the same harmonic oscillation equation and thus have the same frequency.

The red mass, on the other hand obeys the equation of motion of the pendulum leaving the term with $\sin \phi$. It is clear that the real pendulum (i.e. the red one) does not have the same frequency as the others. Moreover, its time trace (left part of the figure) is clearly not a true sinus.

```{figure} images/Pendulum_animation.gif
:name: fig:Pendulum_animation.gif
:width: 600px
:align: center
 
Animation of the pendulum: red is the true pendulum, blue the small angle approximation applied to a large angle case and green the small angle approximation for a small angle.
```

In the widget below, you can vary the initial angle and observe that indeed for a small angle the red mass and the other two follow the same trajectory. But if you increase the initial angle, the red mass behaves differently: it oscillates slower and the time trace of angle as a function of time is no longer sinusoidal.


```{warning}
<!-- <embed width = "100%" height = "500" frameborder="0" scrolling="yes" src="../_static/Widgets/PendulumWidget.html"> 

[Or open the widget full screen](../_static/Widgets/PendulumWidget.html) -->
```

## The damped harmonic oscillator ##
In the above, no friction of any form has been considered. However, in many practical cases friction will be present. For moving objects friction frequently depends on the velocity: the higher the velocity, the higher the frictional force. We will here consider the simplest version: a friction force that is directly proportional to the velocity: $F_f = -b v$ with $b$ a positive constant. Thus, we need to add an additional force to our harmonic oscillator:

$$ m\ddot{x} = -k x - b \dot{x} $$

or bringing all terms to the left hand side:

$$ m\ddot{x} + b \dot{x} + kx = 0 $$

To solve this equation, it is easier not to try to look directly for sinus and cosins, but use the complex notation. 


```{intermezzo} Intermezzo: complex exponential and sin, cos 

In the 18$^{th}$ century, the study of complex numbers, i.e. $i = \sqrt{-1}$, revealed a surprising connection between the exponential function and trigonometry. It was Leonhard Euler (1707-1783) who derived:

$$e^{ix} = \cos x + i \sin x $$

If you want to understand this a bit further, write down the Taylor expansion of all three functions. By realizing that $i^2 = -1, i^3 = i^2 i = -i$, etc. You will see that Euler was right.

We can use the above equation to write $\sin x$ and $\cos x$ as exponential functions:

$$\begin{split}
\sin x & = \frac{e^{ix} - e^{-ix}}{2} \\
\cos x & = \frac{e^{ix} + e^{-ix}}{2} 
\end{split} $$

And we can also state that the real part of $e^{ix}$ is equal to $\cos x$ and the imaginary part to $\sin x$.

The above turns out to be extremely useful in solving differential equations. For instance, rather than trying $\sin$ and $\cos$ as solutions for the harmonic equation $m\ddot{x} + kx = 0$, we could try $e^{i\omega t}$ (please note: x in the first part of this intermezzo is just a real number, whereas now x is the amplitude of the oscillator and is a function of $t$):

$$
m\ddot{x} + kx = 0 \Rightarrow \\
m \frac{d^2 Ae^{i\omega t}}{dt^2 }+ k A e^{i\omega t} = 0 \Rightarrow\\
Am (i\omega)^2 e^{i\omega t} + Ak e^{i\omega t} = 0 \Rightarrow \\
Ae^{i\omega t} \left ( -m\omega^2 +k \right ) = 0 \;\;\;\;\forall t
$$

Thus we conclude that if $Ae^{i\omega t}$ is a solution of the harmonic equation, then $\omega^2 = \frac{k}{m}$. So, with that condition, $Ae^{i\omega t}$ is a solution with $A$ an integration constant that will be fixed by proper initial conditions.

But let's be careful: the harmonic oscillator is governed by a second order differential equation, that is we have differentiated twice with respect to time. Thus we need to integrate also twice, leaving us with 2 rather than 1 integration constant. Hence, we have not found the general solution, yet.

That can be easily cured: if $Ae^{i\omega t}$ is a solution, the $Be^{-i\omega t}$ is one as well. And here is our second solution, with the same condition for $\omega$. And our general solution is 

$$x(t) = Ae^{i\omega t} + Be^{-i\omega t} $$

Note that $A$ and $B$ are complex numbers and thus, we can always rewrite this equation back into $\sin (\omega t)$ and $\cos  (\omega t)$. But in most cases we don't worry about that. We ar interested in the 'rule' for $\omega$ and once we have that, we can write our solution straightaway as $x(t) = C\cos (\omega t) + D \sin (\omega t)$.

Let's use this for the damped harmonic oscillator:

$$m \ddot{x} + b \dot{x} + kx = 0 $$

Try $x(t) =A e^{i \omega t}$.

$$ \Rightarrow Ae^{i\omega t} \left ( -\omega^2 m + i \omega b + k \right ) = 0 \;\;\;\;\; \forall t \Rightarrow\\
\omega^2 m - i \omega b - k = 0 \Rightarrow \\
\omega_{+,-} = \frac{+ib \pm \sqrt{-b^2+4mk}}{2m}
$$

We immediately have our two solutions: one with the $+$sign, the other with $-$sign:

$$x(t) = A e^{i\omega_+ t} + B  e^{i\omega_- t} $$

with both $\omega$'s complex numbers.

Alternatively, we could have started with $x(t) = e^{\lambda t}$, but allowing $\lambda$ to be a complex number. This somewhat easier and as we have seen above, $\omega$ is a complex number ($D = -b^2+4mk$ can be negative). This will gives us:

$$ m\lambda^2 + b\lambda + k = 0 \Rightarrow \lambda_{+,-} = \frac{-b \pm \sqrt{b^2 - 4mk}}{2m} $$

We see, that $\lambda$ always has a negative real part. That makes sense: the negative real part shows that the solution is damped.

Our solution to the damped harmonic oscillator is thus:

$$ x(t) = A e^{\lambda_+ t} + B e^{\lambda_- t} $$
```

The general solution of the (linearly) damped harmonic oscillator is:

$$ m\ddot{x} + b \dot{x} + kx = 0 \Rightarrow \\
\; \\
x(t) = A e^{\lambda_+ t} + B e^{\lambda_- t} \\
\; \\
\text{with} \\
\; \\
 \lambda_{+,-} = \frac{-b \pm \sqrt{b^2 - 4mk}}{2m}
$$

We will investigate various cases.

::::{tab-set}
:::{tab-item} **Case 1** $D = b^2 - 4mk \lt 0$

In this case, the square root in $\lambda$ is imaginary and we can write it as $i\sqrt{4mk - b^2}$. This gives us for the two possibilities of $\lambda$

$$ \lambda_+ = -\frac{b}{2m} + i \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}} \\ 
\;\\
\lambda_- = -\frac{b}{2m} - i \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}} 
$$

Both have the same real part: $-\frac{b}{2m}$ showing that both solutions are damped (with the same factor!). Moreover, the imaginary parts are equal, apart from the sign which we also had in the undamped case. We will write the imaginary part as $\omega$ (that is without the subscript 0 we used for the undamped case). 

So, our solution reads as:

$$ x(t) = \underbrace{\left ( A e^{i\omega t} + B e^{-i\omega t} \right )}_{sinusoidal \; oscillation} \underbrace{e^{-\frac{b}{2m} t}}_{exponential damping}
\; \\
\; \\
with \\
\; \\
\omega \equiv \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}} \lt \sqrt{\frac{k}{m}} = \omega_0
$$

Conclusion: the damped oscillator oscillates with a smaller frequency than the undamped one and it amplitude decreases over time. The later is of course to be expected due to friction: sooner or later friction has dissipated all the kinetic \& potential energy.
:::

:::{tab-item} **Case 2** $D = b^2 - 4mk = 0$
For this specific combination of $b, k, m$ we see that the frequency of the oscillation is 0. In other words, the systems does not perform oscillations. Furthermore, our two values of $\lambda$ are now equal. Consequently the general solution that we presented is no longer complete (we now only have one integration constant, or only one independent function if you prefer.) We need a second one and that turns out to be of the form $t e^{\lambda t}$. You can verify that by substituting it in the equation of motion for the damped case.

Thus we have know:

$$ D = b^2 - 4mk = 0 \Rightarrow \\
\;\\
x(t) = \left ( A + B t \right ) e^{-\frac{b}{2m} t}
$$

:::

:::{tab-item} **Case 3** $D = b^2 - 4mk \gt 0$
Again, there is no imaginary part in $\lambda$, so no oscillations. But we do have two different values for $\lambda$ and thus our original general solution is still valid:

$$ x(t) = A e^{\frac{-b + \sqrt{b^2 - 4mk}}{2m}t} + Be^{\frac{-b - \sqrt{b^2 - 4mk}}{2m}t}
$$

Note that $ -b + \sqrt{b^2 - 4mk} \lt 0 $. So, both terms are decreasing to zero: the motion comes to a stop as $t \rightarrow \infty$.

Further, note that the first part (with $A$) has an exponent that is closer to zero than the one of the other part (with $B$). Thus the second part will decay faster and for sufficiently large $t$, the solution behaves like $A e^{\frac{-b + \sqrt{b^2 - 4mk}}{2m}t}$.

In the figure below, an example of case 1 and case 3 is shown together with the solution of case 2. We see, that case 2 is the one that decays fastest: it has the highest damping coefficient in its exponent. This is called critical damping. If you need to dampen unwanted oscillations: make sure you tune your damping parameter b such that $b^2 - 4mk = 0$.

```{figure} images/DampedOscillatorPlot.png
:name: fig:DampedOscillatorPlot.png
:width: 400px
:align: center
 
Different cases for the damped harmonic oscillator.
```
:::
::::

### Evolution of the damping

Here we will have a quick look how the damping is evolving, that is we look at the root of the characteristic equation

$$
\lambda_{1/2} =\frac{-b \pm \sqrt{b^2 - 4mk}}{2m} 
$$

and see how it evolves as a function of the damping $b$ in the complex plane.

```{figure} images/polezero.png
:name: fig:polezero.png
:width: 400px
:align: center
 
Evolution of $\lambda$ as a function of $b$ in the complex plane.
```


This gives quickly a qualitative view on the different regimes of the damping. The root $\lambda_{1/2}$ is in general complex. We start by looking at the value for roots $\lambda_{1/2}$ as a function of the damping $b$

- No damping: $b=0$. The root is pure imaginary $\lambda_{1/2}=\pm i\sqrt{k/m}$ with two conjugate solutions on the imaginary axis. This gives pure oscillations.
- Some damping $0<b<\sqrt{4mk}$. The root is complex, with real and imaginary part, the oscillation will damp out over time (shown in <span style="color:blue">blue, underdamped regime</span>).
- $b^2=4mk$. The roots collapse into one pure real root $\lambda=-b/2m$  (critically damped), no oscillation.
- Lots of damping $b>\sqrt{4mk}$. The root splits into two real roots, no oscillations (shown in <span style="color:orange">yellow, overdamped regime</span>).

The root walks over the shown graph from $b=0$ on the imaginary axis to $b\to\infty$ over the blue and then yellow part of the graph. The yellow graph does not cross the imaginary axis.

From this plot you can directly see that the system is stable for $b>0$, but unstable for $b=0$ without the need to check the frequency that the system is driven with (for $b=0$ driven with the resonance frequency results in an infinite amplitude - an instable system). How you can see that so quickly you will learn in the second year class *Systems and Signals*.


## Driven Damped Harmonic Oscillator

Oscillators sometimes experience a driving force that can be periodic in itself.  We will take here the case of a sinusoidal force with frequency $\nu$. Once we understand this, forces consisting of more than one frequency (broader spectrum) can be understood using Fourier analysis (which you will learn about classes like *Systems and Signals* or *Fourier Analysis* in math). There you will also learn to treat this system in more detail analytically. Here we will stick to a simple driving force of the form $F_{ext} = F_0 \sin (\nu t)$.

This gives for the equation of motion:

$$
m\ddot{x}  +b\dot{x} +kx=  F_0 \sin (\nu t)
$$

with initial conditions: at $t= 0$ the particle will have some position $x_0$ and some velocity $v_0$.

The solution of the driven damped harmonic oscillator equation of motion for the case $D = b^2 - 4mk < 0$ is:

$$
x(t) = A e^{- \frac{b}{2m} t} \sin \left ( \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}} t+ \epsilon \right ) +
              x_{max} \sin \left ( \nu t + \alpha \right )
$$

With $A$ and $\epsilon$ determined by the initial conditions.

The two other parameters $x_{max}$ and $\alpha$ are fixed. We will give only the expression for $x_{max}$:

$$
x_{max} = \frac{F_0}{\sqrt{\left ( \omega_0^2 - \nu^2 \right ) ^2 + \frac{b^2}{m^2} \nu^2}}
$$

For $t\to\infty$, the second part, i.e., the term from the driving force $x_{max} \sin \left ( \nu t + \alpha \right )$, survives as the exponential decay will have damped the first term. The oscillation will have frequency $\nu$ of the driving force. As can be seen, the amplitude of the motion is for longer times $x_{max}$. 

If the driving frequency $\nu\sim\omega_0$, the amplitude increases strongly. Especially for small damping, i.e., small $b$, the amplitude will increase to high values. This phenomenon is called *resonance*:

$$
\text{if  } b \rightarrow 0 \text{ and } \nu \rightarrow \omega_0 \text{  then  } x_{max} \rightarrow \infty \text{   resonance}
$$


## Coupled Oscillators

In this course we mostly only consider one oscillator, but of course there could be many that are coupled in one way or another. Already <a href="https://nl.wikipedia.org/wiki/Christiaan_Huygens">Christiaan Huygens</a> considered them.


```{figure} images/coupled_huygens.jpg
:name: fig:coupled_huygens.jpg
:width: 300px
:align: center
 
Huygens experiment of weakly coupled pendula.
```

There are 2 pendula suspended from a common connection, which rests on two chairs. If you set the pendula in motion, they will be initially *out of phase*, i.e. the relative position of the pendula is different. But over time their motion synchronises!  What has happend? Apparently the two pendula are connected, *coupled*, via the suspension and act on each other, they are not independent, but influence the motion of the other pendulum.

The video below shows a modern day version of this phenomena. 

```{iframe} https://www.youtube.com/embed/DD7YDyF6dUk?si=Zt65wJNNQCosMU5n"

Weakly coupled metronomes.
```



Here the pendula are coupled via the ground. This influence is called *weak coupling*. In this course we cannot treat this coupling mathematically, but in the second year course on *Classical Mechanics* you will learn to study systems like these.

## Examples

1. Example of resonance: sound waves are exciting a glass. By changing the frequency of the sound waves to the resonance frequency, the glass starts oscillating with increasing amplitude until it finally breaks.

```{warning}
<!-- <video controls muted="true" loop="true" width="90%">
    <source src="../_static/Movies/Resonance_GlassDestroyedbySound.mp4" type="video/mp4">
</video> -->
```

2. Driven harmonic oscillator with damping.

```{warning}
<!-- <embed width = "100%" height = "500" frameborder="0" scrolling="yes" src="../_static/Widgets/DrivenOscillator.html"> 

<a href="../_static/Widgets/DrivenOscillator.html">Or open the widget full screen</a> -->
```

3. 1940: the Tacoma Narrows Bridge in the state Washington on the West coast of the USA is brought into resonance by the wind. The end result: click the movie to see it yourself.

```{warning}
<!-- <video controls muted="true" loop="true" width="90%">
    <source src="../_static/Movies/tacoma_narrows1.mp4" type="video/mp4">
</video> -->
```

4. Breaking a HDD hard disk with a song of Janet Jackson

Read [here](https://devblogs.microsoft.com/oldnewthing/20220816-00/?p=106994?WT.mc_id=onedevquestion-c9-raymond) about this truly amazing piece of applied physics on a blog of Microsoft developer Raimond Chen.
    

5. The blue sky: Rayleigh scattering 
	
Light from the sun (and stars) will have to travel through the atmosphere before reaching the ground level. On
its way it will be subject to absorption and scattering.

When you look on a clear day into the sky its color is blue, everybody knows that. But few people know why. The reason is found in the scattering properties of the molecules: the probability of light being scattered by an air molecule is proportional to the wave length of the light to the power -4, or rephrased: proportional to $f^4$ ($f$ the frequency of the light, the theory of molecular scattering was given first given by Lord Rayleigh). Thus, blue light of a wavelength of 450nm is compared to red light ($\lambda$ = 650nm) $\left ( 650/450 \right ) ^4 = 4.4$ times more likely to be scattered. Consequently, the blue end from the (white) sun light has a reduced probability to reach our eye directly in comparison with the red end. And thus most of the scattered light that reaches us is blue: the sky is blue. 

We will look at scattering of light by considering a simple molecule made of a fixed nucleus with one electron orbiting it. The equation of motion of the electron can be written as that of a harmonic oscillator, with eigen frequency $\omega_0$:

$$
m\ddot{x} + kx = 0 \rightarrow \ddot{x} + \omega_0^2 x = 0
$$


```{figure} images/ElectronBlueSky.png
:name: fig:ElectronBlueSky.png
:width: 150px
:align: center
 
Simple model of electron-light scattering.
```

When light passes the electron, the electron feels a force since light is an electro-magnetic wave. The electric field is the dominating force. For light of wave length $\lambda$, i.e. angular frequency $\omega = 2 \pi f = 2 \pi \frac{c}{\lambda}$, the electric field can be written as $E_0 \sin \omega t$. Such a field will produce a force $F_e = e E_0 \sin \omega t$ on the electron, modifying its equation of motion to:

$$
\ddot{x} + \omega_0^2 x = \frac{e}{m} E_0 \sin \omega t
$$

We recognize this as the forced harmonic oscillator with solution

$$
x(t) = c_1 \sin \omega_0 t + c_2 \cos \omega_0 t + \frac{e E_0}{m} \frac{\sin \omega t}{\omega_0^2 - \omega^2}
$$

The important part is the last one: the extra motion cause by the passing electric field. This causes an additional acceleration of the electron: $a(t) = -\frac{e E_0}{m} \frac{\omega^2}{\omega_0^2 - \omega^2} \sin \omega t$. 

The electron in its original orbit does not radiate. However, due to the extra acceleration the electron starts radiating. It sends out an electromagnetic field with the wave length of the incoming light and an intensity proportional to the square of the acceleration, $\left < a(t)^2 \right >$, i.e. 

$$
I \propto \left [ \frac{\omega^2}{\omega_0^2 - \omega^2} \right ]^2
$$

As the eigen frequency $\omega_0$ of the electrons in oxygen and nitrogen is much higher than the frequency $\omega$ of the incoming light we have that this is basically proportional to $\left ( \frac{\omega}{\omega_0} \right )^4$. As this radiation by the electron obviously feeds on the incoming light, we find that the scattering of the light is proportional to the frequency of the incoming light to the power 4.

	
6. Second-harmonic generation 
	
Of course the harmonic potential is only a first order approximation around an equilibrium. An example, for a non-linear force or anharmonic potential effect, is the generation of [second-harmonic generation](https://en.wikipedia.org/wiki/Second-harmonic_generation). If you shine high intensity light onto the electrons of a molecule, they are pushed out of equilibrium further and if the governing potential is anharmonic, the electric field response will not only include the incoming frequency $\omega$ but also *higher harmonics* $2\omega, 3\omega,\dots$, but with much lower intensity. That the emitted frequencies are occurring in integer multiple of the incident frequency can be understood either from quantization of light into photons (and the conservation of energy) or from Fourier analysis of the periodic motion of the electron.

7. Erasmus Bridge & singing cables. 

The bridge in Rotterdam, but also others, suffer from long cables that the wind can put into resonance. Their motion then generates acoustic waves in the audible spectrum. [Listen here](https://singingbridgesmusic.bandcamp.com/track/erasmus-bridge-rotterdam) to the sound of the cables starting from 1:00 on the website for singing bridges! 

## Waves and oscillations

In the previous sections, we talked about oscillations of individual particles. Oscillations can also occur in a more collective mode. And there are plenty of examples: take for instance a violin or piano string. It is in essence an elastic string suspended between two fixed points. The string is under tension, that is: its natural length is (slightly) less than the distance between the two end points. As a consequence, equilibrium position of the string is a straight line and when brought out of equilibrium there is a net restoring force much like for the mass-spring system.

However, there are at least two important differences: (1) the restoring force is the net result from pulling on a small part of the string by its neighbor parts; (2) the entire string can oscillate in a direction perpendicular to the equilibrium position of the string, making the problem multi-dimensional.

We will give here an intuitive derivation of the equation of motion. Don't worry if you don't grasp it fully. This will come back in your studies further down the line.

In the figure below, a part of the string is drawn with special attention to a small part (the red line). On this small part the tension from the left and right side is pulling on the red part. This is visualized by the two blue arrows. In the inset, this is drawn at a larger scale. The two blue arrows are equal in magnitude ($T$) as the tension in the string is the same everywhere. But the direction in which the two blue forces are pulling is slightly different as the string is curved. 


```{figure} images/TensionString.png
:name: fig:TensionString.png
:width: 350px
:align: center
 
Forces on a small part of a string; inset shows an exaggeration of the vertical components of the forces.
```

If we call the angle of the blue forces with the $x$-axis $\theta$, then $\theta_1 \neq \theta_2$. This makes that a net force is action on the small red piece. And according to Newton's second Law, the small red mass must accelerate. 

Let's set up N2 for the red piece. The problem is 2-dimensional, so we set up N2 for the $x$ and $y$-direction:

$$\begin{split}
m\frac{d^2x}{dt^2} & = -T \cos \theta_1 + T \cos\theta_2 \\
m\frac{d^2y}{dt^2} & = -T \sin \theta_1 + T \sin\theta_2
\end{split}$$

Next, we simplify by only looking at situations where the angle $\theta_1$ and $\theta_2$ are small. The we can approximate the $\sin$ and $\cos$ terms: if $\theta \ll 1$ then $\sin \ theta \approx \theta$ and $\cos \theta \approx 1$ and we can write

$$\begin{split}
m\frac{d^2x}{dt^2} & = -T + T = 0 \\
m\frac{d^2y}{dt^2} & = -T \theta_1 + T \theta_2
\end{split}$$

Thus: for the $x$ direction we don't need to worry, nothing interesting happening there.

For the $y$-direction we face that we have too many unknowns. We need relations between $\theta_1, \theta_2, y$ and $x$. We are going to use again that $\theta \ll 1$ but know to make it seemingly more complex. 

If $\theta \ll 1$ then $\tan \ theta \approx \theta$. And we are going to replace $\theta$ by $\tan \theta$. Is that smart??? Now we get trigonometry back in the equation!! Don't worry. We use the $\tan \theta$ in another way. It is also the direction of the tangent to the curve the spring is making at the point where we are looking. In formula:

$$\tan \theta = \frac{dy}{dx}$$

And this is the coupling between angles and coordinates that we have been looking for.

We are going to plug this in in N2 for the $y$-direction. But before doing so: the left position of the red piece is at position $x$. So instead of label '1' we will use subscript $x$. Similarly, the right end of the red piece is at $x+dx$. Thus we can write

$$
m\frac{d^2y}{dt^2} = -T \left [ \frac{dy}{dx} \right ]_x + T \left [ \frac{dy}{dx} \right ]_{x+dx}
$$

It looks still pretty messy but we are almost there. The mass of the red piece obviously scales with its length. So if we introduce $\mu$ as the mass of the string per unit length, we can write for the mass of the red piece: $m = \mu dx$. Our equation can  now be written as

$$
\frac{d^2y}{dt^2} = \frac{T}{\mu} \frac{\left [ \frac{dy}{dx} \right ]_{x+dx} - \left [ \frac{dy}{dx} \right ]_x}{dx}
$$

We recognize on the right hand side the second derivative of $y$ with respect to $x$. Whereas on the left hand we see differentiating with respect to $t$. 

$$
\frac{d^2y}{dt^2} = \frac{T}{\mu} \frac{d^2y}{dx^2} 
$$

To make clear that we mean on the left hand side we mean: take the derivative only with respect to time we use $\partial t$ instead of $dt$. Similarly on the right hand $\partial x$ instead of $dx$. And we get our final result replaceing $\frac{T}{\mu}$ by $\mathsf{v}^2$

$$\frac{\partial^2 y}{\partial t^2} = \mathsf{v}^2 \frac{\partial^2 y}{\partial x^2}$$

This equation is called the **wave equation** and you will find it back in many branches of science and engineering. To solve it, you need advance calculus and that will certainly come in future courses. Here we will look at some global aspects of the equation.

<ol>

<li>

units of $\mathsf{v}^2$: $m^2 / s^2$. Thus $\mathsf{v}$ is a kind of velocity, at least based on its dimension.
</li>
<li>

if $y(x,t)$ is such that it only depends on $x \pm \mathsf{v}t$, that is $y(x,t) = y(x-\mathsf{v}t)$ then no matter what $y$ as function is, it is always a solution to the wave equation.

This is straightforward to prove: given $y(x,t) = y(x-\mathsf{v}t)$ then call $s \equiv $

$$ \frac{\partial y}{\partial t} = \frac{dy}{ds} \underbrace{\frac{\partial s}{\partial t}}_{=\mathsf{-v}}$$

Note the meaning of $\partial t$: differentiate $s = x - \mathsf{v}t$ as if $x$ is a constant, not depending on $t$.

We can differentiate this once more:

$$\frac{\partial^2 y}{\partial t^2} = \frac{\partial}{\partial t} \left ( -\mathsf{v} \frac{dy}{ds} \right ) = -\mathsf{v} \frac{d}{ds} \left ( \frac{dy}{ds} \right ) \frac{\partial s}{\partial t} = \mathsf{v}^2 \frac{d^2y}{ds^2}$$

Subsequently we look at $\frac{\partial^2 y}{\partial x^2}$:

$$\frac{\partial^2 y}{\partial x^2} = \frac{\partial}{\partial x} \left ( \frac{dy}{ds} \underbrace{\frac{\partial s}{\partial x}}_{=1} \right ) = \frac{d}{ds} \left ( \frac{dy}{ds} \right ) \frac{\partial s}{\partial x} = \frac{d^2y}{ds^2} $$

If we now substitute these two results in the wave equation we see:

$$\begin{split}
\frac{\partial^2 y}{\partial t^2} - \mathsf{v}^2 \frac{\partial^2 y}{\partial x^2} &= \mathsf{v}^2 \frac{d^2y}{ds^2} - \mathsf{v}^2 \frac{d^2y}{ds^2} = 0 \Rightarrow \\

\frac{\partial^2 y}{\partial t^2} &= \mathsf{v}^2 \frac{\partial^2 y}{\partial x^2}

\end{split}$$
And we see that our choice for $y(x,t) = y(x-\mathsf{v}t)$ automatically obeys the wave equation.
</li>
<li>

From the above we also learn that if the string has a certain 'amplitude' $y$ at position $x$ on time $t$ a little later this same amplitude will show up at a position a bit further along the string. Argument: given $x$ and $t$ then at $(x,t)$ the amplitude of the string is $y(x-\mathsf{v}t)$ and a little later, at $t+\Delta t$ we can look at position $x+\mathsf{v} \Delta t$: there $y(x+\Delta x, t +\Delta t)$ is 

$$y(x+\Delta x, t +\Delta t) = y(x+\mathsf{v}\Delta t -\mathsf{v} (t +\Delta t)) = y(x -\mathsf{v} t ) = y(x,t)$$

This actually means, that a traveling wave can be present in the string. We now this from our childhood when we probably all have been playing with a long rope making waves in it by quickly moving one end up and down.

</li>
<li>

The wave equation has as constant $\mathsf{v}^2$. We have identified this as a velocity and we now understand that it is the velocity with which a wave travels. But since the equation contains the square of the velocity, we conclude that if we have a solution with $+\mathsf{v}$, then also a solution with $-\mathsf{v}$ holds. In other words: waves can travel in 2 directions and they do so with the same speed (in magnitude).

</li>
</ol>

In the figure below, a wave is shown that starts as seemingly one hump. But it actually is two traveling waves on a rope.

Moreover, the rope has a fixed end at the left and a free one at the right. Notice the difference in reflection of the waves at both ends.

```{figure} images/OscillatingRope.gif
:name: fig:OscillatingRope.gif
:width: 350px
:align: center
 
Forces on a small part of a string; inset shows an exaggeration of the vertical components of the forces.
```

### Wave characteristics

Waves are omnipresent. We find them in musical instruments e.g. the violin but also in flutes where the wave is directly in the air in the instrument. We have them in water and air: waves on the oceans, waves when we speak. There are waves in solid materials for instance after an earthquake. We use waves in telecommunication.

Why are waves so generally found? They are the analogue of the harmonic oscillator. And thus, many systems in that are brought a bit out of equilibrium will try to go back to equilibrium, over shoot it and end up in a wavy motion.

#### Wave Length

Waves are often sinusoidal and if not, via Fourier Analysis they can be decomposed of a set of sinusoidal waves that built together the pattern we observe.

A sinusoidal wave is of the form

$$y(t) = A \sin (2 \pi f t)$$

with $f$ its frequency (and thus $\omega = 2 \pi f$ its angular frequency).

As we have seen above, in general the wave is also a function of position:

$$y(x,t) \sim A \sin ( x - vt)$$

How can we connect these two forms? First, we need to realize that the last equation has a dimensional issue: what is the sinus of say 7 meter? In other words, the argument of the sin-function should be dimensionless. So we write is in a different form, introducing the frequency in it:

$$y(x,t) =  A \sin \left ( \frac{2 \pi f}{\mathsf{v}} x - 2\pi f t \right ) $$

This seems unnecessary complicated. But it is not! The factor $\frac{f}{\mathsf{v}}$ has dimension 1 over length. If we call it $\frac{f}{\mathsf{v}} \equiv \frac{1}{\lambda}$ we can write

$$ y(x,t) = A \sin \left [2\pi \left ( \frac{x}{\lambda} - ft \right ) \right ] $$

Interpretation: for a fixed value of $t$ the wave is periodic in space with period $\lambda$. This is what we already know: the wave has a wave length $\lambda$.

On the other hand: for a fixed position $x$ the point at $x$ oscillates with a frequency $f$ and thus has a period $T = \frac{1}{f}$. Note that $\lambda$ and $f$ are coupled to each other:

$$\lambda \cdot f = \mathsf{v}$$

### Standing waves versus traveling waves

If we look at the motion of the string on a violin closely, we will not see traveling waves running from one side of the string to the other. Instead, we see all parts of the string moving up and down collectively: they have formed a standing wave. that is a wave that does not travel, but has a fixed, stationary shape whose amplitude various with time. 

For a string with two ends fixed like on a piano or violin, the string can only show standing waves that 'fit'. These standing waves are sinusoidal and their wave length should be such that the beginning and end of the string don't oscillate. In the figure below four possibilities are shown.


```{figure} images/String_animation.gif
:width: 350px
:align: center
 
Standing waves in a string.
```

We see that there is a simple relation between the length of the string, $L$ and the possible wave length, $\lambda$ of the standing waves:

$$ \frac{n}{2} \lambda  = L \Leftrightarrow \lambda = \frac{2L}{n}  \text{   with } n \in N$$

Further we see that the smaller the wavelength, the faster the oscillation. This is due to the relation $\lambda \cdot f = \mathsf{v}$ that still holds: $f = \frac{\mathsf{v}}{\lambda} = \frac{n\mathsf{v}}{2L}$.

The traveling waves had as mathematical form $\sin \left (x - \mathsf{v} t \right )$. The standing waves take forms like $\sin \frac{x}{\lambda} \cdot \sin ( 2\pi ft)$. You will learn much more about this in e.g. Fourier Analysis classes.

### Water waves and Sound waves

It is not necessary that a wave is caused by a tension in the material that tries to restore the equilibrium position. The restoring force can be of a different nature. A well know example is the water waves that we see on lakes and seas. Here gravity is the restoring force: it tries to pull a crest down and push a through up. The water inertia causes overshoot resulting in oscillations, that we call waves. In dealing with waves, we usually don't use the frequency $f$, but instead the angular velocity $\omega = 2 \pi f$. Similarly, frequently the wave length $\lambda$ is replaced by the wavenumber $k \equiv \frac{2\pi}{\lambda}$. Note that these two quantities are also related to each other by the speed of the waves: $\lambda \cdot f = \frac{2\pi}{\lambda} \frac{\omega}{2\pi} = \frac{\omega}{k} = \mathsf{v}$. 

For water waves (with large wave length) the angular momentum and the wave number are coupled to the depth, $h$, of the water:

$$\omega^2 = g k \tanh (kh)$$

From this we learn that waves on deep water travel much faster than on shallow water. This can be seen on our shores: the waves coming from the open sea are slowed down when the approach our beaches. But behind them the fast ones still come in. As a consequence, the wave gets squeezed in length and thus must get higher. This can be extreme with dramatic consequences: the Tsunami. The wave of the Tsunami is formed out in the open, where the sea is very deep. Here it travels at a very high speed which also means that it is a long wave. The Tsunami waves can travel ate velocities of 200m/s and have wave length of hundreds of kilometers. However at full see their amplitude is in the centimeter, decimeter range. A ship at full sea will hardly notice the passing Tsunami wave. But when the approach the shore, the front of the wave is slowed down to tens of m/s. As the back is still coming in at full speed the wave amplitude has to increase. And thus a huge wave in terms of amplitude storms towards the shore. A wall of water is seen coming, crushing everything in its way.

Sound waves are another type of waves that occur frequently. The can exist in solids, liquids and gasses. In contrast to the waves we have discussed so far, the amplitude is not perpendicular to the direction of traveling. It is what we call a longitudinal wave that oscillates in the same direction as it moves. The other waves are called transversal waves. 

For sound waves it is the pressure that is the restoring force. The 'crest' is compressed material, the 'through' is an expansion part. newton was intrigued by sound waves and provided a theory for them. He found that the speed of sound in air, according to his theory, was about 290 m/s. In reality it is some 340 m/s. Newton was well aware of the mismatch. But he couldn't find a good explanation. It took another 100 years for Pierre Laplace corrected Newton's work and arrived at the correct answer. Newton did not know that sound is connected to adiabatic compression. He couldn't as the entire concept was not know. Laplace realized that Newton basically had made an isothermal solution and corrected this.

