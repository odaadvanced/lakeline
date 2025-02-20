import RPi.GPIO as GPIO
import time
import os
import sys
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from tts import TTS
tts = TTS(engine="espeak")
tts.lang("en-US")

rvr = SpheroRvrObserver()

ObstaclePin = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    result = GPIO.input(ObstaclePin)
    while True:
        if result == 0:
            print("Detected Barrier!", end='\r')
            tts.say("Barrier Detected")
            rvr.drive_with_heading(
                speed=20,
                heading=0,
                flags=DriveFlagsBitmask.drive_reverse.value
            )
        else:
            print("No Barrier        ", end='\r')
            tts.say("AA!")
            rvr.drive_with_heading(
                speed=20,
                heading=0,
                flags=DriveFlagsBitmask.drive_reverse.value
            )
        time.sleep(.1)

def destroy():
    print ('exit cleanup')
    rvr.close()
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    try:
        main()
    except(
        KeyboardInterrupt
    ):
        destroy()
