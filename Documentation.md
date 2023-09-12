# TASK7.2-Magic of PID

# Arduino PID Controller

This Arduino program implements a PID (Proportional-Integral-Derivative) controller. The PID controller is a control loop feedback mechanism widely used in control systems.

### Private Variables

- `kp`: Proportional gain.
- `ki`: Integral gain.
- `kd`: Derivative gain.
- `setpoint`: Desired value.
- `error_sum`: Sum of errors for integral term.
- `last_error`: Last error for derivative term.

# PID Controller Equations

A PID controller calculates an error value as the difference between a desired setpoint and a measured process variable. The controller attempts to minimize the error by adjusting the process control inputs. The PID controller calculation involves three separate parameters: the proportional, the integral, and derivative values. The Laplace form of the equation is:

$$
C(s) = K_p + \frac{K_i}{s} + K_d \cdot s
$$

where:

- `C(s)` is the output from the controller,
- `K_p` is the proportional gain,
- `K_i` is the integral gain,
- `K_d` is the derivative gain,
- `s` is the complex frequency.

The time domain form of the PID control algorithm is:

$$
u(t) = K_p \cdot e(t) + K_i \cdot \int_0^t e(\tau) d\tau + K_d \cdot \frac{de(t)}{dt}
$$

where:

- `u(t)` is the controller output,
- `e(t)` is the tracking error,
- `t` is time.

## Proportional Term

The proportional term produces an output value that is proportional to the current error value. The proportional response can be adjusted by multiplying the error by a constant `K_p`, called the proportional gain constant.

The equation for this term is:

$$
P_{\text{out}} = K_p \cdot e(t)
$$

## Integral Term

The integral term is proportional to both the magnitude of the error and the duration of the error. The integral response will continually increase over time unless the error is zero, so this can help eliminate residual errors. The speed at which this happens is determined by a constant `K_i`, called integral gain constant.

The equation for this term is:

$$
I_out = K_i*∫(from 0 to t) e(τ) dτ
$$

## Derivative Term

The derivative term is proportional to the rate of change of the error. This means that if the error is rapidly approaching zero, its response will be larger. This can help avoid overshoot due to too rapid changes in error. The impact of this term is determined by a constant `K_d`, called derivative gain constant.

The equation for this term is:

$$
D_out = K_d*de(t)/dt
$$

By tuning these three constants properly, a PID controller can adjust its outputs to cater to different systems dynamically.

# Code Explaination

```cpp
#include <Arduino.h>

class PIDController {
  private:
    float kp;  // Proportional gain.
    float ki;  // Integral gain.
    float kd;  // Derivative gain.
    float setpoint;  // Desired value.
    float error_sum = 0.0;  // Sum of errors for integral term.
    float last_error = 0.0;  // Last error for derivative term.

  public:
    // Constructor to initialize the PID controller.
    PIDController(float kp, float ki, float kd)
      : kp(kp), ki(ki), kd(kd) {}

    // Method to set the desired value (setpoint).
    void setSetpoint(float new_setpoint) {
      setpoint = new_setpoint;
      error_sum = 0.0;  // Reset sum of errors
      last_error = 0.0;  // Reset last error
    }

    // Compute the control output based on the measured value.
    float compute(float measured_value, float dt) {
      float error = setpoint - measured_value;

      // Proportional term
      float p_term = kp * error;

      // Integral term
      error_sum += error * dt;
      float i_term = ki * error_sum;

      // Derivative term
      float d_term = kd * (error - last_error) / dt;
      last_error = error;

      // Compute the control output
      return p_term + i_term + d_term;
    }
};

PIDController* pidController;

// setup function is called once when the program starts. 
void setup() {
  Serial.begin(9600);  // Initialize serial communication

  // Constants for PID tuning
  const float KP = 0.5;
  const float KI = 0.2;
  const float KD = 0.1;

  // Constant for desired cleaning rate in CFM
  const float CLEANING_RATE = 90.0;

  // Initialize the PID controller and set its setpoint
  pidController = new PIDController(KP, KI, KD);
  pidController->setSetpoint(CLEANING_RATE);
}

// loop function is called repeatedly as long as the Arduino is powered on. 
void loop() {
  // Constants for maximum and minimum flow rate in CFM
  const float MAX_FLOW_RATE = 100.0;
  const float MIN_FLOW_RATE = 0.0;

  // Simulate cleaner hose system with initial flow rate in CFM and time step in seconds
  static float currentFlowRate = 80.0;
  const float dt = 1.0;

  
  // Compute control output using PID controller and update flow rate based on control output
  float controlOutput = pidController->compute(currentFlowRate, dt);
  currentFlowRate += controlOutput * dt;

  // Limit flow rate within allowed range and print current flow rate to serial monitor
  currentFlowRate = max(MIN_FLOW_RATE, min(MAX_FLOW_RATE, currentFlowRate));
  
   Serial.print("Flow Rate: ");
   Serial.print(currentFlowRate);
   Serial.println(" CFM");
  
   delay(1000); // Delay for a second before next iteration
```

This code is the implementation of a PID (Proportional-Integral-Derivative) controller for a cleaner hose system using Arduino. PID controllers are commonly used in control systems to minimize the error between the desired setpoint and the measured process variable.

The code starts by defining a PIDController class with three private variables: kp, ki and kd that represent the proportional gain, integral gain, and derivative gain respectively. The class also has two other private variables: setpoint, which stores the desired value, error_sum, which is the sum of errors for the integral term, and last_error, which stores the last error for the derivative term.

The constructor of the class initializes the values of kp, ki, and kd, while the setSetpoint method sets the desired flow rate and resets the sum of errors and the last error. The compute method is called in the loop to calculate the control output based on the error between the setpoint and the measured value. The computed value is the sum of three terms: the proportional term, the integral term, and the derivative term.

The proportional term is proportional to the current error value and can be adjusted by multiplying the error by a constant kp. The integral term is proportional to both the magnitude of the error and the duration of the error, and it will continually increase over time unless the error is zero. The speed at which this happens is determined by a constant ki. The derivative term is proportional to the rate of change of the error and can help avoid overshoot due to too rapid changes in error. The impact of this term is determined by a constant kd.

The loop function starts by defining two constants for the maximum and minimum flow rate and a static variable currentFlowRate, which represents the initial flow rate. The compute method of the PID controller calculates the control output, which is then added to the current flow rate. The flow rate is then limited within the allowed range, and the current flow rate is printed to the serial monitor every second.

This code demonstrates the use of a PID controller for controlling the flow rate of a cleaner hose system. By tuning the three constants, kp, ki, and kd, the PID controller can dynamically adjust its outputs to cater to different systems.
