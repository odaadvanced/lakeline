import RPi.GPIO as GPIO
import time
from tts import TTS

ObstaclePin = 17

tts = TTS(engine="espeak")
tts.lang("en-US")

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if 0 == GPIO.input(ObstaclePin):
            print("Detected Barrier!", end='\r')
        else:
            print("No Barrier        ", end='\r')
        
        time.sleep(.1)
def main():
    tts.say()
    while True:
        pass

def destroy():
    print ('exit cleanup')
    GPIO.cleanup()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        destroy()    
    
if __name__ == "__main__":
    setup()
    try:
        loop()
    except(
        KeyboardInterrupt
    ):
        destroy()