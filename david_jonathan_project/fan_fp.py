import RPi.GPIO as GPIO
import time

pin = 16

def run_fan():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    on_time = 5
    off_time = 10
    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)   
            time.sleep(on_time)
            GPIO.output(pin, GPIO.LOW)   
            time.sleep(off_time)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup(pin)
     
if __name__ == "__main__":
    run_fan()

