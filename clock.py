import datetime
import time
import os

def alarm(set_time):
    while True:
        # Get current system time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time, end="\r")  

        # Check if time matches
        if current_time == set_time:
            print("\nWake up! Alarm ringing 🔔")
            try:
                # For Windows - plays system beep sound
                duration = 1000  # milliseconds
                freq = 440  # Hz
                os.system('play -nq -t alsa synth {} sine {}'.format(duration/1000, freq))  
            except:
                print("Beep! Beep! Beep!")  # fallback
            break
        time.sleep(1)

# Example: Set alarm time
set_time = input("Enter alarm time in HH:MM:SS format: ")
alarm(set_time)
