#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/UInt16.h>
#include <Servo.h>
#define potenpin A5
#define encoderPinA 2
#define encoderPinB 3
#define clearButton 8

ros::NodeHandle  nh;
std_msgs::Int16 encoderData;
std_msgs::Int16 potenData;
const int stepPin = 3; 
const int dirPin = 2; 

Servo servo;

ros::Publisher Encodepub("Topic_Feedback_encode", &encoderData );
ros::Publisher Potenpub("Topic_Feedback_poten", &potenData );

volatile unsigned int encoderPos = 0;  // สำหรับนับจำนวน
unsigned int lastReportedPos = 1;   // change management
static boolean rotating = false;    // debounce management

boolean A_set = false;
boolean B_set = false;
int laststeppos = 0;

void servocontrol(const std_msgs::Int16& cmd_msg)
{
  int value = cmd_msg.data;
  servo.write(value);
}

void stepcontrol(const std_msgs::Int16& cmd_msg)
{
  int value = cmd_msg.data;
  if (value > laststeppos)
  {
    int timecheck = value-laststeppos;
    digitalWrite(dirPin,HIGH);
    digitalWrite(stepPin,HIGH);
    delay(timecheck*1000);
    digitalWrite(stepPin,LOW);
  }
  else if (value < laststeppos)
  {
    int timecheck = value-laststeppos;
    digitalWrite(dirPin,LOW);
    digitalWrite(stepPin,HIGH);
    delay(timecheck*1000);
    digitalWrite(stepPin,LOW);
  }
  else
  {
    digitalWrite(stepPin,LOW);
  }
  laststeppos = value;
}

ros::Subscriber<std_msgs::Int16> potensub("Topic_Input_Joint2", &servocontrol );
ros::Subscriber<std_msgs::UInt16> encodersub("Topic_Input_Joint1", &stepcontrol);

void setup() 
{ 
   pinMode(encoderPinA, INPUT_PULLUP); // กำหนดโหมดเป็นแบบ Input pullup
   pinMode(encoderPinB, INPUT_PULLUP);
   pinMode(clearButton, INPUT_PULLUP);
   attachInterrupt(0, doEncoderA, CHANGE); //ทำงานแบบ interrupt เบอร์ 0 ในนี้คือขา pin 2
   attachInterrupt(1, doEncoderB, CHANGE); //ทำงานแบบ interrupt เบอร์ 1 ในนี้คือขา pin 3
   pinMode(stepPin,OUTPUT); 
   pinMode(dirPin,OUTPUT);
   nh.initNode();
   nh.advertise(Encodepub);  
   nh.advertise(Potenpub);
 } 

float floatMap(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void loop() { 
  int poten = analogRead(A5);
  float voltage = floatMap(poten, 0, 1023, 0, 180);
  potenData.data = voltage;
  Potenpub.publish(&potenData);
  rotating = true;  // reset the debouncer
  if (lastReportedPos != encoderPos) {
    int newencoderPos;
    if (encoderPos>=180)
    {
      newencoderPos = 180;
    }
    else if (encoderPos<=0)
    {
      newencoderPos = 0;
    }
    else
    {
      newencoderPos = encoderPos;
    }
    lastReportedPos = encoderPos;
    encoderData.data = newencoderPos;
    Encodepub.publish(&encoderData);
  }
  if (digitalRead(clearButton) == LOW )  {
    encoderPos = 0;
    delay(200);
  }
  nh.spinOnce();
  delay(1);
 }

 
void doEncoderA() {
  // debounce
  if ( rotating ) delay (1);  // หน่วงเวลาป้องกันสัญญาณบกวน debounce

  // เช็คว่ามีบิดสวิตช์
  if ( digitalRead(encoderPinA) != A_set ) { // debounce once more
    A_set = !A_set;
    // adjust counter + if A leads B
    if ( A_set && !B_set )
      encoderPos += 1;
    rotating = false;  // no more debouncing until loop() hits again
  }
}

// Interrupt on B changing state, same as A above
void doEncoderB() {
  if ( rotating ) delay (1);
  if ( digitalRead(encoderPinB) != B_set ) {
    B_set = !B_set;
    //  adjust counter - 1 if B leads A
    if ( B_set && !A_set )
      encoderPos -= 1;
    rotating = false;
  }
}
