import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\n⏰ Wake up! Alarm Time Reached!")
        break

    time.sleep(1)
