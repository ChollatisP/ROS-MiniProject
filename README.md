# ROS Miniproject

## Description

ROS Miniproject for PP robot control with Python GUI, Encoder and Potentiometer using Arduino UNO R3.

## Table of Content
- [ROS Miniproject](#ros-miniproject)
  - [Description](#description)
  - [Table of Content](#table-of-content)
  - [Component](#component)
    - [Software](#software)
    - [Hardware](#hardware)
  - [Installing](#installing)
    - [Executing program](#executing-program)
  - [Authors](#authors)
  - [Acknowledgments](#acknowledgments)


## Component

### Software
* Ubuntu 20.04

* ROS Noetic 

* Python3

* Arduino IDE 1.8.15
  
* [Arduino ROSSerial Library into Arduino IDE](https://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)

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
  - DT 2
  - CLK 3
  - SW 8
  - (+) to 5V
  - GND to GND
* Connect Stepper motor
  - Power supply into Driver Board
    - Power supply 12V to VMOD
    - GND to GND
  - Stepper into Driver Board
    - A(Black) to 2A 
    - A-(Green) to 1A
    - B-(Blue) to 1B
    - B(Red) to 2B
  - Driver Board into Arduino
    - DIR 4
    - STP 7
    - FLT to 5V
    - GND to GND
* Connect Servo motor
    - PWM(Orange) 12
    - Vcc(Red) to 5V
    - Ground(Brown) to 
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

* Kantawit Panyateang 6452500198

* Komgrid Petchpayub 6452500392


## Acknowledgments

* [Potentiometer Stabilizer](https://docs.arduino.cc/built-in-examples/analog/Smoothing/)

* [Rotary Encoder](https://forum.arduino.cc/t/rotary-encoder-increment-decrement/858119)

* [Stepper Motor Control](https://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/)

* [Tkinter_tutorial1](https://pythonexamples.org/python-tkinter/)

* [Tkinter_tutorial2](https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/?ref=lbp)

* [Launch file](https://dev.to/admantium/robot-operating-system-creating-a-robot-simulation-45f1) 

* [Simple Readme](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)