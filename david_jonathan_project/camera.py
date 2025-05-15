
from picamera import PiCamera
import os
import time
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')

camera = PiCamera()

def setup():
    camera.start_preview(alpha=200)

def take_photo():
    while True:
        camera.capture(f'/home/pi/dev/lakeline/david_jonathan_project/images/my_photo{time.localtime()}.jpg')
        time.sleep(10)
        

def destroy():
    camera.stop_preview()

if __name__ == '__main__':
    setup()
    try:
        take_photo()
    except KeyboardInterrupt:
        destroy()