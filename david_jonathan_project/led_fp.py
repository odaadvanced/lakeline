import RPi.GPIO as GPIO
import time

# mapping (BCM numbers)
LED_PINS = {
    'green':  [5, 6],
    'yellow': [13, 19],
    'white':  [22, 27]
}

# flatten once so we can clear *every* pin quickly
ALL_PINS = [pin for pins in LED_PINS.values() for pin in pins]

def flash_leds(led_pins=LED_PINS, sequence=None, delay=0.5):
    """
    Flash each color in `sequence` forever until you hit Ctrl+C.
    Before lighting any color, it turns *all* LEDs off.
    
    • led_pins: dict color → [BCM pins]  
    • sequence: list of colors (defaults to the dict keys order)  
    • delay: seconds each color stays on
    """
    # 1) Setup GPIO once
    GPIO.setmode(GPIO.BCM)
    for pin in ALL_PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    if sequence is None:
        sequence = list(led_pins.keys())

    try:
        # 2) Flash loop
        while True:
            for color in sequence:
                # turn *everything* off
                for p in ALL_PINS:
                    GPIO.output(p, GPIO.LOW)
                # then turn on *only* this color
                for p in led_pins[color]:
                    GPIO.output(p, GPIO.HIGH)
                time.sleep(delay)

    except KeyboardInterrupt:
        # stop on Ctrl+C
        pass

    finally:
        # 3) ensure all off, then cleanup
        for p in ALL_PINS:
            GPIO.output(p, GPIO.LOW)
        GPIO.cleanup()