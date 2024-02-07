#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
import os

root = Tk()
root.title('RobotArm')
root.geometry("800x600")
  
v1 = DoubleVar()
  
"""def Joint1():   
    
    sel = "Horizontal Scale Value = " + str(v1.get()) 
    l1.config(text = sel, font =("Courier", 14))"""

Topic1 = Label(root, text = "Joint1")
Topic1.config(font =("Courier", 30))
Topic1.place(x=200, y=20) 

Horizon_Bar = Scale( root, variable = v1,  
            from_ = 1, to = 100, #ระยะบาร์
            orient = HORIZONTAL,
            length = 300,
            width = 50)
Horizon_Bar.place(x=45, y = 50)

Horizon_Label = Label(root,text = "HorizonLabel").place(x = 65, y = 125)

Horizon_Entry_Area = Entry(root,width = 18).place(x = 45 ,y = 100)

root.mainloop()