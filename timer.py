import os
import time

hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")

try:
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    while seconds > 0 or minutes > 0 or hours > 0:
        if seconds == 0 and minutes > 0:
            seconds = 59
            minutes -= 1
        if minutes == 0 and hours > 0 and seconds == 0:
            minutes = 59
            hours -= 1
        seconds -= 1
        os.system('cls')
        print hours, ":", minutes, ":", seconds
        time.sleep(1)
except (TypeError, ValueError) as e:
    print "Not a number"
    pass