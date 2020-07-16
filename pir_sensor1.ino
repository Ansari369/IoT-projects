void setup()
{
  pinMode(2, INPUT);
  Serial.begin(9600);
}

void loop()
{
  boolean data = digitalRead(2);
  Serial.print("Motion is ");
  Serial.println(data);
  if(data==1)
    digitalWrite(3,HIGH);
  else
    digitalWrite(3,LOW);
    
  delay(1000);
  
}