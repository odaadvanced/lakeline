# 09_01_blink.py

import gpiozero, time

ledgreen = gpiozero.LED(18)
ledyellow = gpiozero.LED(23)
ledred = gpiozero.LED(24)
while True:
    if switch.is_pressed:
        print("Button Pressed")
        time.sleep(0.2)ledred.on()
        time.sleep(2.0)
        ledred.off()
        time.sleep(0.5)
            while True:
                ledgreen.on()
                time.sleep(2.0)
                ledgreen.off()
                time.sleep(0.5)
                
                ledyellow.on()
                time.sleep(2.0)
                ledyellow.off()
                time.sleep(0.5)
    
