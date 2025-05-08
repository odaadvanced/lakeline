# Main Program
import threading
from photoresistor_fp  import GUI_photoresistor
from led_fp import flash_leds

if __name__ == "__main__":
    # Thread for your GUI – note Tkinter MUST run in the main thread on some platforms,
    # so if your GUI misbehaves, swap ordering or run the other task in a Thread instead.
    t_flash_leds = threading.Thread(target=flash_leds, daemon=True)
    t_flash_leds.start()

    # Run the GUI in the main thread
    GUI_photoresistor()

from fan_fp import run_fan

if __name__ == "__main__":
    run_fan(pin=16)  