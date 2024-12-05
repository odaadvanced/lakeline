from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.record_video('/home/pi/new_video.mp4', duration=5)
camera.stop_preview()

