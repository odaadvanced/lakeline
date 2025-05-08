import RPi.GPIO as GPIO
import time
import ultrasonic as ult
import drive_with_sensor as drive
from sphero_sdk import SpheroRvrObserver


rvr = SpheroRvrObserver()

ult.setup()
rvr.wake()
time.sleep(2)
rvr.reset_yaw()

def main():
    while True:
        drive.drive()
        time.sleep(5)

def destroy():
    rvr.close()
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        main()
        destroy()
    except KeyboardInterrupt:
        destroy()