import threading
import time
import sys

from drive_with_sensor import drive
from led_fp import flash_leds
from photoresistor_fp import GUI_photoresistor 
from fan_fp import run_fan
from oled_distance_fp import OLED_display

# Each tuple is (callable, args_tuple)
TASKS = [
    (drive, ()),           
    (flash_leds, ()),
    (OLED_display, ()),
    (GUI_photoresistor, ()),            
    (run_fan, (16,)),         
]

def main():
    # Create and start all threads as daemons
    threads = []
    for func, args in TASKS:
        t = threading.Thread(target=func, args=args, daemon=True)
        t.start()
        threads.append(t)

    # Keep the main thread alive until Ctrl+C
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping all tasks…")
        sys.exit(0)
if __name__ == "__main__":
    main()