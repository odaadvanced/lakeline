import os
import sys
import RPi.GPIO as GPIO
import time
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask
from tts import TTS
tts = TTS(engine="espeak")
tts.lang("en-US")

rvr = SpheroRvrObserver()

ObstaclePin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
def main():
    while True:
        result = GPIO.input(ObstaclePin)
        if result == 0:
            print("Detected Barrier!", end='\r')
            tts.say("AA!")
            rvr.drive_with_heading(
                speed=200,
                heading=0,
                flags=DriveFlagsBitmask.drive_reverse.value
            )
            
        else:
            print("no barrier        ", end='\r')
            tts.say("no barrier")
            rvr.drive_with_heading(
                speed=200,
                heading=0,
                flags=DriveFlagsBitmask.none.value
            )
        time.sleep(.001)
        
def destroy():
    print ('exit cleanup      ')
    rvr.close()
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    try:
        main()
    except (KeyboardInterrupt):
        destroy()