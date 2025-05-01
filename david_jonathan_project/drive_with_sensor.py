import RPi.GPIO as GPIO
import time
import os
import sys
import ultrasonic as ult
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask


rvr = SpheroRvrObserver()
ult.setup()

rvr.wake()
time.sleep(2)
rvr.reset_yaw()

def drive():
    while True:
        if ult.distance() <= 30:
            print("Detected Barrier!", end='\r')
            break
        else:
            print("No Barrier         ", end ='\r')
            rvr.drive_with_heading(
                speed=60,
                heading=0,
                flags=DriveFlagsBitmask.none.value
                ) 
                
        time.sleep(.1)
    
drive()
    