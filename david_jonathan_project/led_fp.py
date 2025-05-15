import RPi.GPIO as GPIO
import time

LED_PINS = {
    'green':  [5, 6],
    'yellow': [13, 19],
    'white':  [22, 27]
}

ALL_PINS = [pin for pins in LED_PINS.values() for pin in pins]

def flash_leds(led_pins=LED_PINS, sequence=None, delay=0.5):
    GPIO.setmode(GPIO.BCM)
    for pin in ALL_PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    if sequence is None:
        sequence = list(led_pins.keys())

    try:
        
        while True:
            for color in sequence:
                for p in ALL_PINS:
                    GPIO.output(p, GPIO.LOW)
                for p in led_pins[color]:
                    GPIO.output(p, GPIO.HIGH)
                time.sleep(delay)

    except KeyboardInterrupt:
        pass

    finally:
        for p in ALL_PINS:
            GPIO.output(p, GPIO.LOW)
        GPIO.cleanup()