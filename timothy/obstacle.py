import RPi.GPIO as GPIO
import time

ObstaclePin = 17
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def loop():
    variable = 0
    while True:
        variable += 1
        if 0 == GPIO.input(ObstaclePin):
            print(str(variable) + "Detected Barrier!", end='\r')
        else:
            print(str(variable) + "nobarrier      ", end='\r')
        time.sleep(.1)

def destroy():
    print('exit cleanup')
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    try:
        loop()
    except (KeyboardInterrupt):
        destroy()