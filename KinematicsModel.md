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

These equations take into account the contributions of all three wheels to the robot's position. The term `(ω1 + ω2 + ω3)` represents the sum of the angular velocities of all three wheels, and multiplying it by `r` gives the linear velocity of the robot's center of mass in the x and y directions. The `cosθ` and `sinθ` terms account for the orientation of the robot.

### Orientation Equation

The orientation of the robot can be calculated using the following equation:

- `θ = (r/d)(ω1 - ω3)`

This equation determines the change in the robot's orientation (`θ`) based on the angular velocities of the front wheel (`ω1`) and the rear wheel (`ω3`). The term `(ω1 - ω3)` represents the difference in the angular velocities between these two wheels, and multiplying it by `r/d` gives the rate of change of orientation.

## Derivation

The position equations can be derived by considering the horizontal and vertical displacements of the robot's center of mass. The orientation equation can be derived by considering the rotational motion of the robot.

The horizontal displacement of the wheels is `r(ω1 + ω2 + ω3)cosθ`, and the vertical displacement is `r(ω1 + ω2 + ω3)sinθ`. These equations take into account the contributions of all three wheels to the robot's position. The `cosθ` and `sinθ` terms account for the orientation of the robot.

The orientation equation is derived by equating the angular momentum of the robot, which is given by `Iω` (where `I` is the moment of inertia), with the angular momentum calculated using the wheel velocities. By equating these two expressions and solving for `θ`, we obtain the orientation equation.

## Application

The kinematic model of a three-wheeled robot is useful for simulating the robot's motion and testing different control strategies. By adjusting the wheel velocities, the robot's position and orientation can be predicted, allowing for optimization of its motion and control.

These equations and derivations provide a foundation for understanding and predicting the behavior of a three-wheeled robot. They can be used in the development of control algorithms, path planning, and navigation systems for such robots.
