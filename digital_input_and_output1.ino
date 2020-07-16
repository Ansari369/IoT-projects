void setup()
{
  pinMode(2,INPUT);
  pinMode(3,OUTPUT);
  
  Serial.begin(9600);
}

void loop()
{
  boolean data = digitalRead(2);
  
  digitalWrite(3,data);
  
  Serial.println(data);
}