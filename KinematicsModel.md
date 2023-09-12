# Kinematic Model of a Three-Wheeled Robot

## Linear and Angular Velocity Equations

In the kinematic model of a three-wheeled robot, we can calculate the linear velocities \(V_x\) and \(V_y\) in the x and y directions, respectively, as well as the angular velocity \(\omega\) using the following equations:

- Linear velocity in the x-direction (\(V_x\)):
  \[V_x = r \cdot \left(\frac{\sqrt{3}}{2} \cdot \omega_1 - \frac{\sqrt{3}}{2} \cdot \omega_2\right)\]

- Linear velocity in the y-direction (\(V_y\)):
  \[V_y = r \cdot \left(\omega_3 - \frac{1}{2} \cdot \omega_1 - \frac{1}{2} \cdot \omega_2\right)\]

- Angular velocity (\(\omega\)):
  \[\omega = \frac{r}{d} \cdot \left(\omega_1 + \omega_2 + \omega_3\right)\]

## Explanation

- **Linear velocity in the x-direction (\(V_x\)):** This equation is derived from the fact that the robot's linear velocity in the x-direction is influenced by the differences in angular velocities between the omni wheels. The factor \(\frac{\sqrt{3}}{2}\) accounts for the geometric configuration of the wheels.

- **Linear velocity in the y-direction (\(V_y\)):** Similarly, the linear velocity in the y-direction depends on the angular velocities of the wheels. The coefficients \(\frac{1}{2}\) and \(-\frac{1}{2}\) adjust for the wheel configuration.

- **Angular velocity (\(\omega\)):** The angular velocity of the robot is the sum of the angular velocities of all three wheels, scaled by \(\frac{r}{d}\), where \(r\) is the wheel radius and \(d\) is the distance between the center of the robot and the wheel.

These equations allow us to calculate the robot's linear and angular velocities based on the input angular velocities of its omni wheels. Understanding these relationships is essential for precise control and navigation of three-wheeled robots.

## Application

Utilizing these velocity equations is crucial for designing control algorithms, path planning, and real-time navigation of three-wheeled robots in a variety of applications, including mobile robotics, automation, and autonomous vehicles.
