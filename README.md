# TASK7.1- Cytron vacuum

## Description

This Arduino code is designed to control a motor using the CytronMotorDriver library. It provides two main functionalities:

**1. Soft Start:** This feature gradually ramps up the motor's speed to prevent sudden spikes in current, which can be detrimental to the motor and other components. Soft starting is achieved by smoothly increasing the motor speed over time.

**2. Exponential Smoothing:** The code incorporates an exponential smoothing filter to make changes in motor speed smoother and more gradual, enhancing control precision.

## Code Explanation

### Initialization and Motor Pins

- The code begins by including the `CytronMotorDriver` library, which facilitates motor control.

- It defines two pins: `PWM_PIN` (for Pulse Width Modulation control) and `DIR_PIN` (for setting the direction of the motor). These pins should be specified based on how the motor driver is physically connected to the Arduino.

- An instance of `CytronMotorDriver` named `motor` is created, specifying the pins for PWM and direction control.

- Variables for soft start and filtering are declared. `targetSpeed` represents the desired final motor speed, `currentSpeed` tracks the current motor speed, and `smoothingFactor` determines the rate at which the motor speed changes.

### Setup

- The `setup` function is empty in this example because there are no specific setup requirements.

### Main Loop

- In the `loop` function, the code calculates the new `currentSpeed` using exponential smoothing. The formula `(1.0 - smoothingFactor) * currentSpeed + smoothingFactor * targetSpeed` is employed to gradually adjust the motor speed towards the `targetSpeed`.

- The motor speed is then converted to an integer value (`motorSpeed`) because the `motor.setSpeed()` function typically accepts integer values.

- To prevent out-of-bounds issues, a `constrain` function is utilized to ensure that the motor speed stays within a valid range (-255 to 255).

- The motor's direction is set based on the sign of the speed (positive for forward, negative for reverse) using `motor.setSpeed()`.

- The code provides a section where you can insert your custom cleaning and waste collection logic, allowing you to tailor the behavior of your application.

- Finally, a delay is included (100 milliseconds in this example) to control the update rate. You can adjust this delay to match the timing requirements of your specific application.

This code achieves soft starting and smoother motor speed control through exponential smoothing while utilizing the CytronMotorDriver library. It can be tailored to various motor control applications by modifying parameters and adding specific logic.

## Question
- Does this motor suitable for this application?
- 