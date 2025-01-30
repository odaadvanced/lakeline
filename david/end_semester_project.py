from oled_io import Oled_io
from gpiozero import LED, Button, TonalBuzzer
import time

red = LED(18)
yellow = LED(23)
green = LED(24)
button = Button(26)
bz = TonalBuzzer(19)

note_list = {1:"C4", 2:"D4", 3:"E4", 4:"F4", 5:"G4", 6:"A4", 7:"B4", 8:"C4", 9:"D4", 10:"E4", 11:"F4", 12:"G4", 13:"A4", 14:"B4", 14:"C4", 15:"D4"}
    


display = Oled_io()

display.print("DO NOT CROSS")
red.on()

    
    
    
def Button_Pressed():
    count_red = 15
    for x in range(1, 16):
        display.print("DO NOT CROSS:" + str(count_red))
        count_red = count_red - 1
        bz.play(note_list.get(count_red + 1))
        time.sleep(1)
        bz.stop()
    red.toggle()
    green.toggle()
    green_count = 15
    for x in range(1, 16):
        display.print("MAY CROSS:" + str(green_count))
        green_count = green_count - 1
        bz.play(note_list.get(green_count + 1))
        time.sleep(1)
        bz.stop()
    yellow.toggle()
    green.toggle()
    yellow_count = 3
    for x in range(1, 4):
        display.print("DO NOT CROSS:" + str(yellow_count))
        yellow_count = yellow_count - 1
        bz.play(note_list.get(yellow_count + 1))
        time.sleep(1)
        bz.stop()
    yellow.toggle()
    red.toggle()
    display.print("DO NOT CROSS")      
    

while True:
    button.wait_for_press()
    print("button was pressed")
    Button_Pressed()
    
