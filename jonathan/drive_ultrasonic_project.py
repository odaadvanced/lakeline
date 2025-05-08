import time
import board
import adafruit_hcsr04
import sys
import os
from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
rvr.wake()
time.sleep(2)

def get_distance():
    try:
        return sonar.distance
    except (RuntimeError, OSError):
        time.sleep(0.05)
        return None
try:
    while True:
        dist = get_distance()
        if dist and dist > 20:
            rvr.drive_with_heading(50, 0, 0)
        else:
            rvr.drive_with_heading(0, 0, 0)
            time.sleep(0.5)
            # Rotate in place
            rvr.drive_tank_normalized(left_speed=-50, right_speed=50)  # Spin right
            time.sleep(1.0)  # How long to spin
            rvr.drive_with_heading(50, 0, 0)  # Then drive forward
        time.sleep(0.1)
except KeyboardInterrupt:
    rvr.close()
  