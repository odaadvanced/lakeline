import gpiozero
from time import sleep

green_led = gpiozero.LED(18)
yellow_led = gpiozero.LED(23)
red_led = gpiozero.LED(24)
button = gpiozero.Button(17)

red_led.on()

def button_pressed():
    print("Button is pressed")
    sleep(15)
    red_led.off()
    green_led.on()
    
button.when_pressed = button_pressed
