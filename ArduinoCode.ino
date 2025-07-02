#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();
  int gas = analogRead(A0); // MQ-3 sensor
  Serial.print(temp); Serial.print(",");
  Serial.print(humidity); Serial.print(",");
  Serial.println(gas);
  delay(2000);
}
