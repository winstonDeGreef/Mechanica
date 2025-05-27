# Exercises, examples \& solutions

## Worked Example

In class you have seen the *Superballs* example. You can watch it <a href="https://www.youtube.com/watch?v=2UHS883_P60">here</a> again. The explanation is not really correct there, we will reason the observations here.

If you let a <span style="color:green">smaller</span> and a <span style="color:blue">larger</span> ball drop together, stacked on top of each other, the smaller ball will bounce back much stronger (higher) than if you let the small ball fall without stacking it on the lager ball. How can that happen?


```{figure} images/Superballs.png
:label: fig:superballs.png
:width: 450px
:align: center
 
Bouncing balls.
```

To explain this we use the Galilean Transformation (GT).

* Situation 1). Both balls are falling with velocity $\vec{v}$ towards the ground.
* Situation 2a). The larger ball just hit the ground. As the mass of the ground is much larger than that of the large ball, it is (elastically) reflected, i.e. the direction of the velocity is reversed but the magnitude stays the same. The small ball is still moving downwards with $\vec{v}$.
* Situation 2b). We apply a GT of the observer (yellow star) from the ground to an observer moving with the larger ball. The observer moving with the larger ball sees the smaller ball moving with $2\vec{v}$ towards it.
* Situation 3a). The smaller ball hits the larger ball and is reflected due to its smaller mass. In the frame of the observer on the larger ball, the smaller ball now moves with $2\vec{v}$ away from it.
* Situation 3b).  We apply a GT of the observer (yellow star) from the larger ball  back to an observer on the ground. For the observer on the ground the larger ball has velocity $\vec{v}$ upwards from 2a), therefore the smaller ball has velocity $3\vec{v}$ upwards.

The smaller ball has now velocity $3\vec{v}$ instead of $\vec{v}$ if you drop it without the larger ball. NB: If you would use three balls instead of two, the third ball would have a velocity of $7\vec{v}$ using the same reasoning as above. 

```{figure} images/Superball_animation.gif
:label: fig:Superball_animation.gif
:width: 450px
:align: center
 
Bouncing of three (super)balls.
```

How much higher does the smaller ball fly with velocity $3\vec{v}$ compared to $\vec{v}$?

<b>Answer</b>
  We equate the kinetic energy when the ball is just reflected with the potential energy when the ball reached it maximal height before falling back.

$$ \frac{1}{2}mv^2 = mgh \Rightarrow h = \frac{v^2}{2g} $$
	
Therefore the ball with $3v$ flies 9 times higher.
	
We equate the kinetic energy when the ball is just reflected with the potential energy when the ball reached it maximal height before falling back.
	
$$ \frac{1}{2}mv^2 = mgh \Rightarrow h = \frac{v^2}{2g} $$
	
Therefore the ball with $3v$ flies 9 times higher.

<b>What is very fishy about this whole outcome?</b>  
In situation 1) the kinetic energy is $\frac{1}{2}m_s v^2 + \frac{1}{2}m_\ell v^2$, but in situation 3b) it is $\frac{1}{2}m_s (3v)^2 + \frac{1}{2}m_\ell v^2$ while the potential energy is zero in both cases. This clearly does not add up! But energy must be conserved under all circumstances!

The conclusion is, that we did make an approximation and did not solve the energy and momentum conservation equations for elastic collisions. Even for the case $M \gg m$ there is some momentum transfer. If you solve for the velocity of $m$ after the collision with $M$, you obtain 

$$ v' = \frac{\frac{m}{M}-1}{\frac{m}{M}+1} v $$

For $M \gg m$ you indeed see $v'=-v$. Thus the smaller ball will have a smaller velocity than reasoned above *and* the larger ball with also have a smaller velocity (in the experiment you can clearly notice that it does not fly as high as when it drops without the small ball on top). In real life, the balls also deform which makes the collision inelastic.


## Examples
````{example} 8.1

Consider yourself biking at a constant velocity on an unlikely day with zero wind. Still, you experience a frictional force from the air, with the following observation: the faster you bike, the larger this force. An experimentalist is trying to measure the friction force of the air and relate it to your velocity. She finds that, by and large, these forces turn out to scale with the square of your velocity $v_b$

$$ F_f \propto v_b^2 $$

```{figure} images/Fietser.png
:label: fig:Fietser.png
:width: 300px
:align: center
 
Air resistance on cyclist.
```   

Understanding the Galilean transformation, you immediately see that this can't be correct. In your frame of reference, your velocity is zero. And thus, the friction force would be zero. But that cannot be true: both observers should see the same forces. What you see is that the air is blowing at a speed $v_{air}−v_b$ past you. And indeed, the faster you bike, according to the experimentalist, the faster you see the air moving past you: velocity is relative.

You quickly realize that a proper description of the air friction must depend on the relative velocity between you and the air. *Relative* velocities are invariant under Galilean transformation:

$$ F_f \propto (v_b - v_{air} )^2 $$
````

````{example} 8.2

Riding a bike while it rains. You have done this 100s of times. Your front gets soaked, while the backside of your coat stays dry. Or if you have a passenger on your carrier he/she will not get wet, while you take all the water. From a GT to the reference frame of the biker it is obvious  why this is the case. The rain is not falling straight from the sky, but at an angle towards him. 

```{figure} images/RainBike.png
:label: fig:RainBike.png
:width: 400px
:align: center
 
Riding a bike in the rain.
```   

NB: For Dutch bikers you have had this experiences with head wind and rain all your life.
````

## Demo

A ball is bouncing at a wall. The mass of the wall is much greater than that of the ball. So, acceleration of the wall or changes in momentum of the wall can be ignored. 

On the left side, we see this from the perspective of an observer, S, standing next to the wall. The right side shows what observer S', who is traveling with the ball as it moves towards the wall, sees.
Notice, that both S and S' are inertial observers. That is, they keep their velocity and are no part of the collision.
What would Galilei say?

```{figure} images/BallAgainstWall_animation.gif
:label: fig:BallAgainstWall_animation.gif
:width: 400px
:align: center
 
Ball bouncing at a wall.
```  


## Exercise

````{exercise}
:label: 8.1

A train is passing a station at a constant velocity $V$. At the platform, an observer $S$ sees that in the middle of the train (train length $2L$), at $t=0$ an object is released with a constant velocity $u$. The object moves towards the back of the train and, at some point in time, will hit the back.

```{figure} images/TrainAndObject1.png
:label: fig:TrainAndObject1.png
:width: 350px
:align: center
 
```  

Inside the train, observer $S'$ sees the same phenomenon. Show that both find the same time for the object hitting the back of the train.
````

````{exercise}
:label: 8.2

A point particle of mass $m$ is sitting on a horizontal frictionless table. Gravity is acting in the vertical downward direction.   
According to your observation, $m$ has zero velocity. But you see the table moving at a velocity $-v$ in the negative $x$-direction. The table doesn't stay flat, but has a bump of height $H$. What will happen to $m$?

```{figure} images/TableWithBump1.png
:label: fig:TableWithBump1.png
:width: 350px
:align: center
 
```  

````


```{exercise}
:label: 8.3

Finally, it is winter. And this time, there is lots of fresh snow! You get engaged in a great snowball fight. Your opponent has run out of 'ammunition' and runs away. She is at a distance $L = 2m$ when she starts running at a speed of 5m/s. You throw your last snowball at her at a speed of 10m/s.   
Determine when and where the snowball hits her. Do that three times:

- Your perspective;
- Your opponent's perspective;
- The snowballs perspective.

Next, use the Galilei transformation and show that you could have used your perspective and GT to find the data for the other two perspectives.

```

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Answers


````{solution} 8.1
:class: dropdown

First we make a new sketch, now showing the two observers $S$ and $S'$ and their axis. We have made the velocity of the object red, the color of $S$. And we have given the coordinates of the front and back of the train in green as these are specified according to $S'$. We do this, as it is is crucial to realize that we have 'mixed' information.  

```{figure} images/TrainAndObject2.png
:label: fig:TrainAndObject2.png
:width: 350px
:align: center
 
```  
The velocity of the object is $u$ according to $S$. The observer in the train, $S'$, sees a different velocity.   
The observer in the train will denote the position of the front of the train by $x_f' = L$ and of the back $x_b' = -L$. Both are, according to $S'$, fixed values. But $S$ will se that differently.

According to $S'$, the object moves with velocity $u' = u-V$. Note that this is a negative value, otherwise the object will not hit the back of the train.

$S'$ will describe the trajectory of the object by: $x'(t) = x'_0 +u' t$ with $x'_0=0$. Thus, the object will hit the back of the train at:

$$ x'(T') = -L \rightarrow u'T'=-L \rightarrow T' = \frac{L}{-u'}$$

What does $S$ observe? It will write for the trajectory of the object $x_o(t) = u t$ (where we used that the object was released in the middle of the train at $t=0$ and both observers chose that as their origin).  
According to $S$ also the back of the train is moving. It follows a trajectory $x_b = -L + Vt$, since at $t=0$ the back of the train was at position $x = -L$ according to $S$. The two will collide when

$$x_o(T) = x_b(T) \rightarrow uT = -L + VT \rightarrow T = \frac{L}{V-u}$$

Hence we have $T$ and $T'$ as times of collision. But we already found $u' = u-V$. If we substitute this in $T'$ we get

$$ T' = \frac{L}{-u'} = \frac{L}{V-u} = T $$

Thus, indeed both observers see the collision at the same moment.

Sneak Preview: much to our surprise, when we enter the world of Special Relativity, this will no longer be the case!
````

````{solution} 8.2
:class: dropdown

The particle will 'collide' with the bump. This might cause the particle to start moving to the left. How to analyse this situation?

Perhaps it is easier when we view this from the point of view of an observer moving with the table.

```{figure} images/TableWithBump2.png
:label: fig:TableWithBump2.png
:width: 350px
:align: center
 
```  

Now we have a situation of a particle moving over a friction less table with velocity $v$. If we use conservation of energy, we can write down:

$$\frac{1}{2}mu^2 + mgh = E_0 = \frac{1}{2}mv^2 $$

where we have taken $h$ as the height above the table and denote the velocity of $m$ at some point by $u$. The initial height is zero and the initial velocity is $v$.

So, if the initial velocity is such that $\frac{1}{2}mv^2 > mgH $, the particle will go over the bump and come back to height $h=0$. It will thus pass the bump and then continue moving with velocity $v$. For the original observer this means: the bump will pass the particle and after passing the particle is again laying still (but not at the same position!).

If, on the other hand $v$ is such that $\frac{1}{2}mv^2 < mgH $, the particle will not reach the top of the bump: it has insufficient kinetic energy. In stead it will stop at some height $h^* = \frac{v^2}{2g}$ and then fall of the bump again. It will continue with velocity $-v$ at the flat part of the table. To the original observer this means that $m$ first climbs the bump and returns to get a velocity $-2v$ on the flat part of the table.

The final possibility is $\frac{1}{2}mv^2 = mgH$. In that case the particle will exactly reach the top of the bump and stop there. 

N.B. We have assumed that the bump is not too steep, because in such a case the particle will have a real collision with the bump. Think, for instance, of the bump as a sudden step. Then no matter how fast the particle is moving, it will not end up on the step, but bounce back.

````


````{solution} 8.3
:class: dropdown

First, a sketch:

```{figure} images/SnowBall.png
:label: fig:SnowBall.png
:width: 300px
:align: center
 
```  
It is a 1-dimensional problem, so an $x$-axis will do. We denote the velocity of your opponent (as seen by you) by $v_o$ and of the snowball $v_s$. The inertial system of you is $S$ and you are sitting in the origin $\mathcal{O}$. Similarly, you opponents inertial system is $S'$ with origin $\mathcal{O'}$ and finally the snowball has inertial system $S"$ and the snowball sits in the origin $\mathcal{O"}$.

1) Your perspective  
$$x_s(t) = v_s t$$
$$x_o(t) = L + v_o t$$
require: $x_s(t^*) = x_o(t^*)$
$$\rightarrow t^* = \frac{L}{v_s - v_o} = 0.4 s \rightarrow x^* = v_s t^* = 4m$$

2) Your opponent's perspective  
$$v'_s = v_s - v_0 =5m/s$$
require: $x'_s(t'^*) = 0$ since $S'$ is in $x'=0$. Thus

$$x'_s(t'^*) = -L +v'_s t'^* = 0 \rightarrow t'^* = \frac{L}{v'_s} = 0.4 $$
Same time of course. Position: your opponent concludes she is not moving and this she is hit at $x'=0$.

3) The snowballs perspective.  
According to the snowball $v"_o = v_o - v_s = -5m/s$. Thus,
$$x"_o = L + v"_o t$$
require: $x"_o(t"^*) = 0$

$$x"_o(t"^*) = L + v"_s t"^* \rightarrow t"^* = -\frac{L}{v"_o} = 0.4s$$
And, again the snowball will conclude that it all happened in its origin.

Galilei Transformation  
We now have three different time/place coordinates for the event 'snowball hits opponent'.

$$\begin{split}
S: (x_h,t_h) &= (4m, 0.4s)\\
S': (x'_h,t'_h) &= (0m, 0.4s)\\
S": (x"_h,t"_h) &= (0m, 0.4s)
\end{split}$$

We could have found this directly from a GT.  
a) from $S$ to $S'$: we need to take into account that at $t=0$ the origins do not coincide. Instead $\mathcal{O'}$ is shifted over a distance L w.r.t. $\mathcal{O}$
$$\begin{split}
x' &= x - L - v_o t\\
t' &= t
\end{split}$$
Thus: $x'h = x_h - L - v_o t_h = 0$ and we get indeed $(x'_h,t'_h) = (0m, 0.4s)$

b) We do a similar exercise for $S$ to $S"$:
$$\begin{split}
x" &= x - v_s t \\
t" &= t
\end{split}$$
Thus: $x"_h = x_h - v_s t_h = 0$ and we get $(x"_h,t"_h) = (0m, 0.4s)$
````
