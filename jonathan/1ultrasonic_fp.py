import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import RPi.GPIO as GPIO
import asyncio

from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
import time

loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
GPIO.setmode(GPIO.BCM)

trigger = 20
echo = 21


GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)



def distance():
    GPIO.output(trigger, True)

    time.sleep(0.00001)
    GPIO.output(trigger, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time

    distance = (time_elapsed * 34300) / 2
    return distance


async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)
    while True:
        dist=  distance()
        await asyncio.sleep(.05)
        print("Measurements are {0} cm".format(dist))
        if dist < 35:
            while dist < 35:
                await rvr.raw_motors(2,255,1,255)
                dist =  distance()
                await asyncio.sleep(.05)
                print('turning right')
            await rvr.reset_yaw()
            dist = distance()
        elif dist >= 35:
            await rvr.drive_with_heading(90,0,0)

try:
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )
except KeyboardInterrupt:
    print("Program ended by KeyboardInterrupt")
    GPIO.cleanup()