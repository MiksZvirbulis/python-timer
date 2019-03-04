import os
import time

seconds = int(0)
minutes = int(0)
hours = int(0)

run = raw_input("Enter R to run the program: ")

while run.lower() == "r":
    if seconds >= 60:
        seconds = 0
        minutes += 1
    if minutes > 59:
        minutes = 0
        hours += 1
    os.system('cls')
    seconds += .1
    print hours, ":", minutes, ":", seconds
    time.sleep(.1)