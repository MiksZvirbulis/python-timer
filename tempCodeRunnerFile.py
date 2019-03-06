import os
import time

seconds = int(0)
minutes = int(0)
hours = int(0)

timer = raw_input("Enter length of timer in seconds: ")

try:
    timer = int(timer)
except TypeError:
    print "Not a number"

while timer > 0:
    os.system('cls')
    seconds += .1
    print seconds, " seconds left"
    time.sleep(.1)