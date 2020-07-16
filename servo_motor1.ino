#include<Servo.h>

Servo ser;

void setup()
{
  ser.attach(3);
}

void loop()
{
  ser.write(0);
  delay(1000);
  ser.write(180);
  delay(1000);
  
}