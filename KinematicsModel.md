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

### Orientation Equation

The orientation of the robot can be calculated using the following equation:

- `θ = (r/d)(ω1 - ω3)`

## Derivation

The position equations can be derived by considering the horizontal and vertical displacements of the robot's center of mass. The orientation equation can be derived by considering the rotational motion of the robot.

The horizontal displacement of the wheels is `r(ω1 + ω2 + ω3)cosθ`, and the vertical displacement is `r(ω1 + ω2 + ω3)sinθ`. The total horizontal and vertical displacements of the robot's center of mass can be calculated accordingly.

The orientation equation is derived by equating the angular momentum of the robot, which is given by `Iω` (where `I` is the moment of inertia), with the angular momentum calculated using the wheel velocities.

## Application

The kinematic model of a three-wheeled robot is useful for simulating the robot's motion and testing different control strategies. By adjusting the wheel velocities, the robot's position and orientation can be predicted, allowing for optimization of its motion and control.

