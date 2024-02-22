# ROS Miniproject

## Description

ROS Miniproject for PP robot control with Python GUI, Encoder and Potentiometer using Arduino UNO R3.

## Table of Content
- [ROS Miniproject](#ros-miniproject)
  - [Description](#description)
  - [Table of Content](#table-of-content)
  - [CAD design](#cad-design)
    - [- Base](#--base)
    - [- Joint1](#--joint1)
    - [- Joint2](#--joint2)
  - [Assembly](#assembly)
  - [Component](#component)
    - [Software](#software)
    - [Hardware](#hardware)
  - [Installing](#installing)
    - [Executing program](#executing-program)
  - [Authors](#authors)
  - [Acknowledgments](#acknowledgments)

## CAD design
### - Base

<img src="https://github.com/ChollatisP/ROS-MiniProject/blob/DONE/CAD_Assembly/base.png" width=35% height=35%>

### - Joint1

<img src="https://github.com/ChollatisP/ROS-MiniProject/blob/DONE/CAD_Assembly/Joint1.png" width=35% height=35%>

### - Joint2

<img src="https://github.com/ChollatisP/ROS-MiniProject/blob/DONE/CAD_Assembly/Joint2.png" width=35% height=35%>

## Assembly
<img src="https://github.com/ChollatisP/ROS-MiniProject/blob/DONE/CAD_Assembly/Assembly.png" width=50% height=50%>

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

## Installing and Executing program

### Hardware
* Connect Potentiometer into Arduino using A0 pin on Arduino

* Connect Encoder into Arduino 
  - DT to 2
  - CLK to 3
  - SW to 8
  - (+) to 5V
  - GND to GND
* Connect Stepper
  - Stepper Driver Board
    - Jump SLP and RST
    - [V.ref tunning](https://ardufocus.com/howto/a4988-motor-current-tuning/)
  - Power supply into Driver Board
    - Power supply 12V to VMOD
    - GND to GND
  - Stepper into Driver Board
    - A(Black) to 2A 
    - A-(Green) to 1A
    - B-(Blue) to 1B
    - B(Red) to 2B
  - Driver Board into Arduino
    - DIR to 4
    - STP to 7
    - FLT to 5V
    - GND to GND
* Connect Servo motor
    - PWM(Orange) 12
    - Vcc(Red) to 5V
    - Ground(Brown) to GND

### Software
1. Go to source folder in your workspace by run this command.
  
```
cd catkin_ws/src
```
2. Clone all file in github repository by git clone command.

```
git clone https://github.com/ChollatisP/ROS-MiniProject.git
```
3. Go back to your workspace by this command.

```
cd ~/catkin_ws
```
4. Run catkin_make command to activate package to ROS environment.

```
catkin_make
``` 
5. Open Firmware directory and continue to miniject directory and open Miniject.ino

6. Upload Miniject.ino into your Arduino **This will show you your serial port**
**and Do not forget to plug usb from arduino to your computer**
7. Or sun this command to check port.
```
dmesg* Example -> My serial port is /dev/ttyUSB0. 
* My command gona be like this.

```

8. Run this command on your terminal to launch code.
```
roslaunch robotarm rviz.launch port:="<--YOUR-PORT-->"
```
* Example -> My serial port is /dev/ttyUSB0. 
* My command gona be like this.

```
roslaunch robotarm rviz.launch port:="/dev/ttyUSB0"
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
