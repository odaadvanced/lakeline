import RPi.GPIO as GPIO
import time, asyncio
from sphero_sdk import SpheroRvrAsync, SerialAsyncDal  

# Ultrasonic pins
TRIG, ECHO = 23, 24

async def main():
    # Get the currently running loop
    loop = asyncio.get_event_loop()
    dal  = SerialAsyncDal(loop)        
    rvr  = SpheroRvrAsync(dal=dal)
 
    
    # Wake + reset
    await rvr.wake()
    await rvr.reset_yaw()
    
    # Ultrasonic setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    last_turn = 'left'
    await rvr.raw_motors(1, 50, 1, 50)  # start forward
    
    async def measure_distance():
        GPIO.output(TRIG, False)
        await asyncio.sleep(0.05)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        start = time.time()
        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            end = time.time()
        return (end - start) * 17150
    
    # main loop
    while True:
        dist = await measure_distance()
        if dist < 50:
            await rvr.raw_motors(0, 0, 0, 0)
            if last_turn == 'right':
                await rvr.raw_motors(2, 50, 1, 50); last_turn = 'left'
            else:
                await rvr.raw_motors(1, 50, 2, 50); last_turn = 'right'
            await asyncio.sleep(0.5)
            await rvr.raw_motors(0, 0, 0, 0)
            await rvr.raw_motors(1, 50, 1, 50)
        await asyncio.sleep(0.1)

if __name__ == '__main__':
    # Let asyncio.run create (and close) the loop
    try:
        asyncio.run(main())
    pass:
        GPIO.cleanup()