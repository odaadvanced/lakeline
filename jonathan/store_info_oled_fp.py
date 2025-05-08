import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import RPi.GPIO as GPIO
import asyncio
import time
import csv
from datetime import datetime

from sphero_sdk import SpheroRvrAsync, SerialAsyncDal

import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# ─── SET UP LOG FILE ───────────────────────────────────────────────────────────
log_file = open('distance_log.csv', 'a', newline='')
csv_writer = csv.writer(log_file)
# Write header if file is new (size == 0)
if os.stat('distance_log.csv').st_size == 0:
    csv_writer.writerow(['timestamp', 'distance_cm'])

# ─── OLED SETUP ───────────────────────────────────────────────────────────────
i2c = busio.I2C(board.SCL, board.SDA)
reset_pin = digitalio.DigitalInOut(board.D4)  # change pin if needed
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, reset=reset_pin)
disp.fill(0)
disp.show()

width, height = disp.width, disp.height
image = Image.new("1", (width, height))
draw  = ImageDraw.Draw(image)

# Load larger fonts if available
try:
    font_label = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14
    )
    font_value = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26
    )
except OSError:
    font_label = ImageFont.load_default()
    font_value = ImageFont.load_default()

def display_distance(dist):
    """Draws a big distance readout on the OLED."""
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "Distance:", font=font_label, fill=255)
    txt = f"{dist:.1f} cm"
    w, h = draw.textsize(txt, font=font_value)
    x = (width - w) // 2
    y = 16
    draw.text((x, y), txt, font=font_value, fill=255)
    disp.image(image)
    disp.show()

# ─── SPHERO RVR & ULTRASONIC SETUP ───────────────────────────────────────────
loop = asyncio.get_event_loop()
rvr  = SpheroRvrAsync(dal=SerialAsyncDal(loop))

GPIO.setmode(GPIO.BCM)
TRIG = 20
ECHO = 21

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def distance():
    """Trigger pulse, measure echo, return cm."""
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    return ( (stop - start) * 34300 ) / 2

# ─── MAIN ASYNC LOOP ───────────────────────────────────────────────────────────
async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(2)

    while True:
        dist = distance()
        await asyncio.sleep(0.05)

        # 1) Print & display
        print(f"{datetime.now().isoformat()} → {dist:.1f} cm")
        display_distance(dist)

        # 2) Log to CSV
        csv_writer.writerow([datetime.now().isoformat(), f"{dist:.1f}"])
        log_file.flush()

        # 3) Your driving logic
        if dist <= 35:
            while dist < 35:
                await rvr.raw_motors(2, 255, 1, 255)
                dist = distance()
                await asyncio.sleep(0.05)
                ts = datetime.now().isoformat()
                print(f"{ts} turning right --> {dist:.1f} cm")
                display_distance(dist)
                csv_writer.writerow([ts, f"{dist:.1f}"])
                log_file.flush()
            await rvr.reset_yaw()
            dist = distance()
            display_distance(dist)
            csv_writer.writerow([datetime.now().isoformat(), f"{dist:.1f}"])
            log_file.flush()
        elif dist > 35:
            await rvr.drive_with_heading(128, 0, 0)

# ─── RUN & CLEANUP ─────────────────────────────────────────────────────────────
try:
    loop.run_until_complete(asyncio.gather(main()))
except KeyboardInterrupt:
    print("Program ended by user")
finally:
    GPIO.cleanup()
    disp.fill(0); disp.show()
    log_file.close()