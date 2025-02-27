Python 3.7.3 (/usr/bin/python3)
>>> my_tuple = (1, 2, 3)
>>> my_tuple
(1, 2, 3)
>>> type (my_tuple)
<class 'tuple'>
>>> my_tuple = tuple ('1, 2, 4, 5, 6')
>>> my_tuple = tuple ('12456')
>>> my_tuple
('1', '2', '4', '5', '6')
>>> my_tuple = (1, 2, 4, 5, 6)
>>> my_tuple
(1, 2, 4, 5, 6)
>>> my_tuple = tuple ('12456')
>>> my_tuple = tuple ('1,2,4,5,6')
>>> my_tuple
('1', ',', '2', ',', '4', ',', '5', ',', '6')
>>> def_values = 
  File "<pyshell>", line 1
    def_values =
               ^
SyntaxError: invalid syntax
>>> def_values = ("Luke", 17, 'Austin', 78633)
>>> def_values
('Luke', 17, 'Austin', 78633)
>>> def_values = ("Luke", 17, 'Austin', 78633)
>>> def_values
('Luke', 17, 'Austin', 78633)
>>> len(my_tuple)
9
>>> my_str = ("now is the time")
>>> len (my_str)
15
>>> my_tuple[2]
'2'
>>> my_str[2]
'w'
>>> my_tuple[2:4]
('2', ',')
>>> my_tuple = tuple (1,2,4,5,6)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: tuple expected at most 1 arguments, got 5
>>> my_tuple = (1,2,4,5,6)
>>> my_tuple[2] = 4
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> my_tuple[2] = 3
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> my_tuple
(1, 2, 4, 5, 6)
>>> for number in my_tuple:
    print(number)
    
1
2
4
5
6
>>> for n in my_tuple:
    print(n)
    
1
2
4
5
6
>>> new_tuple = 23.3, 45.6
>>> new_tuple
(23.3, 45.6)
>>> type new_tuple
  File "<pyshell>", line 1
    type new_tuple
                 ^
SyntaxError: invalid syntax
>>> type (new_tuple)
<class 'tuple'>
>>> x, y = new_tuple
>>> x
23.3
>>> y
45.6
>>> x + y
68.9
>>> x == y
False
>>> x  >= y
False
>>> x  <= y
True
>>> x  <= not y
  File "<pyshell>", line 1
    x  <= not y
            ^
SyntaxError: invalid syntax
>>> x + y = b
  File "<pyshell>", line 1
SyntaxError: can't assign to operator
>>> first, middle, last = 'Luke', 'William', 'Alcott'
>>> first
'Luke'
>>> middle
'William'
>>> last
'Alcott'
>>> Last
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'Last' is not defined
>>> num1, num2, num3 = 1,2,3,4
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: too many values to unpack (expected 3)
>>> num1, num2, num3 = 1,2,3
>>> num1
1
>>> num3
3
>>> vowels =('a' , 'e', 'i', 'o', 'u')
>>> 'o' in vowels
True
>>> 'O' in vowels
False
>>> 'x' in vowels
False
>>> def add_SUB (A, B):
    return (A+B, A-B)

>>> add_sub(5,3)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'add_sub' is not defined
>>> def add_sub (A, B):
    return (A+B, A-B)

>>> add_sub
<function add_sub at 0xb4ac9540>
>>> add_sub(5,3)
(8, 2)
>>> x , y = add_sub(5,3)
>>> x
8
>>> y
2
>>> x+y
10
>>> colors =["red", "yellow", "green", "blue"]
>>> colors
['red', 'yellow', 'green', 'blue']
>>> type colors
  File "<pyshell>", line 1
    type colors
              ^
SyntaxError: invalid syntax
>>> type colors)
  File "<pyshell>", line 1
    type colors)
              ^
SyntaxError: invalid syntax
>>> type (colors)
<class 'list'>
>>> list ('python')
['p', 'y', 't', 'h', 'o', 'n']
>>> my_colors = "red, orange, blue, grenn"
>>> my_colors
'red, orange, blue, grenn'
>>> my_colors_list = my_colors.split(',')
>>> my_colors_list
['red', ' orange', ' blue', ' grenn']
>>> my_colors_list[2]
' blue'
>>> my_colors_list[1:3]
[' orange', ' blue']
>>> 'black' in my_colors_list
False
>>> ' blue' in my_colors_list
True
>>> Lower(Luke)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'Lower' is not defined
>>> number = [1, 2, 3, 4, 5, 6]
>>> number[2] = 10
>>> number
[1, 2, 10, 4, 5, 6]
>>> number[2:4] == [30,40,50]
False
>>> number[2:4] = [30,40,50]
>>> number
[1, 2, 30, 40, 50, 5, 6]
>>> number.insert(3, 'not number')
>>> number
[1, 2, 30, 'not number', 40, 50, 5, 6]
>>> a=90
>>> n=0
>>> 1=9
  File "<pyshell>", line 1
SyntaxError: can't assign to literal
>>> int 1=9
  File "<pyshell>", line 1
    int 1=9
        ^
SyntaxError: invalid syntax
>>> int (1 = 9)
  File "<pyshell>", line 1
SyntaxError: keyword can't be an expression
>>> a
90
>>> b=45
>>> c = a + b - 180
>>> c
-45
>>> c = 180 - a + b
>>> c
135
>>> c = 180 - (a + b)
>>> c
45
>>> a=70
>>> b=50
>>> c
45
>>> c = 180 - (a + b)
>>> c
60
>>> number.extend([200,300,400])
>>> number
[1, 2, 30, 'not number', 40, 50, 5, 6, 200, 300, 400]
>>> total = 0
>>> for number in number:
    total = total + number
    
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> number = [1, 2, 30, 40, 50, 5, 6, 100, 200, 300,400]
>>> for number in number:
    total = total + number
    
>>> for a in number:
    total = total + a
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> number
400
>>> total=0
>>> for a in number:
    total = total + a
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> numbers = [1, 2, 30, 40, 50, 5, 6, 100, 200, 300,400]
>>> for number in numbers:
    total = total + number
    
>>> total=0
>>> for number in numbers:
    total = total + number
    
>>> numbers
[1, 2, 30, 40, 50, 5, 6, 100, 200, 300, 400]
>>> total
1134
>>> nums = [20, 30, 1, 400, 30, 50, 60]
>>> min(nums)
1
>>> max(num)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'num' is not defined
>>> max(nums)
400
>>> %Run triangle_angle_finder.py
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 4
    print c
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(c)?
>>> %Run triangle_angle_finder.py
angle a
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run triangle_angle_finder.py
angle a: 30
angle b: 50
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 3, in <module>
    c = 180 - (a+b)
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> %Run triangle_angle_finder.py
angle a: 30
angle b: 50
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 3, in <module>
    c = float(180 - (a + b))
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> %Run triangle_angle_finder.py
angle a: 30
angle b: 60
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 3, in <module>
    c = int(180 - (a + b))
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> %Run triangle_angle_finder.py
angle a: 2
angle b: 3
157
>>> %Run triangle_angle_finder.py
angle a: 30
angle b: 60
-2880
>>> %Run triangle_angle_finder.py
angle a: 30
angle b: 60
-2880
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
-4365.0
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 4, in <module>
    c = 180 - k
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 5, in <module>
    c = g - k
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 5, in <module>
    c = int(g - k)
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> %Run triangle_angle_finder.py
angle a: 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 5, in <module>
    c = int(float(g - k))
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> g = 80
>>> f = 5
>>> g - f
75
>>> h = g - f
>>> h
75
>>> h + g
155
>>> list_1 = [1,2,3,4]
>>> list_2 = list_1
>>> list_2.append(5)
>>> list_2
[1, 2, 3, 4, 5]
>>> list_1
[1, 2, 3, 4, 5]
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
90.0
>>> %Run triangle_angle_finder.py
angle a: 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
90.0
>>> %Run triangle_angle_finder.py
angle a: 70
angle b: 100
10.0
>>> matrix_1 = [[1,2] , [3,4]]
>>> matrix_2 = matrix_1[:]
>>> matrix_2
[[1, 2], [3, 4]]
>>> matrix_2 = [7,8]
>>> matrix_2
[7, 8]
>>> matrix_1
[[1, 2], [3, 4]]
>>> matrix_1[1][1]=10
>>> matrix_1
[[1, 2], [3, 10]]
>>> matrix_2
[7, 8]
>>> %Run triangle_angle_finder.py
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 6
    else a+b <= 180:
         ^
SyntaxError: invalid syntax
>>> import copy
>>> matrix_3 = copy.deepcopy(matrix_1)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'matrix_1' is not defined
>>> matrix_3 = copy.deepcopy(matrix_1)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'matrix_1' is not defined
>>> matrix_1
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'matrix_1' is not defined
>>> matrix_1[1][1]=10
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'matrix_1' is not defined
>>> %Run triangle_angle_finder.py
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 6
    else:
       ^
SyntaxError: invalid syntax
>>> %Run triangle_angle_finder.py
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 6
    elif:
       ^
SyntaxError: invalid syntax
>>> %Run triangle_angle_finder.py
Traceback (most recent call last):
  File "/home/pi/lakeline/luke_code/triangle_angle_finder.py", line 6
    elif:
        ^
SyntaxError: invalid syntax
>>> numbers
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'numbers' is not defined
>>> numbers
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'numbers' is not defined
>>> number
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'number' is not defined
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
90.0
>>> letter = ['z', 'ab', 'bc', 'ba', 'x', 'c']
>>> letter
['z', 'ab', 'bc', 'ba', 'x', 'c']
>>> letter.sort()
>>> letter
['ab', 'ba', 'bc', 'c', 'x', 'z']
>>> %Run triangle_angle_finder.py
angle a: 100
angle b: 100
no
>>> %Run triangle_angle_finder.py
angle a: 45 
angle b: 45
90.0
>>> %Run triangle_angle_finder.py
angle a: 100
angle b: 100
too big over 180
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
angle c is90.0
>>> %Run triangle_angle_finder.py
angle a: 45
angle b: 45
angle c is 90.0 degress
>>> %Run triangle_angle_finder.py
angle a: 40
angle b: 70
angle c is 70.0 degress
>>> capitals = {
    "California": "Sacramento",
    "New York" : "Albany",
    "Texas" : "Austin"
    }
>>> capitals
{'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin'}
>>> key_value_pairs = (
    ("California", "Sacramento"),
    ("NewYprk", "Albany"),
    ("Texas" , "Austin")
    )
>>> key_value_pairs
(('California', 'Sacramento'), ('NewYprk', 'Albany'), ('Texas', 'Austin'))
>>> type(key_value_pairs)
<class 'tuple'>
>>> capital = dict(key_value_pairs)
>>> capitals
{'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin'}
>>> capital
{'California': 'Sacramento', 'NewYprk': 'Albany', 'Texas': 'Austin'}
>>> type (capital)
<class 'dict'>
>>> capital['Texas']
'Austin'
>>> capital["Colorado"] = "Boulder"
>>> capital
{'California': 'Sacramento', 'NewYprk': 'Albany', 'Texas': 'Austin', 'Colorado': 'Boulder'}
>>> del capital['Colorado']
>>> capital
{'California': 'Sacramento', 'NewYprk': 'Albany', 'Texas': 'Austin'}
>>> capital['Azizona']
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'Azizona'
>>> capital['Arizona']
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'Arizona'
>>> for key in capital:
    print(key)
    
California
NewYprk
Texas
>>> for key in capital:
    print(f"The capital of {key} is {capitals[state]}")
    
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
NameError: name 'state' is not defined
>>> for key in capital:
    print(f"The capital of {key} is {[state]}")
    
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
NameError: name 'state' is not defined
>>> for state in capital:
    print(f"The capital of {capital} is {capital[state]}")
    
The capital of {'California': 'Sacramento', 'NewYprk': 'Albany', 'Texas': 'Austin'} is Sacramento
The capital of {'California': 'Sacramento', 'NewYprk': 'Albany', 'Texas': 'Austin'} is Albany
The capital of {'California': 'Sacramento', 'NewYprk': 'Albany', 'Texas': 'Austin'} is Austin
>>> %Run triangle_angle_finder.py
angle a: 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> for state in capital:
    print(f"The capital of {capital} is {capital[state]}")
    
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'capital' is not defined
>>> capital = dict(key_value_pairs)
