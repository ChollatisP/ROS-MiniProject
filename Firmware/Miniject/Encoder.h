#ifndef Encoder_h
#define Encoder_h

#include <Arduino.h>

class Encoder
{
  private:
    int EncoderPinA;
    int EncoderPinB;

  public:
    Encoder(int pinA,int pinB);
    int Readstate();
    int Encoderread(int aLaststate);
};
#endif
