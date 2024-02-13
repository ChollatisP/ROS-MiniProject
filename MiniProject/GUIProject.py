#!/usr/bin/env python3
from tkinter import*
from tkinter import font
from tkinter import messagebox
from sensor_msgs.msg import JointState
import tf
import tkinter as tk
import rospy
from std_msgs.msg import Int16
rospy.init_node("RobotArm_Control")
rate = rospy.Rate(10)

'''rate.sleep()

def Talker(val):
	cmd_val = Int16(val)
	rospy.loginfo(cmd_val)
	pub.publish(cmd_val)'''
def read_encoder(encode_val):
	sensor_1_read = encode_val.data
	Feedback_1.config(text = str(sensor_1_read))
def read_poten(potenval):
    sensor_2_read = potenval.data
    Feedback_2.config(text = str(sensor_2_read))
def reset():  
    Horizon_Bar.set(0)
    Vertical_Bar.set(0)
def clear():  
    show_1.config(text="0")
    show_2.config(text="0")
def send_data():
    show_1.config(text= Horizon_Bar.get())
    show_2.config(text= Vertical_Bar.get())
    msg = JointState()
    msg.name = ['joint1', 'joint2']
    msg.position = [Horizon_Bar.get(),Vertical_Bar.get()]
    Jointpub.publish(msg)
def get_data():
    ()



#pub_encode = rospy.Publisher("Topic_Input_encode", Int16, queue_size = 10)
#pub_poten = rospy.Publisher("Topic_Input_poten", Int16, queue_size = 10)
sub_encode = rospy.Subscriber("Topic_Feedback_encode", Int16, callback = read_encoder)
sub_poten = rospy.Subscriber("Topic_Feedback_poten", Int16, callback = read_poten)
Jointpub = rospy.Publisher("joint_state", JointState, queue_size = 10)

gui = tk.Tk()
gui.title('RobotArm')
gui.geometry("800x550")
gui.resizable(False, False)
gui['background']='#274472'


v1 = DoubleVar()
v2 = DoubleVar()



Topic1 = Label(gui, font = font.Font(size = 35, weight='bold', underline = True), anchor="center", fg = "white", text = "Robot Arm", bg="#274472")
Topic1.place(x=270, y=20)



frame_1=Frame(gui, bg="#C3E0E5", highlightbackground="#41729F", highlightthickness=5, width=350, height=400)
frame_1.place(x=25,y=110)

Label_Horizontal = Label(frame_1, font = font.Font(size = 20, weight='bold'), anchor="center", fg = "black", text = "Joint1_Horizontal", bg="#C3E0E5")
Label_Horizontal.place(x = 55, y =20)
Horizon_Bar = Scale( frame_1, variable=v1, from_ = 0, to = 100, font=font.Font(size = 15), orient = HORIZONTAL,length = 300,width = 50, bg = "#41729F", fg = 'white',resolution = 0.5)
Horizon_Bar.place(x = 15, y = 60)

Label_Vertical = Label(frame_1, font = font.Font(size = 20, weight='bold'), anchor="center", fg = "black", text = "Joint2_Vertical", bg="#C3E0E5")
Label_Vertical.place(x = 70, y = 180)
Vertical_Bar = Scale( frame_1, variable=v2, from_ = 0, to = 100, font=font.Font(size = 15), orient = HORIZONTAL,length = 300,width = 50, bg = "#41729F", fg = 'white',resolution = 0.5)
Vertical_Bar.place(x = 15, y = 220)



frame_2=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=350, height=400)
frame_2.place(x=425,y=110)

Label_Input = Label(frame_2, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Input", bg="#C3E0E5")
Label_Input.place(x = 125, y = 15)

Label_Joint1 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 10, y = 100)

show_1= Label(frame_2, text="0", font=('Helvetica 25'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=4)
show_1.place(x = 80, y=90)

Label_Joint2 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 170, y = 100)

show_2= Label(frame_2, text="0", font=('Helvetica 25'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=4)
show_2.place(x = 240, y=90)

Label_Feedback = Label(frame_2, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Feedback", bg="#C3E0E5")
Label_Feedback.place(x = 90, y = 175)

Label_Joint1 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 10, y = 260)

Feedback_1= Label(frame_2, text="0", font=('Helvetica 25'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=4)
Feedback_1.place(x = 80, y=250)

Label_Joint2 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 170, y = 260)

Feedback_2= Label(frame_2, text="0", font=('Helvetica 25'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=4)
Feedback_2.place(x = 240, y=250)



#button
Submit = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Submit", bg = "green", command = send_data)
Submit.place(x = 90, y = 320)

Home = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Home", bg = "brown", command = reset)
Home.place(x = 180,y = 320)

Get_Data = tk.Button(frame_2,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Get_Data", bg = "green", command = get_data)
Get_Data.place(x = 80,y = 320)

Clear = tk.Button(frame_2,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Clear", bg = "brown", command = clear)
Clear.place(x = 190,y = 320)
#button

gui.mainloop()