"""
This file contains the code for a robot controller.

The robot controller calculates the angular velocities of the two motors
and sets the PWM of the motors. It also updates the PID controller. It also  Converts from the local frame of robot to the 
global frame of the world using a rotational matrix.
"""

import math
import time

from motor import Motor
from pid import PID
import numpy as np

def local_to_global(local_coordinates, theta):
    """
    Convert local coordinates to global coordinates using a rotational matrix.

    Args:
        local_coordinates (tuple): A tuple containing the local (x, y) coordinates.
        theta (float): The angle of rotation (in radians).

    Returns:
        tuple: A tuple containing the global (x, y) coordinates.
    """
    # Extract local (x, y) coordinates
    x_local, y_local = local_coordinates

    # Define the rotational matrix
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])

    # Create a column vector for the local coordinates
    local_vector = np.array([[x_local], [y_local]])

    # Perform the coordinate transformation
    global_vector = np.dot(rotation_matrix, local_vector)

    # Extract the global (x, y) coordinates from the result
    x_global = global_vector[0][0]
    y_global = global_vector[1][0]

    return x_global, y_global

def get_angular_velocities(vx, vy, omega):
    """
    Returns the angular velocities of the three motors.

    Args:
        vx (float): The x-component of the robot's velocity.
        vy (float): The y-component of the robot's velocity.
        omega (float): The angular velocity of the robot.

    Returns:
        tuple: A tuple of the angular velocities (in RPM) of the three motors.
    """

    R = 20  # Wheel radius
    L = 100  # Distance between wheels

    # Calculate the angular velocities for each motor at 0, 120, and 240 degrees.
    w1 = (vx * math.cos(0) + vy * math.sin(0) + L * omega) / R
    w2 = (vx * math.cos(2 * math.pi / 3) + vy * math.sin(2 * math.pi / 3) + L * omega) / R
    w3 = (vx * math.cos(4 * math.pi / 3) + vy * math.sin(4 * math.pi / 3) + L * omega) / R

    return w1, w2, w3

def drive_motor(motor, pwm):
    """
    Drives the motor at the given PWM.

    Args:
        motor (Motor): The motor to drive.
        pwm (float): The PWM (RPM) value to set for the motor.
    """
    motor.set_pwm(pwm)

def create_pid_controller(kp, ki, kd):
    """
    Creates a PID controller.

    Args:
        kp (float): The proportional gain.
        ki (float): The integral gain.
        kd (float): The derivative gain.

    Returns:
        PID: A PID controller instance.
    """
    return PID(kp, ki, kd)

def main():
    # Create the motors.
    motor_1 = Motor(0)  # Motor at 0 degrees
    motor_2 = Motor(120)  # Motor at 120 degrees
    motor_3 = Motor(240)  # Motor at 240 degrees

    # Create the PID controller.
    pid_controller = create_pid_controller(1, 0, 0)

    # Set the target position.
    target_position = [100, 100]
    global_position = [0, 0]
    theta = 0
    # Start the loop.
    while True:
        # Calculate the robot's velocity and angular velocity.
        vx, vy, omega = get_angular_velocities(target_position[0] - motor_1.position,
                                              target_position[1] - motor_2.position, theta)

        # Calculate the angular velocities of the three motors.
        w1, w2, w3 = get_angular_velocities(vx, vy, omega)

        # Convert from the local frame of robot to the global frame of the world using a rotational matrix
        global_position = local_to_global(target_position, theta)
        print("Global coordinates are :", global_position)

        # Set the PWM (RPM) of the motors.
        motor_1.set_pwm(w1)
        motor_2.set_pwm(w2)
        motor_3.set_pwm(w3)

        # Update the PID controller (you can choose which motor's position to use).
        pid_controller.update(motor_1.position, target_position[0])

        # Calculate the error.
        error = target_position[0] - motor_1.position

        # Print the error.
        print("Error = %f" % error)

        # Sleep for a second.
        time.sleep(1)
