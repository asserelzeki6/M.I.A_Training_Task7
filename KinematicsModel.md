# Kinematic Model of a Three-Wheeled Robot

## Kinematic Equations

### Position Equations

The position of the robot can be calculated using the following equations:

- `x = r(ω1 + ω2 + ω3)cosθ`
- `y = r(ω1 + ω2 + ω3)sinθ`

**Proof:**

To derive the position equations, we consider the motion of the robot's center of mass in the x and y coordinates. The linear velocity of the center of mass is given by `v = r(ω1 + ω2 + ω3)`. Integrating this velocity over time, we obtain the position equations `x = r(ω1 + ω2 + ω3)cosθ` and `y = r(ω1 + ω2 + ω3)sinθ`.

### Orientation Equation

The orientation of the robot can be calculated using the following equation:

- `θ = (r/d)(ω1 - ω3)`

**Proof:**

To derive the orientation equation, we consider the rotational motion of the robot. The angular velocity of the robot is given by `ω = (ω1 - ω3)`. Integrating this angular velocity over time, we obtain the orientation equation `θ = (r/d)(ω1 - ω3)`.

### Velocity Equations

The linear and angular velocities of the robot can be calculated using the following equations:

- Linear velocity: `v = r(ω1 + ω2 + ω3)`
- Angular velocity: `ω = (r/d)(ω1 - ω3)`

These equations describe the linear and angular velocities of the robot based on the angular velocities of its wheels.

## Kinematic Constraints

There are kinematic constraints on the robot's motion due to its three-wheeled configuration. These constraints can be expressed as equations:

- `ω1 + ω2 + ω3 = 0`
- `ω1 - ω3 ≤ dω2/r`

These constraints ensure that the robot moves without rotation around its center of mass and prevent excessive slipping or sliding.

## Application

The kinematic model of a three-wheeled robot is useful for simulating the robot's motion, designing control algorithms, and planning its trajectory. By adjusting the wheel velocities, the robot's position, orientation, linear velocity, and angular velocity can be predicted, allowing for optimization of its motion and control.

These equations and proofs provide a foundation for understanding and predicting the behavior of a three-wheeled robot. They are essential for developing control algorithms, path planning, and navigation systems for such robots.
