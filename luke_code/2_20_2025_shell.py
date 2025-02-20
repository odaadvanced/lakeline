Python 3.7.3 (/usr/bin/python3)
>>> %cd /home/pi/dev/lakeline/luke_code
>>> %Run Obstacle_speaking.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/luke_code/Obstacle_speaking.py", line 33, in <module>
    main()
  File "/home/pi/dev/lakeline/luke_code/Obstacle_speaking.py", line 23, in main
    tts.say()
TypeError: say() missing 1 required positional argument: 'words'
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
Detected Barrier!
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
Detected Barrier!
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle_rvr.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run obstacle.py
No Barrier        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> typr(True)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'typr' is not defined
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 1 == 1
True
>>> 3 > 5
False
>>> "a" == "a"
True
>>> "a" == "b"
False
>>> "a" < "b"
True
>>> "a" > "b"
False
>>> "a" == "b"
False
>>> "A" > "b"
False
>>> "A" < "b"
True
>>> "a" < "b"
True
>>> "a" == "A"
False
>>> 1 < 2 and 3 < 4
True
>>> 1 < 2 and 3 < 2
False
>>> 2 < 1 and 4 < 3
False
>>> 2 < 1 and 4 < 6
False
>>> 2 < 2 and 4 < 4
False
>>> 1 < 2 or 3 < 4
True
>>> 1 < 2 or 3 < 2
True
>>> 1 < 2 or "a" > "b" 
True
>>> 2 < 1 or "a" > "b" 
False
>>> 2 < 1 or "a" < "b" 
True
>>> not True
False
>>> not False
True
>>> <, <=, ==, >=, >
  File "<pyshell>", line 1
    <, <=, ==, >=, >
    ^
SyntaxError: invalid syntax
>>> not
  File "<pyshell>", line 1
    not
      ^
SyntaxError: invalid syntax
>>> and
  File "<pyshell>", line 1
    and
      ^
SyntaxError: invalid syntax
>>> or
  File "<pyshell>", line 1
    or
     ^
SyntaxError: invalid syntax
>>> not 2 > 6
True
>>>  2 > 6
False
>>> False == not True
  File "<pyshell>", line 1
    False == not True
               ^
SyntaxError: invalid syntax
>>> False == (not) True
  File "<pyshell>", line 1
    False == (not) True
                 ^
SyntaxError: invalid syntax
>>> False == (not True)
True
>>> True and not (1 != 1 )
True
>>> True and False == True and False
False
>>> (True and False) == (True and False)
True
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> 
>>> 2+2
4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> if 2+2 == 4:
    print ("2 and 2 is 4")
    
2 and 2 is 4
>>> %Run Passed_test.py
You passed the class!
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/luke_code/Passed_test.py", line 4, in <module>
    Print("Thank you for atteding")
NameError: name 'Print' is not defined
>>> %Run Passed_test.py
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
Thank you for atteding
>>> %Run Passed_test.py

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run Passed_test.py
Thank you for atteding
>>> %Run Passed_test.py
you failed the class
Thank you for atteding
>>> %Run Passed_test.py
you failed the class
Thank you for atteding
>>> %Run Passed_test.py
give grade
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run Passed_test.py
give grade :80
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :50
you failed the class
Thank you for atteding
>>> %Run Passed_test.py
give grade :100
You got a A great job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
You got a A great job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/luke_code/Passed_test.py", line 5
    if grade > =90:
               ^
SyntaxError: invalid syntax
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
You got a A great job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
You got a A great job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :90
You got a A great job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :70
You got a A great job!
You passed the class!
You failed the class
Thank you for atteding
>>> %Run Passed_test.py
give grade :70
You got a A great job!
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :50
You got a A great job!
You failed the class
Thank you for atteding
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
Thank you for atteding
>>> %Run Passed_test.py
give grade :
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
Thank you for atteding
>>> %Run Passed_test.py
give grade :99
You got a A great job!
Thank you for atteding
>>> %Run Passed_test.py
give grade :89
You passed the class!
Thank you for atteding
>>> %Run Passed_test.py
give grade :hello
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/luke_code/Passed_test.py", line 2, in <module>
    grade = float (input("give grade :"))
ValueError: could not convert string to float: 'hello'
>>> %Run Passed_test.py
give grade :100
You got a +A amazing job!
Thank you for atteding
>>> %Run Passed_test.py
give grade :90
You got a A great job!
Thank you for atteding
>>> %Run Break_Satement.py
0
1
Finished with n = 2
>>> %Run Break_Satement.py
0
1
Finished with n = 2
>>> %Run Break_Satement.py
0
1
Finished with n = 2
>>> %Run Break_Satement.py
0
1
Finished with n = 2
>>> %Run Break_Satement.py
0
1
2
3
Finished with n = 3
>>> %Run Break_Satement.py
0
1
2
3
Finished with n = 3
>>> %Run Break_Satement.py
0
1
2
Finished with n = 3
>>> %Run for_else_loop.py
There was no'X' in the phrase
>>> %Run for_else_loop.py
There was no'X' in the phrase
>>> %Run for_else_loop.py
>>> %Run for_else_loop.py
There was no'X' in the phrase
>>> %Run for_else_loop.py
>>> %Run for_else_loop.py
Write a phrase: hello
There was no'X' in the phrase
>>> %Run for_else_loop.py
Write a phrase: X
>>> %Run for_else_loop.py
Write a phrase: Hello X
X was in the phrase
>>> %Run for_else_loop.py
Write a phrase: x
X was in the phrase
>>> int ("not a number")
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'not a number'
>>> float ("not a number")
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: could not convert string to float: 'not a number'
>>> "1" = 2
  File "<pyshell>", line 1
SyntaxError: can't assign to literal
>>> int ("1" = 2)
  File "<pyshell>", line 1
SyntaxError: keyword can't be an expression
>>> int "1" = 2
  File "<pyshell>", line 1
    int "1" = 2
          ^
SyntaxError: invalid syntax
>>> print(dose_not_exist)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'dose_not_exist' is not defined
>>> print phrase
  File "<pyshell>", line 1
    print phrase
               ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(phrase)?
>>> print (phrase)
x
>>> 1/0
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ZeroDivisionError: division by zero
>>> pow(2.0, 1_000_000)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
OverflowError: (34, 'Numerical result out of range')
>>> 6^7
1
>>> 2^2
0
>>> 2^4
6
>>> 2^6
4
>>> 2^6
4
>>> 2^8
10
>>> 2**@
  File "<pyshell>", line 1
    2**@
       ^
SyntaxError: invalid syntax
>>> 2**2
4
>>> %Run try_except.py
>>> %Run try_except.py
>>> %Run try_except.py
>>> divide
<function divide at 0xb5c4ec90>
>>> divide(2,3)
0.6666666666666666
>>> %Run try_except.py
give a number2
give a number2
>>> %Run try_except.py
Traceback (most recent call last):
  File "/home/pi/dev/lakeline/luke_code/try_except.py", line 1, in <module>
    divide
NameError: name 'divide' is not defined
>>> divide (2,5)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'divide' is not defined
>>> %Run try_except.py
>>> divide(3,2)
1.5
>>> %Run try_except.py
>>> divide(3,9)
0.3333333333333333
>>> %Run try_except.py
>>> divide
<function divide at 0xb5c77c90>
>>> 
