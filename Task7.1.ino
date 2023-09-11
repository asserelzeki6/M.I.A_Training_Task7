#include <Arduino.h>
#include <CytronMotorDriver.h>

// Define motor pins
#define PWM_PIN 3 // PWM input pin connected to Cytron motor driver
#define DIR_PIN 4 // Direction input pin connected to Cytron motor driver

// Create an instance of CytronMotorDriver
CytronMD motor(PWM_DIR, PWM_PIN, DIR_PIN);

// Variables for soft start and filtering
float targetSpeed = 255.0; // Target motor speed
float currentSpeed = 0.0;  // Current motor speed
const float smoothingFactor = 0.1; // Exponential smoothing factor

void setup() {
  // No setup needed in this example
}

void loop() {
  // Calculate the new currentSpeed using exponential smoothing
  currentSpeed = (1.0 - smoothingFactor) * currentSpeed + smoothingFactor * targetSpeed;

  // Set motor speed
  int motorSpeed = int(currentSpeed);

  // Ensure motor speed is within valid range (-255 to 255)
  motorSpeed = constrain(motorSpeed, -255, 255);

  // Set motor direction based on speed sign
  motor.setSpeed(motorSpeed);

  // You can add your cleaning and waste collection logic here

  delay(100); // Adjust the delay as needed for your application
}
