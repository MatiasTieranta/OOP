import time

import threading


class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW!")
                    os.popen("alarm.mp3")
                    return
            time.sleep(60)
        except:
            return

    def just_die(self):
        self.keep_running = False


alarm_Hour = input("Enter the hour you want to wake up at: ")
alarm_Minutes = input("Enter the minute you want to wake up at: ")

print("You want to wake up at:", alarm_Hour, alarm_Minutes)

alarm = Alarm(alarm_Hour, alarm_Minutes)
alarm.start()

try:
    while True:
        text = str(input())
        if text == "stop":
            alarm.just_die()
            break
except:
    print("Yikes lets get out of here")
    alarm.just_die()
