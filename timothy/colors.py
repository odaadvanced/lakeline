import os
import sys
import time
from time import sleep
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

rvr = SpheroRvrObserver()

def main():
    """This program demonstrates how to set all the LEDs of RVR using the LEDs"""
    try:
        rvr.wake()
        sleep(2)
        rvr.led_control.turn_leds_off()
        sleep(1)
        rvr.led_control.set_all_leds_color(color=Colors.yellow)
        sleep(2)
        rvr.led_control.turn_leds_off()
        sleep(1)
        rvr.led_control.set_all_leds_rgb(red=255,green=0,blue=0)
        sleep(2)
        rvr.led_control.turn_leds_off()
        sleep(1)
    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')       
    finally:
        rvr.close()
    
if __name__ == '__main__':
        main()