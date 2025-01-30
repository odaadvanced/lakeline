Python 3.7.3 (/usr/bin/python3)
>>> %cd /home/pi/dev/lakeline/luke_code
>>> %Run Stop_Light_Project_V4.py
hello

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> %cd /home/pi/Public/prog_pi_ed3
>>> %Run 11_02_fancy_clock.py
Traceback (most recent call last):
  File "/home/pi/Public/prog_pi_ed3/11_02_fancy_clock.py", line 3, in <module>
    import board, time, gpiozero
ModuleNotFoundError: No module named 'board'
>>> %Run 11_01_clock.py
Traceback (most recent call last):
  File "/home/pi/Public/prog_pi_ed3/11_01_clock.py", line 3, in <module>
    import board, time
ModuleNotFoundError: No module named 'board'
>>> type ('helloe')
<class 'str'>
>>> %Run 11_01_clock.py
Traceback (most recent call last):
  File "/home/pi/Public/prog_pi_ed3/11_01_clock.py", line 3, in <module>
    import board, time
ModuleNotFoundError: No module named 'board'
>>> text = 'She ,what"
  File "<pyshell>", line 1
    text = 'She ,what"
                     ^
SyntaxError: EOL while scanning string literal
>>> text = 'She ','what''
  File "<pyshell>", line 1
    text = 'She ','what''
                        ^
SyntaxError: EOL while scanning string literal
>>> text = 'She '/'what''
  File "<pyshell>", line 1
    text = 'She '/'what''
                        ^
SyntaxError: EOL while scanning string literal
>>> text = 'She '/'what/''
  File "<pyshell>", line 1
    text = 'She '/'what/''
                         ^
SyntaxError: EOL while scanning string literal
>>> len ('abc')
3
>>> len ('abcg')
4
>>> string_lemgth = len('abc')
>>> string_lemgth
3
>>> my_sting = "now is \ to come"
>>> print my_sting
  File "<pyshell>", line 1
    print my_sting
                 ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(my_sting)?
>>> print (my_sting)
now is \ to come
>>> my_sting = """now is to come"""
>>> my_sting
'now is to come'
>>> print (my_sting)
now is to come
>>> my_sting = """now is\to come"""
>>> print (my_sting)
now is	o come
>>> my_sting = """now is\oto come"""
>>> print (my_sting)
now is\oto come
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> len(obj,/)
  File "<pyshell>", line 1
    len(obj,/)
            ^
SyntaxError: invalid syntax
>>> sting+sting
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'sting' is not defined
>>> sting_1="abra"
>>> sting_2="cadabra"
>>> m_sting=sting_1+sting_2
>>> m_sting
'abracadabra'
>>> f_name="arthur"
>>> l_name="Dent"
>>> f_name="Arthur"
>>> full_name=f_name+"" l_name;
  File "<pyshell>", line 1
    full_name=f_name+"" l_name;
                             ^
SyntaxError: invalid syntax
>>> full_name=f_name + "" l_name;
  File "<pyshell>", line 1
    full_name=f_name + "" l_name;
                               ^
SyntaxError: invalid syntax
>>> full_name= f_name + "" l_name;
  File "<pyshell>", line 1
    full_name= f_name + "" l_name;
                                ^
SyntaxError: invalid syntax
>>> full_name= f_name+""l_name;
  File "<pyshell>", line 1
    full_name= f_name+""l_name;
                             ^
SyntaxError: invalid syntax
>>> flavor='apple pie'
>>> flavor[1]
'p'
>>> flavor[0]
'a'
>>> flavor[09]
  File "<pyshell>", line 1
    flavor[09]
            ^
SyntaxError: invalid token
>>> flavor[08]
  File "<pyshell>", line 1
    flavor[08]
            ^
SyntaxError: invalid token
>>> flavor[8]
'e'
>>> flavor[-1]]
  File "<pyshell>", line 1
    flavor[-1]]
              ^
SyntaxError: invalid syntax
>>> flavor[-1]
'e'
>>> flavor[-6]
'l'
>>> flavor='apple_pie'
>>> flavor[0:3]
'app'
>>> flavor[0:5]
'apple'
>>> flavor[3:5]
'le'
>>> flavor[:5]
'apple'
>>> flavor[5:]
'_pie'
>>> flavor[0:]
'apple_pie'
>>> word="goal"
>>> word[0] = 'f'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> "Jean-luc Picard".lower()
'jean-luc picard'
>>> "Jean-luc Picard".upper()
'JEAN-LUC PICARD'
>>> load_voice="can you hear me yet?"
>>> load_voice
'can you hear me yet?'
>>> load_voice.upper()
'CAN YOU HEAR ME YET?'
>>> white_space= '    This has whie space'
>>> white_space
'    This has whie space'
>>> rsting=white_space.rstrip()
>>> rsting
'    This has whie space'
>>> lsting=white_space.lstrip()
>>> lsting
'This has whie space'
>>> white_space='this is white space'
>>> s_sting=white_space.strip()
>>> s_sting
'this is white space'
>>> starship='enterprise'
>>> starship='Enterprise'
>>> starship.startswith('en')
False
>>> starship.startswith('En')
True
>>> starship.lowerstartswith('en')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'str' object has no attribute 'lowerstartswith'
>>> starship.lower.startswith('en')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'startswith'
>>> starship.lower_startswith('en')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'str' object has no attribute 'lower_startswith'
>>> starship_lower.startswith('en')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'starship_lower' is not defined
>>> starship_=lower.startswith('en')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'lower' is not defined
>>> starship.endwith('se')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'str' object has no attribute 'endwith'
>>> starship.endswith('se')
True
>>> name='luke'
>>> name.capitalize
<built-in method capitalize of str object at 0xb4b451c0>
>>> name
'luke'
>>> name.upper
<built-in method upper of str object at 0xb4b451c0>
>>> name
'luke'
>>> print name.upper
  File "<pyshell>", line 1
    print name.upper
             ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(name.upper)?
>>> input()
q
'q'
>>> input('please enter a value')
please enter a value1
'1'
>>> input('please enter a value:')
please enter a value:787
'787'
>>> input('please enter a value:')ghiuhiaughiagifuawfdioahjcdiou
  File "<pyshell>", line 1
    input('please enter a value:')ghiuhiaughiagifuawfdioahjcdiou
                                                               ^
SyntaxError: invalid syntax
>>> input('please enter a value:')
please enter a value:abgihufbgigaiuhgfviua
'abgihufbgigaiuhgfviua'
>>> prompt='please enter a vaule'
>>> input(prompt)
please enter a vaule1
'1'
>>> prompt='please enter a vaule:'
>>> input(prompt)
please enter a vaule:2
'2'
>>> input(prompt)
please enter a vaule:22
'22'
>>> input(prompt)
please enter a vaule:5
'5'
>>> input(prompt)
please enter a vaule:5
'5'
>>> input(prompt)
please enter a vaule:7+7
'7+7'
>>> input(prompt)
please enter a vaule:14
'14'
>>> user_input=input(prompt)
please enter a vaule:1
>>> user_input
'1'
>>> user_input
'1'
>>> user_input
'1'
>>> user_input=input(prompt)
please enter a vaule:45
>>> user_input
'45'
>>> num='2'
>>> num +num
'22'
>>> num='12'
>>> num*3
'121212'
>>> '12'*"3"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> '12'*'3'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> '3'+3
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 3+3
6
>>> num=input('Enter a number to be dubled')
Enter a number to be dubled3
>>> nume
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'nume' is not defined
>>> num
'3'
>>> duubled_num=num*2
>>> print(doubled_num)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'doubled_num' is not defined
>>> print(duubled_num)
33
>>> %cd /home/pi/dev/lakeline/luke_code
>>> %Run Stop_Light_Project_V4.py
hello
q
quit

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Python 3.7.3 (/usr/bin/python3)
>>> my_num="12.0"
>>> my_num=int(my_num)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12.0'
>>> my_num='12'
>>> my_numn=int(my_num)
>>> prtin(my_num)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'prtin' is not defined
>>> print(my_num)
12
>>> num_pancakes=10
>>> "I am going to eat"+num_pancakes + "pancakes."
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> "I am going to eat"+ num_pancakes + "pancakes."
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> "I am going to eat"+ str(num_pancakes) + "pancakes."
'I am going to eat10pancakes.'
>>> "I am going to eat"+ str( num_pancakes ) + "pancakes."
'I am going to eat10pancakes.'
>>> "I am going to eat "+ str( num_pancakes ) + " pancakes."
'I am going to eat 10 pancakes.'
>>> arms=2
>>> heads=3
>>> print('has'+str(heads)+'heads and' + str(arms) + '
  File "<pyshell>", line 1
    print('has'+str(heads)+'heads and' + str(arms) + '
                                                     ^
SyntaxError: EOL while scanning string literal
>>> print('has'+str(heads)+'heads and' + str(arms) + ' arms.')
has3heads and2 arms.
>>> print('has '+str(heads)+' heads and ' + str(arms) + ' arms.')
has 3 heads and 2 arms.
>>> F"has{heads}heads and {arms}arms"
'has3heads and 2arms'
>>> F"has {heads} heads and {arms} arms"
'has 3 heads and 2 arms'
>>> 902*3945^293
3558099
>>> 902*3945^293/85
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: unsupported operand type(s) for ^: 'int' and 'float'
>>> phrase='The surpise is in here somewhere'
>>> phrase.find('surpise')
4
>>> phrase.find('today')
-1
>>> phrase.find('today''bady')
-1
>>> %cd /home/pi/Public/prog_pi_ed3
>>> 
>>> 
