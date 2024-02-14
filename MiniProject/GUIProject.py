#!/usr/bin/env python3
from tkinter import*
from tkinter import font
from tkinter import messagebox
import tkinter as tk
from sensor_msgs.msg import JointState
import tf
import rospy
from std_msgs.msg import Int16
rospy.init_node("RobotArm_Control")
rate = rospy.Rate(10)
mode = 1
'''rate.sleep()

def Talker(val):
	cmd_val = Int16(val)
	rospy.loginfo(cmd_val)
	pub.publish(cmd_val)'''
def get_data():
    global mode
    mode = ~mode

def read_encoder(encode_val):
    sensor_1_read = encode_val.data
    if mode==1:
        Joint1_Bar.set(sensor_1_read)
def read_poten(potenval):
    sensor_2_read = potenval.data
    if mode==1:
        Joint2_Bar.set(sensor_2_read)

def reset():
    Joint1_Bar.set(0)
    Joint2_Bar.set(0)

def send_data():
    show_1.config(text= Joint1_Bar.get())
    show_2.config(text= Joint2_Bar.get())
    msg = JointState()
    msg.name = ['joint1', 'joint2']
    msg.position = [Joint1_Bar.get(),Joint2_Bar.get()]
    Jointpub.publish(msg)
    pub_Joint1.publish(Joint1_Bar.get())
    pub_Joint2.publish(Joint2_Bar.get())



pub_Joint1 = rospy.Publisher("Topic_Input_Joint1", Int16, queue_size = 10)
pub_Joint2 = rospy.Publisher("Topic_Input_Joint2", Int16, queue_size = 10)
sub_encode = rospy.Subscriber("Topic_Feedback_encode", Int16, callback = read_encoder)
sub_poten = rospy.Subscriber("Topic_Feedback_poten", Int16, callback = read_poten)
Jointpub = rospy.Publisher("joint_state", JointState, queue_size = 10)

gui = tk.Tk()
gui.title('RobotArm')
gui.geometry("660x500")
gui.resizable(False, False)
gui['background']='#274472'



v1 = DoubleVar()
v2 = DoubleVar()



Topic1 = Label(gui, font = font.Font(size = 30, weight='bold', underline = True), anchor="center", fg = "white", text = "Robot Arm", bg="#274472")
Topic1.place(x=210, y=20)



frame_1=Frame(gui, bg="#C3E0E5", highlightbackground="#41729F", highlightthickness=5, width=300, height=360)
frame_1.place(x=20,y=100)

Label_Joint1_Scale = Label(frame_1, font = font.Font(size = 20, weight='bold'), anchor="center", fg = "black", text = "Joint1_Scale", bg="#C3E0E5")
Label_Joint1_Scale.place(x = 50, y =20)
Joint1_Bar = Scale( frame_1, variable=v1, from_ = 0, to = 100, font=font.Font(size = 15), orient = HORIZONTAL,length = 250,width = 40, bg = "#41729F", fg = 'white')
Joint1_Bar.place(x = 20, y = 60)

Label_Joint2_Scale = Label(frame_1, font = font.Font(size = 20, weight='bold'), anchor="center", fg = "black", text = "Joint2_Scale", bg="#C3E0E5")
Label_Joint2_Scale.place(x = 50, y = 150)
Joint2_Bar = Scale( frame_1, variable=v2, from_ = 0, to = 100, font=font.Font(size = 15), orient = HORIZONTAL,length = 250,width = 40, bg = "#41729F", fg = 'white')
Joint2_Bar.place(x = 20, y = 190)



frame_2=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=300, height=130)
frame_2.place(x=340,y=100)

Label_Input = Label(frame_2, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Input", bg="#C3E0E5")
Label_Input.place(x = 90, y = 15)

Label_Joint1 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 15, y = 70)

show_1= Label(frame_2, text="0", font=('Helvetica 20'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
show_1.place(x = 85, y=65)

Label_Joint2 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 150, y = 70)

show_2= Label(frame_2, text="0", font=('Helvetica 20'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
show_2.place(x = 220, y=65)



frame_3=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=300, height=130)
frame_3.place(x=340,y=250)

Label_Feedback = Label(frame_3, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Feedback", bg="#C3E0E5")
Label_Feedback.place(x = 50, y = 15)

Label_Joint1 = Label(frame_3, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 15, y = 70)

Feedback_1= Label(frame_3, text="0", font=('Helvetica 20'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
Feedback_1.place(x = 85, y=65)

Label_Joint2 = Label(frame_3, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 150, y = 70)

Feedback_2= Label(frame_3, text="0", font=('Helvetica 20'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
Feedback_2.place(x = 220, y=65)



#button
Submit = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Submit", bg = "green", command = send_data)
Submit.place(x = 45, y = 280)

Home = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Home", bg = "brown", command = reset)
Home.place(x = 155,y = 280)

Get_Data = tk.Button(gui,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Mode", bg = "green", command = get_data)
Get_Data.place(x = 440,y = 400)

'''Clear = tk.Button(frame_2,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Clear", bg = "brown", command = clear)
Clear.place(x = 175,y = 310)'''
#button

gui.mainloop()