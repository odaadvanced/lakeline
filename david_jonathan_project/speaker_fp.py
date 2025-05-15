import RPi.GPIO as GPIO
import time

def beep_speaker(duration=1):
    pin = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 1000)
    pwm.start(50)
    time.sleep(duration)
    pwm.stop()
    GPIO.cleanup(pin)