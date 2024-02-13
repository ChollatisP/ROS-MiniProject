/*#include "Encoder.h"

Encoder::Encoder()
{
   
}

volatile unsigned int encoderPos = 0;  // สำหรับนับจำนวน
unsigned int lastReportedPos = 1;   // change management
static boolean rotating = false;    // debounce management

boolean A_set = false;
boolean B_set = false;
void Encoder::EncoderInit(int PinA,int PinB,int Pinclear)
{
  encoderPinA = PinA;
  encoderPinB = PinB;
  clearButton = Pinclear;
  pinMode(encoderPinA, INPUT_PULLUP); // กำหนดโหมดเป็นแบบ Input pullup
  pinMode(encoderPinB, INPUT_PULLUP);
  pinMode(clearButton, INPUT_PULLUP);
  attachInterrupt(0, doEncoderA, CHANGE); //ทำงานแบบ interrupt เบอร์ 0 ในนี้คือขา pin 2
  attachInterrupt(1, doEncoderB, CHANGE); //ทำงานแบบ interrupt เบอร์ 1 ในนี้คือขา pin 3
}

int Encoder::Readstate()
{
   return  digitalRead(EncoderPinA);
}
int Encoder::Encoderread(int curposition)
{
  int counter = 0; 
  int aState = digitalRead(EncoderPinA);
   if (aState != curposition){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(EncoderPinB) != aState) { 
       counter ++;
     } else {
       counter --;
     }
   } 
   int newposition = aState; // Updates the previous state of the outputA with the current state
   return newposition;
}*/
