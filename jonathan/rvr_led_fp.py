import asyncio
import time
from sphero_sdk import SpheroRvrAsync, SerialAsyncDal, Colors

async def main_LED():
    
    loop = asyncio.get_event_loop()
    rvr = SpheroRvrAsync(dal=SerialAsyncDal(loop))
    
    
    await rvr.wake()
    await asyncio.sleep(2)
    
    
    
    cycle = [
        Colors.red,
        Colors.green,
        Colors.blue,
        Colors.yellow,
        Colors.cyan,
        Colors.magenta,
        Colors.white,
        Colors.off     # turns LEDs off briefly
    ]
    
    
    try:
        while True:
            for color in cycle:
                await rvr.led_control.set_all_leds_color(color=color)   # named colors :contentReference[oaicite:0]{index=0}
                # Or you could use RGB:
                # await rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)  # pure red :contentReference[oaicite:1]{index=1}
                await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        
        await rvr.led_control.turn_leds_off()
        await rvr.close()

if __name__ == "__main_LED__":
    asyncio.run(main_LED())