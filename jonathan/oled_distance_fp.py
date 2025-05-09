import RPi.GPIO as GPIO
import time
import csv
import board
import busio
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

def OLED_display():
    """
    Continuously read an HC-SR04 ultrasonic sensor,
    display the distance on a 128×64 SSD1306 OLED,
    and log timestamped readings to oled_distance.csv.
    Press Ctrl+C to stop.
    """
    # — CSV setup —
    log_file = open('oled_distance.csv', 'a', newline='')
    writer = csv.writer(log_file)
    if log_file.tell() == 0:
        writer.writerow(['timestamp', 'distance_cm'])

    # — GPIO setup for HC-SR04 —
    GPIO.setmode(GPIO.BCM)
    TRIG = 20
    ECHO = 21
    GPIO.setup(TRIG, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ECHO, GPIO.IN)

    # — OLED setup (I²C) —
    i2c      = busio.I2C(board.SCL, board.SDA)
    reset_pin= digitalio.DigitalInOut(board.D4)  # change if wired elsewhere
    disp     = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, reset=reset_pin)
    disp.fill(0)
    disp.show()

    width, height = disp.width, disp.height
    image  = Image.new('1', (width, height))
    draw   = ImageDraw.Draw(image)
    font   = ImageFont.load_default()

    try:
        while True:
            # — Trigger ultrasonic pulse —
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            # — Measure echo —
            start = time.time()
            while GPIO.input(ECHO) == 0:
                start = time.time()
            while GPIO.input(ECHO) == 1:
                stop = time.time()

            # — Compute distance (cm) —
            dist_cm = (stop - start) * 34300 / 2

            # — Display on OLED —
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((0, 0), "Distance:", font=font, fill=255)
            draw.text((0, 16), f"{dist_cm:.1f} cm", font=font, fill=255)
            disp.image(image)
            disp.show()

            # — Log to CSV —
            ts = time.strftime("%Y-%m-%dT%H:%M:%S")
            writer.writerow([ts, f"{dist_cm:.1f}"])
            log_file.flush()

            time.sleep(0.5)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        disp.fill(0)
        disp.show()
        log_file.close()