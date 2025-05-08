import RPi.GPIO as GPIO
import time
import ultrasonic as ult
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask


rvr = SpheroRvrObserver()

def drive():
    rvr.reset_yaw()
    while True:
        time.sleep(.3)
        if ult.distance() <= 20:
            rvr.drive_with_heading(
                speed=0,
                heading=90,
                flags=DriveFlagsBitmask.drive_reverse.value
                )
            break
        else:
            rvr.drive_with_heading(
                speed=40,
                heading=0,
                flags=DriveFlagsBitmask.none.value
                )
        
def destroy():
    rvr.close()
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        ult.setup()
        rvr.wake()
        time.sleep(1)
        drive()
        destroy()
    except KeyboardInterrupt:
        destroy()
    
    