#include "Encoder.h"

Encoder::Encoder(int pinA,int pinB)
{
   EncoderPinA = pinA;
   EncoderPinB = pinB;
   pinMode(EncoderPinA, INPUT);
   pinMode(EncoderPinB, INPUT);
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
}
