/*#ifndef Encoder_h
#define Encoder_h

#include <Arduino.h>

class Encoder
{
  private:
    int EncoderPinA;
    int EncoderPinB;
    int clearButton;

  public:
    Encoder();
    void EncoderInit(int PinA,int PinB,int Pinclear);
    int Readstate();
    int Encoderread(int aLaststate);
};
#endif*/
