import RPi.GPIO as GPIO
import time

ObstaclePin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
def loop():
    while True:
        if 0 == GPIO.input(ObstaclePin):
            print("Detected Barrier!", end='\r')
        else:
            print("no barrier        ", end='r')
            
        time.sleep(.1)
        
def destroy():
    print ('exit cleanup')
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    try:
        loop()
    except (KeyboardInterrupt):
        destroy()