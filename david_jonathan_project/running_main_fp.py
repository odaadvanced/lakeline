import threading
import time
import sys

import RPi.GPIO as GPIO

from drive_with_sensor import drive
from led_fp import flash_leds
from photoresistor_fp import GUI_photoresistor 
from fan_fp import run_fan
from oled_distance_fp import OLED_display
from camera import take_photo

TASKS = [
    (drive, ()),           
    (flash_leds, ()),
    (OLED_display, ()),
    (GUI_photoresistor, ()),            
    (run_fan, ()),
    (take_photo, ())
]

def main():
    threads = []
    for func, args in TASKS:
        t = threading.Thread(target=func, args=args, daemon=True)
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping all tasks…")
        time.sleep(2)
        GPIO.cleanup()
        sys.exit(0)
if __name__ == "__main__":
    main()