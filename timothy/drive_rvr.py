import os
import sys
import time
from time import sleep
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask

rvr = SpheroRvrObserver()

def main():
    """ This program has RVR drive around in different directions using the function drive_with_heading."""
    try:
        rvr.wake()
        #give RVR time to wake up
        sleep(2)
        rvr.reset_yaw()
        rvr.drive_with_heading(
            speed=16, #valid speed values are 0-255
            heading=0, #valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )
        sleep(2)
        rvr.drive_with_heading(
            speed=16, #valid speed values are 0-255
            heading=90, #valid heading values are 0-359
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        sleep(2)
        rvr.drive_with_heading(
            speed=16, #valid speed values are 0-255
            heading=180, #valid heading values are 0-359
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        sleep(2)
        rvr.drive_with_heading(
            speed=16, #valid speed values are 0-255
            heading=270, #valid heading values are 0-359
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        sleep(2)
        rvr.drive_with_heading(
            speed=16, #valid speed values are 0-255
            heading=0, #valid heading values are 0-359
            flags=DriveFlagsBitmask.drive_reverse.value
        )
        sleep(2)
    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')       
    finally:
        rvr.close()
if __name__ == '__main__':
        main()