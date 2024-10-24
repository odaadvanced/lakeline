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

        drive_map = [[60,0,0.2],[120,0.2,0.4],[180,0.4,0.4],
                     [240,0.6,0.2],[300,0.4,0.0],[0,0.2,0]]
    
        for side in range(0, 6):

            rvr.drive_with_heading(
                speed=20,  # Valid speed values are 0-255
                heading=0,  # Valid heading values are 0-359
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
