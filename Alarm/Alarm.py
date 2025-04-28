import datetime
import time
from playsound import playsound

ALARM_SOUND = "alarmSound.wav"  # Make sure alarm.mp3 is in the same folder

def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")
    try:
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))
    except ValueError:
        print("Invalid format. Please use HH:MM:SS format.")
        return

    print(f"Alarm set for {alarm_time}...")

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("Wake up!")
            playsound(ALARM_SOUND)
            break

        time.sleep(1)

if __name__ == "__main__":
    set_alarm()
