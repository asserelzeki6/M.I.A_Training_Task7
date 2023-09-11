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
}
