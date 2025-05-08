import picamera
import time

camera = picamera.PiCamera()

def picture(directory):
    '''The picture(directory) function takes a picture using the camera and saves it to the 'directory' directory.'''
    camera.start_preview()
    time.sleep(1)
    camera.capture(directory)
    camera.stop_preview()
    
