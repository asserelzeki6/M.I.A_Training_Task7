<h1>Kinematics modeling and simulation of an autonomous
omni-directional mobile robot</h1>

<p>Although robotics has progressed to the extent that it has become relatively accessible with low-cost projects, there is still a need to
create models that accurately represent the physical behavior of a robot.</p>
<img src="https://i.ibb.co/JFFt2Rd/image.png"></img>

<h2>Required Equations</h2>
<p>Matrix models a radius R wheel, omni-directional with
radius r and rollers fixed to 90º, with traction but non-directional. Regarding vector q, wix represents the angular speed
of the motor attached to the wheel, wir is the wheel´s rollers
angular speed and wiz holds the rotational slippage in relation to the vertical axis of the wheel. Then, the jacobean for
the i-th wheel can be expressed as follows:</p>
<img src="https://i.ibb.co/ZHj1DqC/image.png"></img>
<p>Since there are
three rows that are linear combination from the others. Because of this condition, non-actuated variables are removed accordingly to the actuated, and the following equations are obtained:</p>
<img src="https://i.ibb.co/5Bgmnbw/image.png"></img>
<p>Matrix contains the relation between the vehicle
speed and the rollers, but from a practical point of view
only actuated degrees are taken, such that the non-slippage
condition </p>
<img src="https://i.ibb.co/vL8LCgc/image.png"></img>

<h1>Kinematics</h1>
<p>Equations can be accommodated as a matrix and the final
Jacobean of the robot is obtained</p>
<img src="https://i.ibb.co/N2mkDtk/image.png"></img>
<p>The inverse of the Jacobean  of the robot can be expressed as follows:</p>
<img src="https://i.ibb.co/Fxv6qGw/image.png"></img>
