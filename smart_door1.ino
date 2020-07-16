#include<Servo.h>

Servo ser;

void setup()
{
  pinMode(2, INPUT);
  Serial.begin(9600);
  
  ser.attach(3);
}

void loop()
{
  boolean data = digitalRead(2);
  Serial.print("Motion is ");
  Serial.println(data);
  if(data==1)
    ser.write(180);
  else
    ser.write(0);
    
}