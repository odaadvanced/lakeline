import picamera
from time import sleep

camera = picamera.PiCamera()

def picture(directory):
    camera.start_preview()
    sleep(5)
    camera.capture(directory)
    camera.stop_preview()
    
picture('/dev/lakeline/finalprojectforLMT/')