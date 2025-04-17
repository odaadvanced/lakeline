Python 3.7.3 (/usr/bin/python3)
>>> %Run flameSensor.py
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
The end !
>>> %FastDebug flameSensor.py
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0
Current analog value is 0

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %FastDebug ADC0832.py
>>> help(gpio.output)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'gpio' is not defined
>>> import gpio
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ModuleNotFoundError: No module named 'gpio'
>>> import RPi.GPIO as GPIO
>>> help(GPIO.output)
Help on built-in function output in module RPi._GPIO:

output(...)
    Output to a GPIO channel or list of channels
    channel - either board pin number or BCM number depending on which mode is set.
    value   - 0/1 or False/True or LOW/HIGH

>>> 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> import pathlib
>>> path = pathlib.Path("/home/pi/Documents/hello.text")
>>> path = pathlib.Path("/home/pi/Documents/hello.txt")
>>> path
PosixPath('/home/pi/Documents/hello.txt')
>>> home = pathlib.Path.home()
>>> home
PosixPath('/home/pi')
>>> pathlib.path.cwd()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: module 'pathlib' has no attribute 'path'
>>> pathlib.Path.cwd()
PosixPath('/home/pi/dev/lakeline/timothy')
>>> relative_path = pathlib.Path("Documents")
>>> relative_path
PosixPath('Documents')
>>> absolute_path = relative_path.resolve()
>>> absolute_path
PosixPath('/home/pi/dev/lakeline/timothy/Documents')
>>> home / pathlib.Path("Photos/image.png")
PosixPath('/home/pi/Photos/image.png')
>>> path = pathlib.Path.home() / "hello.txt"
>>> path
PosixPath('/home/pi/hello.txt')
>>> path.exists()
False
>>> path.exists()
True
>>> path.is_file()
True
>>> path.is_dir()
False
>>> home.is_dir()
True
>>> from pathlib import Path
>>> new_dir = Path.home() / "new_directory"
>>> new_dir.mkdir()
>>> new_dir.exists()
True
>>> new_dir.is_dir()
True
>>> nested_dir = new_dir / "folder_a" / "folder_b"
>>> nested_dir.make_dir()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'PosixPath' object has no attribute 'make_dir'
>>> nested_dir.make_dir(parents=True)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'PosixPath' object has no attribute 'make_dir'
>>> nested_dir.mkdir(parents=True)
>>> fil_path = new_dir / "file1.txt"
>>> file_path = new_dir / "file1.txt"
>>> file_path.exists()
False
>>> file_path.touch()
>>> file_path.exists()
True
>>> file_path.is_file()
True
>>> path.touch()
>>> file = path.open(mode="r", encoding="utf-8")
>>> file.close()
>>> file
<_io.TextIOWrapper name='/home/pi/hello.txt' mode='r' encoding='utf-8'>
>>> my_path = Path.home() / "hello.txt"
>>> file = open(my_path, mode="r", encoding="utf-8")
>>> file
<_io.TextIOWrapper name='/home/pi/hello.txt' mode='r' encoding='utf-8'>
>>> with file as file:
    text=file.read()
    
>>> text
'Hello, World!\n'
>>> file = my_path.open(mode="r", encoding="utf-8")
>>> with file as file:
    text=file.read()
    
>>> text
'Hello, World!\nHello, World Again!\n'
>>> file = my_path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for line in file.readlines():
        print(line)
        
Hello, World!

Hello, World Again!

>>> with file as file:
    for line in file.readlines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> file = my_path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for line in file.readlines():
        print(line, end='')
        
Hello, World!
Hello, World Again!
>>> file = my_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!")
  File "<pyshell>", line 1
    file = my_path.open(mode="w", encoding="utf-8") as file:
                                                     ^
SyntaxError: invalid syntax
>>> with my_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!")
    
9
>>> with my_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!\n")
    
10
>>> file = my_path.open(mode="w", encoding="utf-8")
>>> with file as file:
    file.write("Greetings and salutations!\n")
    
27
>>> file = my_path.open(mode="r", encoding="utf-8")
>>> with my_file as file:
    for line in file.readlines():
        print(line, end="")
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_file' is not defined
>>> with file as file:
    for line in file.readlines():
        print(line, end="")
     
Greetings and salutations!
>>> file = my_path.open(mode="a", encoding="utf-8")
>>> with file as file:
    file.write("Salutations and greetings!")
    
26
>>> file = my_path.open(mode="a", encoding="utf-8")
>>> with file as file:
    file.write("\nSalutations and greetings!\n")
    
28
>>> file = my_path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for line in file.readlines():
        print(line, end="")
     
Greetings and salutations!
Salutations and greetings!
Salutations and greetings!
>>> file_path = Path.home() / "temperatures.csv"
>>> temperature_readings = [68, 65, 68, 70, 74, 72]
>>> with file_path.open(mode='a', encoding='utf-8') as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp")
        
  File "<pyshell>", line 4
SyntaxError: f-string: expecting '}'
>>> with file_path.open(mode='a', encoding='utf-8') as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")
        
2
3
3
3
3
3
>>> file = my_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
  File "<pyshell>", line 1
    file = my_path.open(mode="r", encoding="utf-8") as file:
                                                     ^
SyntaxError: invalid syntax
>>> 
>>> with my_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    
>>> text
'Greetings and salutations!\nSalutations and greetings!\nSalutations and greetings!\n'
>>> with file_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    
>>> text
'68,65,68,70,74,72'
>>> temperatures = text.split(',')
>>> temperatures
['68', '65', '68', '70', '74', '72']
>>> daily_temperatures = [ [68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70],[68,70,74,76,74,73],]
>>> file = file_path.open(mode='w',encoding='utf-8', newline='')
>>> import csv
>>> writer = csv.writer(file)
>>> for temp_list in daily_temperatures:
    writer.writerow(temp_list)
    
19
19
19
>>> file.close()
>>> file = file_path.open(mode='r',encoding='utf-8', newline='')
>>> reader = csv.reader(file)
>>> for row in reader:
    print(row)
    
['68', '65', '68', '70', '74', '72']
['67', '67', '70', '72', '72', '70']
['68', '70', '74', '76', '74', '73']
>>> file.close()
>>> 
