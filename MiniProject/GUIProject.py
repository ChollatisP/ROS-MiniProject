#!/usr/bin/env python3
from tkinter import*
from tkinter import font
from tkinter import messagebox
import tkinter as tk

gui = tk.Tk()
gui.title('RobotArm')
gui.geometry("800x550")
gui.resizable(False, False)
gui['background']='#274472'

v1 = DoubleVar()
v2 = DoubleVar()

def reset():  
    Horizon_Bar.set(0)
    Vertical_Bar.set(0)

def get_data():
    show_1.config(text= Horizon_Bar.get(), font= ('Helvetica 25'))
    show_2.config(text= Vertical_Bar.get(), font= ('Helvetica 25'))

def refresh():  
    show_1.config(text="")
    show_2.config(text="")


Topic1 = Label(gui, font = font.Font(size = 35, weight='bold', underline = True), anchor="center", fg = "white", text = "Robot Arm", bg="#274472")
Topic1.place(x=270, y=20)

frame_1=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=350, height=400)
frame_1.place(x=25,y=110)

Label_Horizontal = Label(frame_1, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Horizontal", bg="#C3E0E5")
Label_Horizontal.place(x = 85, y =15)
Horizon_Bar = Scale( frame_1, variable = v1, from_ = 0, to = 100, font=font.Font(size = 15), orient = HORIZONTAL,length = 300,width = 50, bg = "#41729F", fg = 'white')
Horizon_Bar.place(x = 15, y = 60)

Label_Vertical = Label(frame_1, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Vertical", bg="#C3E0E5")
Label_Vertical.place(x = 100, y = 175)
Vertical_Bar = Scale( frame_1, variable = v2, from_ = 0, to = 100, font=font.Font(size = 15), orient = HORIZONTAL,length = 300,width = 50, bg = "#41729F", fg = 'white')
Vertical_Bar.place(x = 15, y = 220)



frame_2=Frame(gui, bg="#C3E0E5",highlightbackground="#41729F",highlightthickness=5, width=350, height=400)
frame_2.place(x=425,y=110)

Label_Input = Label(frame_2, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Input", bg="#C3E0E5")
Label_Input.place(x = 125, y = 15)

Label_Joint1 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 20, y = 100)

show_1= Label(frame_2, text="", font=('Helvetica 25'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
show_1.place(x = 90, y=90)

Label_Joint2 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 180, y = 100)

show_2= Label(frame_2, text="", font=('Helvetica 25'), bg='#C3E0E5', fg='red',highlightbackground="black",highlightthickness=2,width=3)
show_2.place(x = 250, y=90)

Label_Feedback = Label(frame_2, font = font.Font(size = 25, weight='bold'), anchor="center", fg = "black", text = "Feedback", bg="#C3E0E5")
Label_Feedback.place(x = 100, y = 175)

Label_Joint1 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint1", bg="#C3E0E5")
Label_Joint1.place(x = 20, y = 260)

Label_Joint2 = Label(frame_2, font = font.Font(size = 15, weight='bold'), anchor="center", fg = "black", text = "Joint2", bg="#C3E0E5")
Label_Joint2.place(x = 180, y = 260)


#button
Start = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Submit", bg = "green", command = get_data)
Start.place(x = 90, y = 320)

Home = tk.Button(frame_1,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Home", bg = "brown", command = reset)
Home.place(x = 180,y = 320)

Refresh = tk.Button(frame_2,font = font.Font(size = 15, weight='bold'), anchor="center", fg = "white", text = "Refresh", bg = "red", command = refresh)
Refresh.place(x = 120,y = 320)

#button



gui.mainloop()