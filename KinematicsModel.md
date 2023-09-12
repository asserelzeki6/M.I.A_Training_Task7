# Kinematic Model of a Three-Wheeled Robot

## Linear and Angular Velocity Equations

In the kinematic model of a three-wheeled robot, we can calculate the linear velocities \(V_x\) and \(V_y\) in the x and y directions, respectively, as well as the angular velocity \(\omega\) using the following equations:

- **Linear velocity in the x-direction (\(V_x\)):**
  \[
  V_x = r \cdot \left(\frac{\sqrt{3}}{2} \cdot \omega_1 - \frac{\sqrt{3}}{2} \cdot \omega_2\right)
  \]

- **Linear velocity in the y-direction (\(V_y\)):**
  \[
  V_y = r \cdot \left(\omega_3 - \frac{1}{2} \cdot \omega_1 - \frac{1}{2} \cdot \omega_2\right)
  \]

- **Angular velocity (\(\omega\)):**
  \[
  \omega = \frac{r}{d} \cdot \left(\omega_1 + \omega_2 + \omega_3\right)
  \]

## Explanation

- **Linear velocity in the x-direction (\(V_x\)):** This equation accounts for the robot's forward/backward linear velocity. The factor \(\frac{\sqrt{3}}{2}\) is introduced to accommodate the wheel geometry.

- **Linear velocity in the y-direction (\(V_y\)):** Similarly, this equation calculates the robot's left/right linear velocity. The coefficients \(\frac{1}{2}\) and \(-\frac{1}{2}\) adjust for the wheel configuration.

- **Angular velocity (\(\omega\)):** The angular velocity of the robot is determined by the sum of the angular velocities of all three wheels, scaled by \(\frac{r}{d}\), where \(r\) is the wheel radius and \(d\) is the distance between the center of the robot and the wheel.

These equations provide a fundamental understanding of how the angular velocities of the omni wheels influence the robot's linear and angular motion.

## Application

Utilizing these velocity equations is essential for designing control algorithms, path planning, and real-time navigation of three-wheeled robots in a wide range of applications, including mobile robotics, automation, and autonomous vehicles.
