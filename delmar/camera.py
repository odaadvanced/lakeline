from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)  # Wait for the camera to adjust
camera.capture('/home/pi/Desktop/image1b.jpg')
camera.stop_preview()