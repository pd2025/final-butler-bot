#include <DRV8835MotorShield.h>

// Open claw and close claw
//use ultra sonic to sense can

DRV8835MotorShield motors;
#define trigPin 3
#define echoPin 2
long duration;
int distanceCm, distanceInch;
bool closed = false;
void setup() {
  Serial.begin(9600);
  motors.flipM1(true);
  motors.flipM2(true);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * 0.034 / 2;
  distanceInch = duration * 0.0133 / 2;
  Serial.print("Current distance: ");
  Serial.println(distanceCm);
  if (/*!closed && */distanceCm <= 10) {  // close
    motors.setM1Speed(100);
    delay(500);
    motors.setM1Speed(0);
    delay(1000);
    //closed = true;
  }
  else /*if (closed && distanceCm > 10)*/ {  // open
    motors.setM1Speed(-100);
    delay(500);
    motors.setM1Speed(0);
    delay(1000);
    //closed = false;
  }
} (edited) 