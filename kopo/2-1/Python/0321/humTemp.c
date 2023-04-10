#include
<wiringPi.h
>
#include
<stdio.h
>
#define MAXTIMINGS 85
#define DHTPIN
2
int dhtVal[5] = { 0, 0, 0, 0, 0 };
void readData() {
int laststate = HIGH;
int counter = 0;
int j = 0, i;
float f; /* fahrenheit */
dhtVal[0] = dhtVal[1] = dhtVal[2] = dhtVal[3] = dhtVal[4] = 0;
/* pull pin down for 18 milliseconds */
pinMode
(DHTPIN, OUTPUT);
digitalWrite
(DHTPIN, LOW);
delay(18);
/* then pull it up for 40 microseconds */
digitalWrite
(DHTPIN, HIGH);
delayMicroseconds(40);
/* prepare to read the pin */
pinMode
(DHTPIN, INPUT);