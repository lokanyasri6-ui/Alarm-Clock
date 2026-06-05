from tkinter import *
from tkinter import messagebox
from datetime import datetime

def check_alarm():
    current_time = datetime.now().strftime("%H:%M")

    if current_time == alarm_time.get():
        messagebox.showinfo("Alarm", "Wake Up! Alarm Time Reached!")
    else:
        root.after(1000, check_alarm)

def start_alarm():
    check_alarm()

root = Tk()
root.title("Alarm Clock")
root.geometry("300x200")

Label(root, text="Set Alarm (HH:MM)").pack(pady=10)

alarm_time = StringVar()
Entry(root, textvariable=alarm_time).pack(pady=5)

Button(root, text="Start Alarm", command=start_alarm).pack(pady=10)

root.mainloop()
