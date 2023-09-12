# Robot Controller

This file contains the code for a robot controller. The robot controller calculates the angular velocities of the three motors and sets the PWM of the motors. It also updates the PID controllers for each motor.

## Functions

### `local_to_global(local_coordinates, theta)`
   
Convert local coordinates to global coordinates using a rotational matrix.

**Arguments:**

- `local_coordinates (tuple)`: A tuple containing the local (x, y) coordinates.
- `theta (float)`: The angle of rotation (in radians).  
   

**Returns:**

tuple: A tuple containing the global (x, y) coordinates.
    

### `get_angular_velocities(vx, vy, omega)`

Returns the angular velocities of the three motors.

**Arguments:**

- `vx`: The x-component of the robot's velocity.
- `vy`: The y-component of the robot's velocity.
- `omega`: The angular velocity of the robot.

**Returns:**

A tuple of the angular velocities of the three motors.

### `drive_motor(motor, pwm)`

Drives the specified motor at the given PWM (RPM).

**Arguments:**

- `motor`: The motor to drive.
- `pwm`: The PWM to set, which will be equal to RPM.

### `create_pid_controller(kp, ki, kd)`

Creates a PID controller.

**Arguments:**

- `kp`: The proportional gain.
- `ki`: The integral gain.
- `kd`: The derivative gain.

**Returns:**

A PID controller.

### `main()`

The main function of the program.

- Creates the motors and the PID controllers for each motor.
- Sets the target position.
- Starts the loop, which calculates the angular velocities of the motors, sets the PWM of the motors, updates the PID controllers, and prints the error.

## Usage

To use the robot controller:

1. Create the motors and the PID controllers for each motor.
2. Set the target position.
3. Start the loop.

```markdown
Example usage:

```python
# Create motors and PID controllers
motor1 = create_motor()
motor2 = create_motor()
motor3 = create_motor()

pid1 = create_pid_controller(kp, ki, kd)
pid2 = create_pid_controller(kp, ki, kd)
pid3 = create_pid_controller(kp, ki, kd)

# Set the target position
set_target_position(target_position)

# Start the control loop
while True:
    # Calculate angular velocities
    velocities = get_angular_velocities(vx, vy, omega)
    
    # Set PWM for motors
    drive_motor(motor1, velocities[0])
    drive_motor(motor2, velocities[1])
    drive_motor(motor3, velocities[2])
    
    # Update PID controllers and print error
    error1 = update_pid(pid1, current_position1)
    error2 = update_pid(pid2, current_position2)
    error3 = update_pid(pid3, current_position3)
    
    print(f"Error1: {error1}, Error2: {error2}, Error3: {error3}")
