import threading
import signal
import sys

from photoresistor_fp import GUI_photoresistor    # your Tkinter + LDR code
from led_fp import flash_leds   # your LED‐blinking function

def shutdown(signum, frame):
    """Signal handler for Ctrl+C → force exit."""
    print("\nCaught SIGINT, exiting…")
    # If your GUI is still open, this will raise KeyboardInterrupt in the main thread
    sys.exit(0)

if __name__ == "__main__":
    # 1) Install the SIGINT handler
    signal.signal(signal.SIGINT, shutdown)

    # 2) Start LEDs in a daemon thread so they don't block shutdown
    t_led = threading.Thread(target=flash_leds, daemon=True)
    t_led.start()

    # 3) Run your GUI (blocks until window closes or SIGINT)
    try:
        GUI_photoresistor
    except SystemExit:
        # shutdown() calls sys.exit(0), which raises SystemExit here
        pass