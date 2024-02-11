import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import pygame
import threading
from tkcalendar import Calendar

def alarm(set_alarm):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm:
            print("Time to Wake up")
            pygame.mixer.init()
            filename =  "C:\\Users\\HP\\CODING\\Python_Coding\\real_loud_alarm.mp3"
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            break
        else:
            current_day = datetime.datetime.now().strftime("%A")
            if current_day == set_alarm:
                print(f"Alarm will be repeated for {set_alarm}")

def set_alarm_time():
    global alarm_time # global variable
    try:
        alarm_hour = int(hour_combobox.get())
        alarm_minute = int(minute_combobox.get())
        alarm_second = int(second_combobox.get())

        current_time = datetime.datetime.now()
        selected_time = datetime.datetime.combine(calendar.selection_get(), datetime.time(alarm_hour, alarm_minute, alarm_second))

        if repeat_combobox.get() == "None":
            if selected_time < current_time:
                print("Invalid Input: Alarm time cannot be in the past.")
                return

            time_difference = selected_time - current_time
            days_left = time_difference.days
            hours_left, remainder = divmod(time_difference.seconds, 3600)
            minutes_left, seconds_left = divmod(remainder, 60)
            print(f"Alarm set for {days_left} days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds from now")
            alarm_time = selected_time.strftime("%H:%M:%S")
            threading.Thread(target=alarm, args=(alarm_time,)).start()
        else:
            if selected_time < current_time:
                print("Selected time is in the past. Setting alarm for the next occurrence of the selected day(s).")
                selected_days = [days[i] for i, day_var in enumerate(custom_day_vars) if day_var.get() == 1]
                if not selected_days:
                    print("Invalid Input: Please select at least one day for custom alarm.")
                    return

                # Find the next occurrence of the selected day(s)
                for day in selected_days:
                    days_until_selected_day = (days.index(day) - current_time.weekday()) % 7
                    next_selected_day = current_time + datetime.timedelta(days=days_until_selected_day)
                    alarm_time = next_selected_day.replace(hour=alarm_hour, minute=alarm_minute, second=alarm_second)
                    threading.Thread(target=alarm, args=(alarm_time.strftime("%H:%M:%S"),)).start()
                    print(f"Alarm set for next occurrence of {day}")

            else:
                alarm_repeat_option = repeat_combobox.get()
                if alarm_repeat_option == "Daily":
                    alarm_time = selected_time.strftime("%H:%M:%S")
                    threading.Thread(target=alarm, args=(alarm_time,)).start()
                    print("Alarm set for daily")
                elif alarm_repeat_option == "Mon to Fri":
                    alarm_time = selected_time.strftime("%H:%M:%S")
                    # Find the nearest upcoming Monday
                    days_until_monday = (0 - selected_time.weekday()) % 7
                    next_monday = selected_time + datetime.timedelta(days=days_until_monday)
                    alarm_time = next_monday.strftime("%H:%M:%S")
                    threading.Thread(target=alarm, args=(alarm_time,)).start()
                    print("Alarm set for Mon to Fri starting from the next Monday")
                elif alarm_repeat_option == "Custom":
                    custom_days = [day_var.get() for day_var in custom_day_vars]
                    if sum(custom_days) == len(custom_days):
                        alarm_time = selected_time.strftime("%H:%M:%S")
                        threading.Thread(target=alarm, args=(alarm_time,)).start()
                        print("Alarm set for daily")
                    else:
                        selected_days = [days[i] for i, day in enumerate(custom_days) if day == 1]
                        if not selected_days:
                            print("Invalid Input: Please select at least one day for custom alarm.")
                            return

                        # Find the next occurrence of the selected day(s)
                        for day in selected_days:
                            days_until_selected_day = (days.index(day) - current_time.weekday()) % 7
                            next_selected_day = current_time + datetime.timedelta(days=days_until_selected_day)
                            alarm_time = next_selected_day.replace(hour=alarm_hour, minute=alarm_minute, second=alarm_second)
                            threading.Thread(target=alarm, args=(alarm_time.strftime("%H:%M:%S"),)).start()
                            print(f"Alarm set for next occurrences of {day}")

                else:
                    print("Invalid repeat option selected.")
    except ValueError as e:
        print("Invalid input:", e)

def update_current_time():
    current_time = datetime.datetime.now()
    current_time_str = current_time.strftime("%A, %B %d, %Y %H:%M:%S")
    time_label.config(text=current_time_str)
    time_label.after(1000, update_current_time)  # Schedule the next update

def update_custom_days_visibility(event):
    custom_days_frame.place(relx=0.5, rely=0.45, anchor=tk.CENTER)  # Place the frame at the desired position
    if repeat_combobox.get() != "Custom":
        custom_days_frame.place_forget()  # Hide custom days frame if option is not "Custom"

# Initialize Tkinter
clock = tk.Tk()
clock.title("Alarm Clock") 
clock.geometry("600x800")  # Increased height to accommodate the new dropdown

# Load and display image
img = Image.open("C:\\Users\\HP\\CODING\\Python_Coding\\alarm.jpg")   
img = img.resize((100,100))
photo = ImageTk.PhotoImage(img)
label = tk.Label(clock, image=photo)
label.image = photo
label.pack(pady=10)

time_format = tk.Label(clock, text= "Enter time in 24 hour format!", fg="black",bg="white",font=("TIMES NEW ROMAN",10))
time_format.pack(pady=(0, 5))

hour_label = tk.Label(clock, text="Hour", font=("TIMES NEW ROMAN", 10))
hour_label.pack()
hour_combobox = ttk.Combobox(clock, width=5, values=[str(i).zfill(2) for i in range(24)])
hour_combobox.pack()

minute_label = tk.Label(clock, text="Minute", font=("TIMES NEW ROMAN", 10))
minute_label.pack()
minute_combobox = ttk.Combobox(clock, width=5, values=[str(i).zfill(2) for i in range(60)])
minute_combobox.pack()

second_label = tk.Label(clock, text="Second", font=("TIMES NEW ROMAN", 10))
second_label.pack()
second_combobox = ttk.Combobox(clock, width=5, values=[str(i).zfill(2) for i in range(60)])
second_combobox.pack()

repeat_label = tk.Label(clock, text="Repeat Option", font=("TIMES NEW ROMAN", 10))
repeat_label.pack()
repeat_combobox = ttk.Combobox(clock, width=15, values=["None", "Daily", "Mon to Fri", "Custom"])
repeat_combobox.pack()
repeat_combobox.bind("<<ComboboxSelected>>", update_custom_days_visibility)  # Bind event to update visibility

custom_days_frame = tk.Frame(clock)
# Place the frame at the desired position initially
custom_days_frame.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

custom_day_vars = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    day_var = tk.IntVar(value=0)
    custom_day_vars.append(day_var)
    chk = tk.Checkbutton(custom_days_frame, text=day, variable=day_var)
    chk.pack(side="left", padx=5)

setYourAlarm = tk.Label(clock,text = "Select Date",fg="black",relief = "solid",font=("TIMES NEW ROMAN",10,"bold"))
setYourAlarm.pack(pady=(10, 5))

calendar = Calendar(clock, selectmode="day", date_pattern="y-mm-dd")
calendar.pack(pady=20)

tk.Button(clock,text = "Set Alarm",fg="red",width = 10,command = set_alarm_time).pack(pady=5)
tk.Button(clock, text = "Exit Program", command=clock.quit).pack(pady=(5, 10))

time_label = tk.Label(clock, font=("TIMES NEW ROMAN", 20), fg="black", bg="white")
time_label.pack(pady=10)

alarm_time = None  # Initialize alarm time

# Start updating the clock
update_current_time()

clock.mainloop()
