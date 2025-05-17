const int sensorLuz = A0;  
const int led1 = 10;
const int led2 = 9;
const int led3 = 8;
void setup() { pinMode(sensorLuz, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600);  }
void loop() {
  int valorLuz = analogRead(sensorLuz);
  Serial.println(valorLuz);  
  if (valorLuz < 100) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH); }
  else if (valorLuz < 700) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);}
  else if (valorLuz < 1000) {
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW); }
  else {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);}
  delay(200);
}