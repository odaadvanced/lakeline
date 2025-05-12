import RPi.GPIO as GPIO
import time
import ultrasonic as ult
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask, Colors


rvr = SpheroRvrObserver()

def drive():
    ult.setup()
    rvr.wake()
    time.sleep(1)
    while True:
        while True:
                rvr.reset_yaw()
                if ult.distance() <= 20:
                    rvr.led_control.set_all_leds_color(color=Colors.red)
                    rvr.drive_with_heading(
                        speed=0,
                        heading=90,
                        flags=DriveFlagsBitmask.drive_reverse.value
                        )
                    time.sleep(5)
                    break
                else:
                    rvr.drive_with_heading(
                        speed=40,
                        heading=0,
                        flags=DriveFlagsBitmask.none.value
                        )
                    time.sleep(1)
                    rvr.led_control.set_all_leds_color(color=Colors.blue) 
            
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
    
    