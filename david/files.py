Python 3.7.3 (/usr/bin/python3)
>>> import pathlib
>>> path = pathlib.Path("/home/pi/Documents/hello.txt")
>>> path
PosixPath('/home/pi/Documents/hello.txt')
>>> home = pathlib.Path.home()
>>> home
PosixPath('/home/pi')
>>> pathlib.Path.cwd()
PosixPath('/home/pi/dev/lakeline/david/packages')
>>> relative_path = pathlib.Path("Documents")
>>> relative_path
PosixPath('Documents')
>>> absolute_path - relative_path.resolve()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'absolute_path' is not defined
>>> absolute_path = relative_path.resolve()
>>> absolute_path
PosixPath('/home/pi/dev/lakeline/david/packages/Documents')
>>> home = pathlib.Path.home()
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
>>> my_sanity.exists()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_sanity' is not defined
>>> nested_dir = new_dir / "folder_a" / "folder b"
>>> nested_dir.mkdir()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
  File "/usr/lib/python3.7/pathlib.py", line 1251, in mkdir
    self._accessor.mkdir(self, mode)
FileNotFoundError: [Errno 2] No such file or directory: '/home/pi/new_directory/folder_a/folder b'
>>> nested_dir.mkdir(parents=True)
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
>>> file = path.open(mode="r", encoding="utf-8")
>>> file
<_io.TextIOWrapper name='/home/pi/hello.txt' mode='r' encoding='utf-8'>
>>> file.close()
>>> file
<_io.TextIOWrapper name='/home/pi/hello.txt' mode='r' encoding='utf-8'>
>>> my_path = Path.home() / "hello.txt"
>>> file = open(my_path, mode="r", encoding="utf-8")
>>> file
<_io.TextIOWrapper name='/home/pi/hello.txt' mode='r' encoding='utf-8'>
>>> text = file.read()
>>> text
'Hello, World!\n'
>>> text
'Hello, World!\n'
>>> text = file.read()
>>> text
'Hello, World Again!\n'
>>> file = path.open(mode="r", encoding="utf-8")
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
>>> with file as file:
    for line in file.readlines():
        print(line)
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for line in file.readlines():
        print(line)
        
Hello, World!

Hello, World Again!

>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for file in file.readlines():
        print(line, end="")
        
Hello, World Again!
Hello, World Again!
>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for file in file.readlines():
        print(line, end="")
        
Hello, World Again!
Hello, World Again!
>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for file in file.readlines():
        print(line, end='')
        
Hello, World Again!
Hello, World Again!
>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for file in file.readlines():
        print(line, end='')
        
Hello, World Again!
Hello, World Again!
>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for file in file.readlines():
        print(line, end='')
        
Hello, World Again!
Hello, World Again!
>>> file.close()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'str' object has no attribute 'close'
>>> file = path.open(mode="r", encoding="utf-8")
>>> with file as file:
    for file in file.readlines():
        print(line, end='')
        
Hello, World Again!
Hello, World Again!
>>> file
'Hello, World Again!\n'
>>> with my_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!")
    
9
>>> with my_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!/n")
    
11
>>> with my_path.open(mode="w", encoding="utf-8") as file:
    file.write("Hi there!\n")
    
10
>>> file = path.open(mode="r", encoding="utf-8")
>>> with my_file as file:
    for lines in file.readlines():
        print(line, end='')
        
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_file' is not defined
>>> my_file = path.open(mode="r", encoding="utf-8")
>>> with my_file as file:
    for lines in file.readlines():
        print(line, end='')
        
Hello, World Again!
>>> my_path
PosixPath('/home/pi/hello.txt')
>>> with my_file as file:
    file.write("Hi there again")
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> my_file = my_path.open(mode="a", encoding="utf-8")
>>> with my_file as file:
    file.write("Hi there again")
    
14
>>> my_file = my_path.open(mode="a", encoding="utf-8")
>>> with my_file as file:
    file.write("Hi there again\n")
    
15
>>> my_file = my_path.open(mode="r", encoding="utf-8")
>>> for line in file.readlines():
    print(line, end"")
    
  File "<pyshell>", line 2
    print(line, end"")
                    ^
SyntaxError: invalid syntax
>>> for line in file.readlines():
    print(line, end="")
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> my_file = my_path.open(mode="r", encoding="utf-8")
>>> for line in file.readlines():
    print(line, end="")
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> my_file = my_path.open(mode="r", encoding="utf-8")
>>> from pathlib import path
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ImportError: cannot import name 'path' from 'pathlib' (/usr/lib/python3.7/pathlib.py)
>>> file_path = Path.home() / "temperatures.csv"
>>> temperature_readings = [68, 65, 68, 70, 74, 72]
>>> with file_path.open(mode"a", encoding="utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:] :
        file.write(f",{temp}")
        
  File "<pyshell>", line 1
    with file_path.open(mode"a", encoding="utf-8") as file:
                              ^
SyntaxError: invalid syntax
>>> with file_path.open(mode="a", encoding="utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:] :
        file.write(f",{temp}")
        
2
3
3
3
3
3
>>> with file_path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    
>>> text
'68,65,68,70,74,72'
>>> temperatures = text.split(",")
>>> temperatures
['68', '65', '68', '70', '74', '72']
>>> daily_temperatures
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'daily_temperatures' is not defined
>>> daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [20, 4, 13, 19, 32, 105]]
>>> file = file_path.open(mode="w", encoding="utf-8", newline="")
>>> import csv
>>> writer = csv.writer(file)
>>> for temp_list in daily_temperatures:
    writer.writerow(temp_list)
    
19
19
19
>>> file.close()
>>> file = file_path.open(mode="r", encoding="utf-8", newline="")
>>> reader = csv.reader(file)
>>> for row in reader:
    print(row)
    
['68', '65', '68', '70', '74', '72']
['67', '67', '70', '72', '72', '70']
['20', '4', '13', '19', '32', '105']
>>> 
