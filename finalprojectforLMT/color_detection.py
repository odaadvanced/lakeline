import os
import sys
import time
import pathlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import guizero
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices


rvr = SpheroRvrObserver()


def color_detected_handler(color_detected_data):
    '''This function takes the color data from the sensor and prints it to the shell and adds it to a text file'''
    print('Color detection data response: ', color_detected_data)
    path = pathlib.Path('/home/pi/dev/lakeline/finalprojectforLMT/data/collection.txt')
    file = path.open(mode='a', encoding='utf-8')
    with file as file:
        file.write(f'{color_detected_data} at {time.time()}\n')
    app = guizero.App(title="Color Data")
    message = guizero.Text(app, text=f"{color_detected_data}")
    app.display()
    

def main():
    """ This program demonstrates how to use the color sensor on RVR (located on the down side of RVR, facing the floor)
        to report colors detected.
    """

    
    rvr.wake()

    # Give RVR time to wake up
    time.sleep(2)

    rvr.enable_color_detection(is_enabled=True)
    rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.color_detection,
        handler=color_detected_handler
    )
    rvr.sensor_control.start(interval=250)
    time.sleep(0.3)
    rvr.sensor_control.clear()
    time.sleep(.5)
    


