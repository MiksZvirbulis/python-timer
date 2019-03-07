# Importing os to be able to clear the console
import os
# Importing time to use the sleep function to delay timer
import time

# Collecting time information for timer to run
hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")

try:
    # Trying to set input data to integer
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    # Loop while seconds, minutes and hours are more than 0
    while seconds > 0 or minutes > 0 or hours > 0:
        # Execute if seconds equal to 0 and minutes are more than 0
        if seconds == 0 and minutes > 0:
            # Set seconds to 59 as minutes are more than 0, yet seconds are 0
            seconds = 59
            # Decrement minutes by 1 as minutes are more than 0, yet seconds are 0
            minutes -= 1
            # Execute if minutes and seconds equal to 0 and hours are more than 0
        if minutes == 0 and hours > 0 and seconds == 0:
            # Set minutes and seconds to 59 as hours are more than 1 and minutes/seconds are both 0
            minutes = 59
            seconds = 59
            # Decrement hours by 1 as minutes and seconds are 0 and hours are more than 1
            hours -= 1
            # Decrement seconds by 1
        seconds -= 1
        # Clear console
        os.system('cls')
        # Print time left
        print hours, ":", minutes, ":", seconds
        # Pause for 1 second
        time.sleep(1)
        # Time not given as integer, handling error
except (TypeError, ValueError) as e:
    print "Not a number"
    pass