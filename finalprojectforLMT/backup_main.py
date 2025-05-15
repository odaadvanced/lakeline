import sys

import os

import camera

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from tts import TTS

tts = TTS(engine="espeak")
tts.lang("en-US")

import RPi.GPIO as GPIO

from oled_io import Oled_io

display = Oled_io()


from sphero_sdk import SerialAsyncDal

import time



GPIO.setmode(GPIO.BCM)


right_trigger = 6

right_echo = 5

left_trigger = 19

left_echo = 13

buzzer_pin = 17

GPIO.setup(left_trigger, GPIO.OUT)

GPIO.setup(left_echo, GPIO.IN)

GPIO.setup(right_trigger, GPIO.OUT)

GPIO.setup(right_echo, GPIO.IN)

GPIO.setup(buzzer_pin, GPIO.OUT)

pwm = GPIO.PWM(buzzer_pin, 1000)

def distance_left():

    GPIO.output(left_trigger, True)


    time.sleep(0.00001)

    GPIO.output(left_trigger, False)


    start_time = time.time()

    stop_time = time.time()


    while GPIO.input(left_echo) == 0:

        start_time = time.time()


    while GPIO.input(left_echo) == 1:

        stop_time = time.time()


    time_elapsed = stop_time - start_time


    distance = (time_elapsed * 34300) / 2

    return distance



def distance_right():

    GPIO.output(right_trigger, True)


    time.sleep(0.00001)

    GPIO.output(right_trigger, False)


    start_time = time.time()

    stop_time = time.time()


    while GPIO.input(right_echo) == 0:

        start_time = time.time()


    while GPIO.input(right_echo) == 1:

        stop_time = time.time()


    time_elapsed = stop_time - start_time


    distance = (time_elapsed * 34300) / 2

    return distance

def drive():

    rvr.wake()

    rvr.reset_yaw()

    time.sleep(.5)
    
        
    while True:
        

        dist_r =  distance_right()

        dist_l =  distance_left()
        
        time.sleep(.05)

        print('Measurements are {0} cm right and {1} cm left'.format(dist_r, dist_l))
        display.print(f"{dist_l:.2f}")
        if dist_r < 40:
            
            while dist_r < 40:
                pwm.start(40)
                display.print(f"{dist_l:.2f}")
                rvr.raw_motors(2,90,1,90)

                dist_r =  distance_right()

                time.sleep

                print('turning left')
                tts.say("Turning left.")
            rvr.reset_yaw()
            

        elif dist_l < 40:
            
            while dist_l < 40:
                display.print(f"{dist_l:.2f}")
                pwm.start(40)
                rvr.raw_motors(1,90,2,90)

                dist_l =   distance_left()

                time.sleep(.02)

                print('turning right')
                tts.say("Turning right.")
            rvr.reset_yaw()
            

        elif dist_l >= 50 and dist_r >= 50:
            pwm.stop()
        
            rvr.drive_with_heading(20,0,0)
            


def main():
    while True:
        start = time.time()
        while time.time() - start < 10:
            drive()
        collect.main()
        

try:
    while True:
        main()
except KeyboardInterrupt:

    print('Program ended by KeyboardInterrupt')

    GPIO.cleanup()