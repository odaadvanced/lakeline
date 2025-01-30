# 09_01_blink.py

import gpiozero, time

ledgreen = gpiozero.LED(18)
ledyellow = gpiozero.LED(23)
ledred = gpiozero.LED(24)
switch = gpiozero.Button(25, pull_up=True)
while True:
    if switch.is_pressed:
        ledred.on()
        time.sleep(5.5)
        ledred.off()
        time.sleep(0.5)
        
        print('hello')
        
        ledgreen.on()
        time.sleep(2.0)
        ledgreen.off()
        time.sleep(0.5)
                
        ledyellow.on()
        time.sleep(2.0)
        ledyellow.off()
        time.sleep(0.5)
    else:
        ledred.on()
