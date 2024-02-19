# ROS Miniproject

## Description

ROS Miniproject for PP robot control with Python GUI, Encoder and Potentiometer using Arduino UNO R3.

## Component

### Software
* Ubuntu 20.04

* ROS Noetic 

* Python3

* Arduino 18.....

* Arduino ROS Library

### Hardware
* Arduino UNO R3

* 50K Potentiometer

* KY-040 Rotary Encoder (WH-040)

* MG90S Servo motor

* Usongshine 17hs4401 (Stepper motor)

* DRV8825 Stepper motor driver board

* 12V or Higher Power supply 

* Photoboard (Optional)

## Installing

* Connect Potentiometer into Arduino using A0 pin on Arduino

* Connect Encoder into Arduino 
    - PinA 2
    - PinB 3
    - Clear 8
* Connect Stepper motor
* 
* Run this Command in terminal
```
cd catkin_ws/src
git clone https://github.com/ChollatisP/ROS-MiniProject.git
cd catkin_ws
catkin_make
```
* Open Firmware directory and continue to miniject directory and open Miniject.ino
* Upload Miniject.ino into your Arduino

### Executing program

* Run this command on your terminal
```
roslaunch robotarm rviz.launch
```

## Authors

* Chollatis Petchsing 6452500023
* Kantawit    6452500198
* Komgrid Petchpayub 6452500392


## Acknowledgments

Inspiration, code snippets, etc.
* [Potentiometer Stabilizer](https://docs.arduino.cc/built-in-examples/analog/Smoothing/)
* [Simple Readme](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Rotary Encoder](https://forum.arduino.cc/t/rotary-encoder-increment-decrement/858119)
* [Stepper Motor Control](https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/)

