import board
import busio
import digitalio
import threading
import time
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

class OLEDDisplay:
    def __init__(self, width=128, height=64, reset_pin_gpio=4):
        # Initialize I²C bus and reset pin
        self.i2c = busio.I2C(board.SCL, board.SDA)
        reset_pin = digitalio.DigitalInOut(getattr(board, f"D{reset_pin_gpio}"))
        
        # Create SSD1306 OLED class instance
        self.disp = adafruit_ssd1306.SSD1306_I2C(
            width, height, self.i2c, reset=reset_pin
        )
        
        # Clear display
        self.disp.fill(0)
        self.disp.show()
        
        # Prepare drawing canvas
        self.width  = width
        self.height = height
        self.image  = Image.new("1", (self.width, self.height))
        self.draw   = ImageDraw.Draw(self.image)
        self.font   = ImageFont.load_default()
        
        # Placeholder for your callback and thread
        self._callback = None
        self._interval = 1.0
        self._thread   = None

    def _update_loop(self):
        """Background thread: fetch text, redraw, and sleep."""
        while True:
            text = self._callback()                     # get fresh text
            # clear frame
            self.draw.rectangle((0, 0, self.width, self.height),
                                outline=0, fill=0)
            # draw new text
            self.draw.text((0, 0), text, font=self.font, fill=255)
            # send to display
            self.disp.image(self.image)
            self.disp.show()
            time.sleep(self._interval)

    def start(self, info_callback, interval=1.0):
        """
        Begin automatic updates.
        
        • info_callback: function returning the string to display  
        • interval: seconds between refreshes
        """
        self._callback = info_callback
        self._interval = interval
        self._thread   = threading.Thread(
            target=self._update_loop, daemon=True
        )
        self._thread.start()

# ──────────────────────────────────────────────────────────────────────────────
# Example usage below:

def get_dynamic_info():
    # Replace this with your own logic (sensor read, timestamp, variable, etc.)
    return time.strftime("Now: %H:%M:%S")

if __name__ == "__main__":
    # 1) Create the display (reset pin wired to GPIO4 by default)
    oled = OLEDDisplay(width=128, height=64, reset_pin_gpio=4)
    
    # 2) Start auto‐refresh: call get_dynamic_info() every 0.5s
    oled.start(get_dynamic_info, interval=0.5)
    
    # 3) Your main program can run forever without touching the OLED again
    try:
        while True:
            # ... other work ...
            time.sleep(1)
    except KeyboardInterrupt:
        pass