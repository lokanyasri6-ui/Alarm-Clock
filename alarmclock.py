from tkinter import*
from tkinter import messagebox
import datetime
def chech_alarm():
  current_time=datetime.date_time.now().strftime("%H:%M")
  if current_time==alarm_time.get():messageobx.showinfo("Alarm","Wake Up!")
  root.after(1000, check_alarm)
root=Tk()
root.title("Alarm Clock")
root.geometry("300x200")
Label(root, text="Set Alarm (HH:MM)").pack(pady=10)
alarm_time = StringVar()
Entry(root,textvariable=alarm_time).pack()
Button(root,text="Start Alarm",command=check_alarm.pack(pady=10)
root.mainloop()
