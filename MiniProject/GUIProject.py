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
onstat = 0

def Mode():
    global mode
    mode = ~mode
    if Change_Mode['text']=='Manual':
        Change_Mode.configure(text='GUI Control')
    elif Change_Mode['text']=='GUI Control':
        Change_Mode.configure(text='Manual')

def reset():
    Joint2_Bar.set(0)
    Joint1_Bar.set(0)

def On():
    global onstat
    BTN_On.configure(bg='green')
    BTN_Off.configure(bg='gray')
    onstat = 1
    
def Off():
    global onstat
    BTN_On.configure(bg='gray')
    BTN_Off.configure(bg='brown')
    pub_Joint2.publish(0)
    pub_Joint1.publish(0)
    onstat = 0

def read_encoder(encode_val):
    sensor_1_read = encode_val.data
    if mode==1:
        Joint1_Bar.set(sensor_1_read)
def read_poten(potenval):
    sensor_2_read = potenval.data
    if mode==1:
        Joint2_Bar.set(sensor_2_read)

def send_data():
    if onstat == 1:
        show_1.config(text= Joint1_Bar.get())
        show_2.config(text= Joint2_Bar.get())
        msg = JointState()
        msg.name = ['joint1', 'joint2']
        msg.position = [(Joint1_Bar.get()*0.056)*10**-3,(-Joint2_Bar.get()*0.47)*10**-3]
        msg.header.stamp = rospy.Time.now()
        Jointpub.publish(msg)
        pub_Joint2.publish(Joint2_Bar.get())
        pub_Joint1.publish(Joint1_Bar.get()*144)
    

def setup():
    msg = JointState()
    msg.name = ['joint1', 'joint2']
    msg.position = [(Joint1_Bar.get()*0.056)*10**-3,(-Joint2_Bar.get()*0.47)*10**-3]
    msg.header.stamp = rospy.Time.now()
    Jointpub.publish(msg)
    pub_Joint2.publish(0)
    pub_Joint1.publish(0)



pub_Joint1 = rospy.Publisher("Topic_Input_Joint1", Int16, queue_size = 10)
pub_Joint2 = rospy.Publisher("Topic_Input_Joint2", Int16, queue_size = 10)
sub_encode = rospy.Subscriber("Topic_Feedback_encode", Int16, callback = read_encoder)
sub_poten = rospy.Subscriber("Topic_Feedback_poten", Int16, callback = read_poten)
Jointpub = rospy.Publisher("joint_states", JointState, queue_size = 10)

gui = tk.Tk()
gui.title('RobotArm')
gui.geometry("660x500")
gui.resizable(False, False)
gui['background']='#274472'

gui.after(1000,setup)

v1 = DoubleVar()
v2 = DoubleVar()



Topic1 = Label(gui, font = font.Font(size = 30, weight='bold', underline = True), anchor="center", fg = "white", text = "Robot Arm", bg="#274472")
Topic1.place(x=210, y=20)



frame_1=Frame(gui, bg="#C3E0E5", highlightbackground="#41729F", highlightthickness=5, width=300, height=360)
frame_1.place(x=20,y=100)

Label_Joint1_Scale = Label(frame_1, font = font.Font(size = 20, weight='bold'), anchor="center", fg = "black", text = "Joint1_Scale", bg="#C3E0E5")
Label_Joint1_Scale.place(x = 50, y =20)
Joint1_Bar = Scale( frame_1, variable=v1, from_ = 0, to = 7, font=font.Font(size = 15), orient = HORIZONTAL,length = 250,width = 40, bg = "#41729F", fg = 'white')
Joint1_Bar.place(x = 20, y = 60)

Label_Joint2_Scale = Label(frame_1, font = font.Font(size = 20, weight='bold'), anchor="center", fg = "black", text = "Joint2_Scale", bg="#C3E0E5")
Label_Joint2_Scale.place(x = 50, y = 150)
Joint2_Bar = Scale( frame_1, variable=v2, from_ = 0, to = 180, font=font.Font(size = 15), orient = HORIZONTAL,length = 250,width = 40, bg = "#41729F", fg = 'white')
Joint2_Bar.place(x = 20, y = 190)



frame_2=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=300, height=260)
frame_2.place(x=340,y=100)

Label_Input = Label(frame_2, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Input", bg="#C3E0E5")
Label_Input.place(x = 90, y = 15)

Label_Joint1 = Label(frame_2, font = font.Font(size = 17, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 45, y = 70)

show_1= Label(frame_2, text="0", font=('Helvetica 40'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
show_1.place(x = 30, y=110)

Label_Joint2 = Label(frame_2, font = font.Font(size = 17, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 170, y = 70)

show_2= Label(frame_2, text="0", font=('Helvetica 40'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
show_2.place(x = 160, y=110)

Label_Change_Mode = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Mode:", bg="#C3E0E5")
Label_Change_Mode.place(x = 25, y = 207)



# frame_3=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=300, height=130,)
# frame_3.place(x=340,y=250)

# Label_Feedback = Label(frame_3, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Feedback", bg="#C3E0E5")
# Label_Feedback.place(x = 50, y = 15)

# Label_Joint1 = Label(frame_3, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
# Label_Joint1.place(x = 15, y = 70)

# Feedback_1= Label(frame_3, text="0", font=('Helvetica 20'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
# Feedback_1.place(x = 85, y=65)

# Label_Joint2 = Label(frame_3, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
# Label_Joint2.place(x = 150, y = 70)

# Feedback_2= Label(frame_3, text="0", font=('Helvetica 20'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
# Feedback_2.place(x = 220, y=65)



#button
Submit = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Submit", bg = "green", command = send_data)
Submit.place(x = 45, y = 280)

Home = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Home", bg = "brown", command = reset)
Home.place(x = 155,y = 280)

Change_Mode = tk.Button(frame_2,font = font.Font(size = 15, weight='bold'), anchor="center",width=10, fg = "white", text = "Manual", bg = "green",activebackground='gray',activeforeground='white', command = Mode)
Change_Mode.place(x = 100,y = 200)

BTN_On = tk.Button(gui,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "ON", bg = "gray",activebackground='green',activeforeground='white',width=5, command = On)
BTN_On.place(x = 395,y = 390)

BTN_Off = tk.Button(gui,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "OFF", bg = "brown",activebackground='red',activeforeground='white',width=5, command = Off)
BTN_Off.place(x = 490,y = 390)

#button

gui.mainloop()