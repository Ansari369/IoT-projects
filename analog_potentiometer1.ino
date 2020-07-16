void setup()
{
  pinMode(A0,INPUT);
  Serial.begin(9600);
  pinMode(3,OUTPUT);
  
}

void loop()
{
  int values = analogRead(A0);
  int ledvalues=map(values,0,1023,0,255);
  analogWrite(3,ledvalues);
  
  Serial.print("Analog Value ");
  Serial.println(ledvalues);
}