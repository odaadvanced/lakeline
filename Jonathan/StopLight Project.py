import time
import board
import busio
import digitalio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(128, 64, i2c)

red_led = digitalio.DigitalInOut(board.D18)
red_led.direction = digitalio.Direction.OUTPUT

green_led = digitalio.DigitalInOut(board.D23)
green_led.direction = digitalio.Direction.OUTPUT

yellow_led = digitalio.DigitalInOut(board.D24)
yellow_led.direction = digitalio.Direction.OUTPUT

buzzer = digitalio.DigitalInOut(board.D25)
buzzer.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D17)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

def update_display(text):
    draw.rectangle((0, 0, oled.width, oled.height), fill=0)
    draw.text((10, 20), text, font=font, fill=255)
    oled.image(image)
    oled.show()

try:
    while True:
        red_led.value = True
        green_led.value = False
        yellow_led.value = False
        update_display("DO NOT CROSS")

        while not button.value:
            time.sleep(0.1)

        for seconds in range(15, 0, -1):
            update_display(f"Countdown: {seconds}")
            buzzer.value = True
            time.sleep(0.2)
            buzzer.value = False
            time.sleep(0.8)

        red_led.value = False
        green_led.value = False
        update_display("MAY CROSS")

        for seconds in range(15, 0, -1):
            update_display(f"Countdown: {seconds}")
            time.sleep(1)

        green_led.value = False
        yellow_led.value = True
        update_display("DO NOT CROSS")
        time.sleep(3)

        yellow_led.value = False
        red_led.value = True
        update_display("DO NOT CROSS")

except KeyboardInterrupt:
    red_led.value = False
    green_led.value = False
    yellow_led.value = False
    buzzer.value = False
    update_display("")