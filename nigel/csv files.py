Python 3.7.3 (/usr/bin/python3)
>>> import pathlib
>>> path = pathlib.Path("/home/pi/Documents/hello.text.txt")
>>> path
PosixPath('/home/pi/Documents/hello.text.txt')
>>> home = pathlib.Path.home()
>>> home
PosixPath('/home/pi')
>>> pathlib.Path.cwd()
PosixPath('/home/pi/lakeline/nigel/packages')
>>> relative_path = pathlib.Path("Documents")
>>> relative_path
PosixPath('Documents')
>>> absolute_path = relative_path.resolve
>>> absolute_path = relative_path.resolve()
>>> absolute_path
PosixPath('/home/pi/lakeline/nigel/packages/Documents')
>>> path = pathlib.Path.home () / "hello.txt"
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
>>> path.
  File "<pyshell>", line 1
    path.
        ^
SyntaxError: invalid syntax
>>> Path.
  File "<pyshell>", line 1
    Path.
        ^
SyntaxError: invalid syntax
>>> Path.period
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: type object 'Path' has no attribute 'period'
>>> path.period
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'PosixPath' object has no attribute 'period'
>>> path.touch
<bound method Path.touch of PosixPath('/home/pi/hello.txt')>
>>> nested_dir = new_dir / "folder_a" / "folder_b"
>>> nested_dir.mkdir()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
  File "/usr/lib/python3.7/pathlib.py", line 1251, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/home/pi/new_directory/folder_a/folder_b'
>>> nested_dir.mkdir(parents=True)
>>> nested_dir.mkdir()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
  File "/usr/lib/python3.7/pathlib.py", line 1251, in mkdir
    self._accessor.mkdir(self, mode)
FileExistsError: [Errno 17] File exists: '/home/pi/new_directory/folder_a/folder_b'
>>> nested_dir.is_dir()
True
>>> file_path = new_dir / "file1.txt"
>>> file_path.exists()
False
>>> file_path.touch()
>>> file_path.exists()
True
>>> file_path.is_file()
True
>>> path = Path.home() / "hello.txt"
>>> path.touch()
>>> file = path.open(mode="r",encoding="utf-8")
>>> file.close()
>>> file.return()
  File "<pyshell>", line 1
    file.return()
              ^
SyntaxError: invalid syntax
>>> file.return
  File "<pyshell>", line 1
    file.return
              ^
SyntaxError: invalid syntax
>>> my_path = Path.home() / "hello.txt"
>>> file = open(my_path, mode="r",encoding="utf-8")
>>> file
<_io.TextIOWrapper name='/home/pi/hello.txt' mode='r' encoding='utf-8'>
>>> with file as file:
    text = file.read()
    
>>> text
'Hello, World!\n'
>>> file = open(my_path, mode="r",encoding="utf-8")
>>> file = my_path.open(my_path, mode="r",encoding="utf-8")
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: open() got multiple values for argument 'mode'
>>> file = open(my_path, mode="r",encoding="utf-8")
>>> with file as file:
    text = file.read()
    
>>> text
'Hello, World!\nHello, World Again!\n'
>>> with file as file:
    for line in file.readlines():
        print(line)
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> file = my_path.open(mode="r",encoding="utf-8")
>>> with file as file:
    for line in file.readlines():
        print(line,end='')
        
Hello, World!
Hello, World Again!
>>> file = my_path.open(mode="r",encoding="utf-8")
>>> file = my_path.open(mode="w",encoding="utf-8") as file:
    file.write("Hi there!")
  File "<pyshell>", line 1
    file = my_path.open(mode="w",encoding="utf-8") as file:
                                                    ^
SyntaxError: invalid syntax
>>> with my_path.open(mode="w",encoding="utf-8") as file:
    file.write("Hi there!")
    
9
>>> file = my_path.open(mode="w",encoding="utf-8")
>>> with file as file:
    file.write("Hi there!")
    
9
>>> my_file = my_path.open(mode="r",encoding="utf-8")
>>> with my _file as file:
    for lin in file.realines():
        print(line, end='')
        
  File "<pyshell>", line 1
    with my _file as file:
                ^
SyntaxError: invalid syntax
>>> with my_file as file:
    for lin in file.realines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
AttributeError: '_io.TextIOWrapper' object has no attribute 'realines'
>>> with my_file as file:
    for line in file.realines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> my_file = my_path.open(mode="r",encoding="utf-8")
>>> with my_file as file:
    for line in file.realines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
AttributeError: '_io.TextIOWrapper' object has no attribute 'realines'
>>> with my_file as file:
    for line in file.readines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> my_file = my_path.open(mode="r",encoding="utf-8")
>>> with my_file as file:
    for line in file.readines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
AttributeError: '_io.TextIOWrapper' object has no attribute 'readines'
>>> with my_file as file:
    for line in file.readlines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> my_file = my_path.open(mode="r",encoding="utf-8")
>>> with my_file as file:
    for line in file.readlines():
        print(line, end='')
        
Hi there!
>>> my_file = my_path.open(mode="r",encoding="utf-8")
>>> with my_file as file:
    file.write("Hi there again!")
    
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
io.UnsupportedOperation: not writable
>>> my_file = my_path.open(mode="a",encoding="utf-8")
>>> with my_file as file:
    file.write("Hi there again!")
    
15
>>> my_file = my_path.open(mode="r",encoding="utf-8")
>>> with my_file as file:
    for line in file.readlines():
        print(line, end='')
        
Hi there!Hi there again!
>>> file_path = Path.home() /
  File "<pyshell>", line 1
    file_path = Path.home() /
                            ^
SyntaxError: invalid syntax
>>> file_path = Path.home() / "temperature.csv"
>>> temperature_readings = [68, 65, 68, 70, 74, 72]
>>> with file_path.open(mode="a",encoding="utf-8") as file:
    file.write(str(temperature_reading[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")
        
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
NameError: name 'temperature_reading' is not defined
>>> file_path = Path.home() / "temperatures.csv"
>>> temperature_readings = [68, 65, 68, 70, 74, 72]
>>> with file_path.open(mode="a",encoding="utf-8") as file:
    file.write(str(temperature_reading[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")
        
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
NameError: name 'temperature_reading' is not defined
>>> with file_path.open(mode="a",encoding="utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f",{temp}")
        
2
3
3
3
3
3
>>> with file_path.open(mode="r",encoding="utf-8") as file:
    text = file.read()
    
>>> text
'68,65,68,70,74,72'
>>> temperature = text.split(",")
>>> temperatures
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'temperatures' is not defined
>>> temperature
['68', '65', '68', '70', '74', '72']
>>> daily_temperatures = [[68, 65, 68, 70, 74, 72,],[ 67, 67, 70, 72, 70],[68, 70, 74, 76, 74, 73],]
>>> file = my_path.open(mode="w",encoding="utf-8", newline="")
>>> import csv
>>> writer = csv.writer(file)
>>> for temp_list in daily_temeratures:
    writer.writerow(temp_list)
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'daily_temeratures' is not defined
>>> file = my_path.open(mode="r",encoding="utf-8", newline="")
>>> reader = csv.reader(file)
>>> for row in reader:
    print(row)
    
>>> 