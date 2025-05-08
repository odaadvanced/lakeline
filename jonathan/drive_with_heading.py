import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import DriveFlagsBitmask


rvr = SpheroRvrObserver()


def main():
    """ This program has RVR drive around in different directions using the function drive_with_heading.
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.reset_yaw()

        rvr.drive_with_heading(
            speed=50,  # Valid speed values are 0-255
            heading=45,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_heading(
            speed=50,  # Valid speed values are 0-255
            heading=300,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_heading(
            speed=50,  # Valid speed values are 0-255
            heading=270,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )

        # Delay to allow RVR to drive
        time.sleep(1)

        rvr.drive_with_heading(
            speed=50,  # Valid speed values are 0-255
            heading=200,  # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )

        # Delay to allow RVR to drive
        time.sleep(1)
        
        rvr.drive_with_heading(
            speed=50, #Valid speed values are 0-255
            heading=160, # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )
        
        # Delay to allow RVR to drive
        time.sleep(1)
        
        rvr.drive_with_heading(
            speed=50, #Valid speed values are 0-255
            heading=180, # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )
        
        # Delay to allow RVR to drive
        time.sleep(1)
        
        rvr.drive_with_heading(
            speed=50, #Valid speed values are 0-255
            heading=90, # Valid heading values are 0-359
            flags=DriveFlagsBitmask.none.value
        )
        
        # Delay to allow RVR to drive
        time.sleep(1)
        
    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()
