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

def flash_LEDs(stop_event, led_pins=LED_PINS, sequence=None, delay=0.5):
    """
    Continuously flash each color in `sequence` until `stop_event` is set,
    then turn *all* LEDs off and clean up.

    • stop_event: threading.Event instance; when .is_set() becomes True, the loop exits  
    • led_pins: dict color → [BCM pins]  
    • sequence: list of colors (defaults to the dict keys order)  
    • delay: seconds each color stays on
    """
    # 1) Setup GPIO once
    GPIO.setmode(GPIO.BCM)
    for pin in ALL_PINS:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    if sequence is None:
        sequence = list(led_pins.keys())

    try:
        # 2) Flash loop
        while not stop_event.is_set():
            for color in sequence:
                if stop_event.is_set():
                    break
                # turn *everything* off
                for p in ALL_PINS:
                    GPIO.output(p, GPIO.LOW)
                # then turn on *only* this color
                for p in led_pins[color]:
                    GPIO.output(p, GPIO.HIGH)
                # wait, but wake early if stopped
                end_time = time.time() + delay
                while time.time() < end_time:
                    if stop_event.is_set():
                        break
                    time.sleep(0.05)

    finally:
        # 3) ensure all off, then cleanup
        for p in ALL_PINS:
            GPIO.output(p, GPIO.LOW)
        GPIO.cleanup()