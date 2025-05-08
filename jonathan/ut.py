import time
import board
import adafruit_hcsr04

# Setup ultrasonic

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        distance = sonar.distance
        print(f"Distance: {distance:.2f} cm")
    except Exception as e:
        print(f"Sensor error: {e}")
    time.sleep(0.1)