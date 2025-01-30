from oled_io import Oled_io
from gpiozero import LED

red = LED(18)
yellow = LED(23)
green = LED(24)


display = Oled_io()

display.clear

red.off()
yellow.off()
green.off()