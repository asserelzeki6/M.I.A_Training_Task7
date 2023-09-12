# Kinematic Model of a Three-Wheeled Robot

The kinematic model describes the motion of a three-wheeled robot with the following dimensions:

- Radius of the wheels: `r`
- Distance between the front and rear wheels: `d`
- Distance between the front wheel and the center of mass: `h`

## Kinematic Equations

### Position Equations

The position of the robot can be calculated using the following equations:

- `x = r(ω1 + ω2 + ω3)cosθ`
- `y = r(ω1 + ω2 + ω3)sinθ`

Here, `ω1`, `ω2`, and `ω3` represent the angular velocities of the wheels, and `θ` is the orientation of the robot.

These equations determine the robot's position in the x and y coordinates based on the angular velocities of all three wheels. By summing the angular velocities of the wheels and multiplying by `r`, we obtain the linear velocity of the robot's center of mass. The `cosθ` and `sinθ` terms account for the orientation of the robot.

### Orientation Equation

The orientation of the robot can be calculated using the following equation:

- `θ = (r/d)(ω1 - ω3)`

This equation determines the change in the robot's orientation (`θ`) based on the angular velocities of the front wheel (`ω1`) and the rear wheel (`ω3`). The term `(ω1 - ω3)` represents the difference in the angular velocities between these two wheels, and multiplying it by `r/d` gives the rate of change of orientation.

### Velocity Equations

The linear and angular velocities of the robot can be calculated using the following equations:

- Linear velocity: `v = r(ω1 + ω2 + ω3)`
- Angular velocity: `ω = (r/d)(ω1 - ω3)`

Here, `v` represents the linear velocity, and `ω` represents the angular velocity.

The linear velocity is obtained by summing the angular velocities of all three wheels and multiplying by `r`. This represents the forward or backward movement of the robot. The angular velocity is determined by the difference in angular velocities between the front and rear wheels, multiplied by `r/d`. This represents the rate of rotation of the robot.

### Kinematic Constraints

There are kinematic constraints on the robot's motion due to the nature of its three-wheeled configuration. These constraints can be expressed as equations:

- `ω1 + ω2 + ω3 = 0`
- `ω1 - ω3 ≤ dω2/r`

The first equation states that the sum of the angular velocities of all three wheels must be zero, which ensures that the robot moves without any rotation around its center of mass.

The second equation imposes a constraint on the angular velocities to prevent the robot from having excessive slipping or sliding. It ensures that the difference in angular velocities between the front and rear wheels (`ω1 - ω3`) is less than or equal to the angular velocity of the middle wheel (`ω2`) multiplied by `d/r`.

## Derivation

The position equations can be derived by considering the horizontal and vertical displacements of the robot's center of mass. The orientation equation can be derived by considering the rotational motion of the robot.

The velocity equations are derived from the position equations by differentiating them with respect to time.

The kinematic constraints arise from the requirement that the robot moves without rotation around its center of mass and to prevent excessive slipping or sliding.

## Application

The kinematic model of a three-wheeled robot is useful for simulating the robot's motion, designing control algorithms, and planning its trajectory. By adjusting the wheel velocities, the robot's position, orientation, linear velocity, and angular velocity can be predicted, allowing for optimization of its motion and control.

These equations and derivations provide a foundation for understanding and predicting the behavior of a three-wheeled robot. They are essential for developing control algorithms, path planning, and navigation systems for such robots.
