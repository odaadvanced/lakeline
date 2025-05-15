import time
import color_detection
import picamera



camera = picamera.PiCamera()


def picture(directory):
    '''The picture(directory) function takes a picture using the camera and saves it to the 'directory' directory.'''
    camera.start_preview()
    time.sleep(1)
    camera.capture(directory)
    camera.stop_preview()

def main():
    """This function takes a picture in front of the rover and logs the color of the ground underneath the rover and saves it to a text file."""
    picture(f'/home/pi/dev/lakeline/finalprojectforLMT/data/{time.time():.0f}.jpg')
    color_detection.main()
    
main()