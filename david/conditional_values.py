Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle.py
Detected Barrier!  
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 1==1
True
>>> 3>5
False
>>> "a" == "a"
True
>>> "a" == "b"
False
>>> "a" < "b"
True
>>> "b" < "a"
False
>>> 1<2 and 3<4
True
>>> 1<2 and 3<2
False
>>> not True
False
>>> not False
True
>>> False == not True
  File "<pyshell>", line 1
    False == not True
               ^
SyntaxError: invalid syntax
>>> False == (not True)
True
>>> True and not (1 != 1)
True
>>> ("A" != "A") or not (2>=3)
True
>>> True False == True and False
  File "<pyshell>", line 1
    True False == True and False
             ^
SyntaxError: invalid syntax
>>> True and False == True and False
False
>>> (True and False) == (True and False)
True
>>> if 2+2 == 4:
    print("True")
    
True
>>> grade = 95
>>> %Run grade.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/david/grade.py", line 1
    grade 95
           ^
SyntaxError: invalid syntax
>>> %Run grade.py
You passed the class
thank you for attending
>>> %Run grade.py
YOU FAILED
thank you for attending
>>> %Run grade.py
You passed the class
you passes the class
thank you for attending
>>> %Run grade.py
YOU FAILED
thank you for attending
>>> %Run grade.py
You passed the class
thank you for attending
>>> %Run grade.py
YOU FAILED
thank you for attending
>>> %Run grade.py
you passes the class
thank you for attending
>>> %Run grade.py
You passed the class
thank you for attending
>>> %Run grade.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/david/grade.py", line 9
    else grade < 70:
             ^
SyntaxError: invalid syntax
>>> %Run grade.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/david/grade.py", line 9
    else grade < 70:
             ^
SyntaxError: invalid syntax
>>> %Run grade.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/david/grade.py", line 9
    else grade < 70:
             ^
SyntaxError: invalid syntax
>>> %Run grade.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/david/grade.py", line 9
    else grade < 70:
             ^
SyntaxError: invalid syntax
>>> %Run grade.py
55
YOU FAILED
thank you for attending
>>> %Run grade.py
98
You passed the class with an A
thank you for attending
>>> %Run grade.py
input a grade:86
you passes the class with a B
thank you for attending
>>> %Run grade.py
input a grade:100
You passes the class with an A+
thank you for attending
>>> %Run break.py
0
1
>>> %Run break.py
0
1
>>> %Run x_marks_the_spot.py
There was no 'X' in the phrase
>>> %Run x_marks_the_spot.py
There was no 'X' in the phrase
>>> %Run x_marks_the_spot.py
There was no 'X' in the phrase
>>> %Run x_marks_the_spot.py
>>> %Run x_marks_the_spot.py
There was no 'X' in the phrase
>>> %Run x_marks_the_spot.py
An 'X' has marked the spot
>>> int("not a number")
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'not a number'
>>> try:
    int("not a number")
  File "<pyshell>", line 2
    int("not a number")
                      ^
SyntaxError: unexpected EOF while parsing
>>> 
>>> "1" + 2
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(does_not_exist)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'does_not_exist' is not defined
>>> 1/0
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ZeroDivisionError: division by zero
>>> pow(2.0, 1000000000000000000000000)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
OverflowError: (34, 'Numerical result out of range')
>>> pow(10, 100)
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> pow(10, 1000)

>>> pow(10, 10000)

>>> pow(10, 100000)


>>> 
>>> %Run divide.py
>>> %Run divide.py
20
4
Both arguments must be numbers
>>> %Run divide.py

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run divide.py
1
0
num2 must not be 0
>>> %Run divide.py
4
2
2.0
>>> %Run divide.py
'1'
2
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/david/divide.py", line 9, in <module>
    divide(input(),input())
  File "/home/pi/dev/lakeline/david/divide.py", line 3, in divide
    print(int(num1)/int(num2))
ValueError: invalid literal for int() with base 10: "'1'"
>>> %Run divide.py
"1"
2
Both arguments must be integers
>>> %Run divide.py
1
1000000000000000000000000000000000000000000000000000000000000000000
1e-66
>>> 
