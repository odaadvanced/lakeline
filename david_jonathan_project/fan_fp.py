import RPi.GPIO as GPIO
import time

def run_fan(pin, on_time=5, off_time=10):
    """
    Continuously cycle a DC fan on and off.

    • pin      – BCM GPIO pin driving your motor transistor base  
    • on_time  – seconds to keep it ON (default 5)  
    • off_time – seconds to keep it OFF (default 10)

    Stops cleanly on Ctrl+C.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    try:
        while True:
            GPIO.output(pin, GPIO.HIGH)   # fan ON
            time.sleep(on_time)
            GPIO.output(pin, GPIO.LOW)    # fan OFF
            time.sleep(off_time)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup(pin)
