import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

buzzer_pin = 17

GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1000)
pwm.start(50)