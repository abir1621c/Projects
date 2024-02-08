from tkinter import *
from PIL import Image, ImageTk
import datetime
import time
import pygame



def alarm(set_alarm):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == set_alarm:
            print("Time to Wake up")
            pygame.mixer.init()
            filename =  "C:\\Users\\HP\\CODING\\Python_Coding\\real_loud_alarm.mp3"
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            break

def actual_time():
    set_alarm = f"{hour.get()}:{min.get()}"
    alarm(set_alarm)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x300")

img = Image.open("C:\\Users\\HP\\CODING\\Python_Coding\\alarm.jpg")   
img = img.resize((100,100))
photo = ImageTk.PhotoImage(img)
label = Label(clock, image=photo)
label.image = photo
label.place(x=150, y=10)

time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font=("TIMES NEW ROMAN",10)).place(x=115,y=130)
addTime = Label(clock,text = "Hour  Min",font=60).place(x = 120, y=160)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("TIMES NEW ROMAN",10,"bold")).place(x=0, y=30)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "blue",width = 15).place(x=70,y=180)
minTime= Entry(clock,textvariable = min,bg = "blue",width = 15).place(x=160,y=180)


#To take the time input by user:
Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =140,y=210)
Button(clock, text = "Exit Program", command=clock.quit).place(x=140, y=240)

clock.mainloop()
#Execution of the window.

