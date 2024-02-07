 
#include <ros.h>
#include <std_msgs/Int16.h>
#include "Encoder.h"
#define potenpin A0

ros::NodeHandle  nh;
std_msgs::Int16 encoderData;
std_msgs::Int16 potenData;

ros::Publisher Encodepub("Encodersend", &encoderData );
ros::Publisher Potenpub("Potensend", &potenData );

Encoder En1(1,2);
int aState;
int aLastState;  

void setup() 
{ 
   aLastState = En1.Readstate(); 
   nh.initNode();
   nh.advertise(Encodepub);  
   nh.advertise(Potenpub);
 } 

float floatMap(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void loop() { 
  float voltage = floatMap(analogRead(potenpin), 0, 1023, 0, 5);
  potenData.data = voltage;
  aLastState = En1.Encoderread(aLastState);
  encoderData.data = aLastState;
  Encodepub.publish(&encoderData);
  Potenpub.publish(&potenData);
  nh.spinOnce();
  delay(1);
 }
