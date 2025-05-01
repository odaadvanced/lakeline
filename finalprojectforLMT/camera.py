import PiCamera from picamera as cam
from time import sleep

camera = cam()

def picture(directory):
    camera.start_preview()
    sleep(5)
    camera.capture(directory)
    camera.stop_preview()