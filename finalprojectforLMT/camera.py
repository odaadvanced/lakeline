import picamera
from time import sleep

camera = picamera.PiCamera()

def picture(directory):
    '''The picture(directory) function takes a picture using the camera and saves it to the 'directory' directory.'''
    camera.start_preview()
    sleep(1)
    camera.capture(directory)
    camera.stop_preview()
    
picture('/dev/lakeline/finalprojectforLMT/')