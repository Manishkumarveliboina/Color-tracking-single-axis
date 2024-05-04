#include <Servo.h>

Servo myservo;  // Create a servo object
int servoPin = 9;  // Define the pin for the servo motor
int angle = 90;  // Initial angle for the servo motor

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  myservo.attach(servoPin);  // Attach the servo to the specified pin
  myservo.write(angle);  // Set initial position of the servo
}

void loop() {
  if (Serial.available() > 0) {  // Check if data is available to read
    char command = Serial.read();  // Read the command from serial input
    
    // Move servo based on command
    switch (command) {
      case 'a':
        angle = 180; // Angle for letter A
        break;
      case 'b':
        angle = 170; // Angle for letter B
        break;
      case 'c':
        angle = 160; // Angle for letter C
        break;
      case 'd':
        angle = 150; // Angle for letter D
        break;
      case 'e':
        angle = 140; // Angle for letter E
        break;
      case 'f':
        angle = 130; // Angle for letter F
        break;
      case 'g':
        angle = 120; // Angle for letter G
        break;
      case 'h':
        angle = 110; // Angle for letter H
        break;
      case 'i':
        angle = 100; // Angle for letter I
        break;
      case 'j':
        angle = 90; // Angle for letter J
        break;
      case 'k':
        angle = 80; // Angle for letter K
        break;
      case 'l':
        angle = 70; // Angle for letter L
        break;
      case 'm':
        angle = 60; // Angle for letter M
        break;
      case 'n':
        angle = 50; // Angle for letter N
        break;
      case 'o':
        angle = 40; // Angle for letter O
        break;
      case 'p':
        angle = 30; // Angle for letter P
        break;
      case 'q':
        angle = 20; // Angle for letter Q
        break;
      case 'r':
        angle = 10; // Angle for letter R
        break;
      case 's':
        angle = 0; // Angle for letter S
        break;
      default:
        break;
    }
    
    myservo.write(angle);  // Move the servo to the new angle
    Serial.print("Servo position set to: ");
    Serial.println(angle);
  }
}
