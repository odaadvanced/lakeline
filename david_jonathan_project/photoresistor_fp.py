import spidev
import time
import csv
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def GUI_photoresistor():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 500_000

    
    log_file = open('brightness_log.csv', 'a', newline='')
    csv_writer = csv.writer(log_file)
    if log_file.tell() == 0:
        csv_writer.writerow(['timestamp', 'brightness_pct'])

    root = tk.Tk()
    root.title("Photoresistor Brightness")
    root.geometry("300x120")
    root.resizable(False, False)

    percent_var = tk.StringVar(value="-- %")
    ttk.Label(root, text="Brightness:").pack(pady=(10, 0))
    ttk.Label(root, textvariable=percent_var, font=("TkDefaultFont", 16)).pack()

    pb = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate")
    pb.pack(pady=(5, 10))
    

    def update_reading():
        cmd  = 0b11000000 | (0 << 5)
        resp = spi.xfer2([cmd, 0x00])
        raw  = resp[1]
        pct  = (raw / 255) * 100

        percent_var.set(f"{pct:5.1f} %")
        pb['value'] = pct

        ts = datetime.now().isoformat()
        csv_writer.writerow([ts, f"{pct:.1f}"])
        log_file.flush()

        root.after(200, update_reading)
        
    def on_close():
        spi.close()
        log_file.close()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.after(0, update_reading)
    root.mainloop()

