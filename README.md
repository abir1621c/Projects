⏰ Tkinter Alarm Clock

A beautiful Python-based Alarm Clock built using Tkinter, with support for custom date, repeat options, and audio alerts. This project demonstrates the use of GUI development, multi-threading, and date-time handling in Python — perfect for beginners and intermediate developers!

📸 Preview
![Screenshot 2025-05-22 115659](https://github.com/user-attachments/assets/1173249e-5346-4c53-b792-8a6b43650e0d)


✨ Features
🕓 Set Exact Time: Configure hour, minute, and second using dropdowns.

📆 Select Date: Pick a specific calendar date for the alarm.

🔁 Repeat Options:

None – One-time alarm.

Daily – Repeats every day.

Mon to Fri – Weekday alarms only.

Custom – Choose specific days like only Sat-Sun or Tue-Thu.

🎵 Custom Sound Alert: Plays a loud alarm sound (.mp3).

📅 Calendar Integration: Tkcalendar widget for date selection.

🧠 Multithreading: Alarm runs on a separate thread to keep UI responsive.

🕒 Live Time Display: Current date and time shown at the bottom.

🚀 How to Run
✅ Prerequisites
Make sure you have these libraries installed:

bash
Copy
Edit
pip install tkcalendar pygame pillow
▶️ Run the App
bash
Copy
Edit
python alarm_clock.py
Make sure to update the alarm sound path in the code:

python
Copy
Edit
filename = "C:\\Users\\HP\\CODING\\Python_Coding\\real_loud_alarm.mp3"
🛠️ Folder Structure
bash
Copy
Edit
alarm_clock/
│
├── alarm_clock.py         # Main source file
├── alarm.jpg              # Clock logo image
├── README.md              # Project documentation
📌 Notes
Alarm only works if the time matches the current system time exactly.

Alarm sound will not repeat unless you implement a loop or reset mechanism.

You need to keep the application running for alarms to trigger.

🔮 Future Enhancements
Suggestions for improvements to be added in future versions:

🔊 Volume control slider in UI.

📳 Vibration pattern simulation (for mobile version).

🔄 Snooze option with intervals.

📩 Email or popup notifications.

🌓 Dark mode / Light mode toggle.

🧠 AI Wake Suggestions based on sleep cycles.

📱 Mobile version with Kivy or Flutter.

🧑‍💻 Author
Abir Soren
🎓 B.Tech in Computer Science & Engineering NIT DURGAPUR '27
🛠️ Tech Enthusiast | 🧠 AI/ML Explorer | 💡 Builder
