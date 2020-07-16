float tmp,tmpc,tmpmv;

void setup()
{
  pinMode(A0,INPUT);
  pinMode(2,OUTPUT);
  pinMode(5,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  tmp = analogRead(A0);
  
  Serial.println("Analog value of tmp ");
  Serial.println(tmp);
  tmpmv=tmp*5000/1024;
  tmpc=(tmpmv/10)+(-50);
  Serial.print("Tmperature is ");
  Serial.println(tmpc);
  if(tmpc<50)
  {
    digitalWrite(2,HIGH);
    digitalWrite(5,LOW);
  }
  else
  {
    digitalWrite(2,LOW);
    digitalWrite(5,HIGH);
  }
}