Python 3.7.3 (/usr/bin/python3)
>>> type("Hello, world")
<class 'str'>
>>> string1='Hello'
>>> string_2='Goodbye'
>>> string_3="We're #1!"
>>> string_4='I said 
  File "<pyshell>", line 1
    string_4='I said
                   ^
SyntaxError: EOL while scanning string literal
>>> text = "She said, "What time is it?""
  File "<pyshell>", line 1
    text = "She said, "What time is it?""
                          ^
SyntaxError: invalid syntax
>>> text = "She said, 'What time is it?'
  File "<pyshell>", line 1
    text = "She said, 'What time is it?'
                                       ^
SyntaxError: EOL while scanning string literal
>>> 
>>> len('abc')
3
>>> string_length = len('abc')
>>> print (string_length)
3
>>> my_string="Now is the time for all good men \ to come to the aid of their country"
>>> print(my_string)
Now is the time for all good men \ to come to the aid of their country
>>> my_string="""Now is the time for all good men to come to the aid of their country"""
>>> my_string
'Now is the time for all good men to come to the aid of their country'
>>> print(my_string)
Now is the time for all good men to come to the aid of their country
>>> help (len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> string_1 = "abra"
>>> string_2 = "cadabra"
>>> magic_string = string_1 + string_2
>>> magic_string
'abracadabra'
>>> first_name = "Arthur"
>>> last_name = "Dent"
>>> full_name = first_name + "" + last_name;
>>> full_name
'ArthurDent'
>>> full_name = first_name + " " + last_name;
>>> full_name
'Arthur Dent'
>>> flavor = 'apple pie'
>>> flavor[1]
'p'
>>> flavor[-3]
'p'
>>> flavor = 'apple_pie'
>>> flavor[0:3]
'app'
>>> flavor[4:5]
'e'
>>> word = "goal"
>>> word[0] = 'f'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> "Jean-luc Picard".lower
<built-in method lower of str object at 0xb525b4d0>
>>> "Jean-luc Picard".lower()
'jean-luc picard'
>>> loud_voice = "Can you hear me yet?"
>>> loud_voice.upper()
'CAN YOU HEAR ME YET?'
>>> white_space = '    This is white space  '
>>> white_space
'    This is white space  '
>>> rstring = white_space.rstrip()
>>> rstring
'    This is white space'
>>> white_space
'    This is white space  '
>>> lstring = white_space.lstrip()
>>> lstring
'This is white space  '
>>> s_string = white_space.strip()
>>> s_string
'This is white space'
>>> starship="Enterprise"
>>> starship.startswith("en")
False
>>> starship.endswith("rise")
True
>>> starship.lower().startswith("en")
True
>>> starship.upper().startswith("en")
False
>>> name = 'Jonathan'
>>> name.
  File "<pyshell>", line 1
    name.
        ^
SyntaxError: invalid syntax
>>> name
'Jonathan'
>>> input()
parameter is the promt string
'parameter is the promt string'
>>> input('Please enter a value')
Please enter a value
''
>>> promt = 'Please enter a value'
>>> input(promt)
Please enter a value1
'1'
>>> user_input = input(promt)
Please enter a value1
>>> user_input
'1'
>>> num = '2'
>>> num + num
'22'
>>> num ='12'
>>> num * 3
'121212'
>>> "12 * "3"
  File "<pyshell>", line 1
    "12 * "3"
           ^
SyntaxError: invalid syntax
>>> "12" * "3"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> "3" +3
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> num =input("Enter a number to be doubled:")
Enter a number to be doubled:6
>>> doubled_num=num*2
>>> print(doubled_num)
66
>>> num =input("Enter a number to be doubled:")
Enter a number to be doubled:3
>>> doubled_num=float(num) *2
>>> print(doubled_num)
6.0
>>> my_num = int(my_num)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_num' is not defined
>>> my_num="12.0"
>>> my_num = int(my_num)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12.0'
>>> my_num="12"
>>> my_num = int(my_num)
>>> print(my_num)
12
>>> num_pancakes = 10
>>> "I am going to eat" + num_pancakes + "pancakes."
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> "I am going to eat" + str(num_pancakes) + "pancakes."
'I am going to eat10pancakes.'
>>> "I am going to eat " + str(num_pancakes) + "pancakes."
'I am going to eat 10pancakes.'
>>> "I am going to eat " + str(num_pancakes) + " pancakes."
'I am going to eat 10 pancakes.'
>>> arms=2
>>> heads=3
>>> print('Has' + str(heads) + ' headsand' + str(arms) +'arms.')
Has3 headsand2arms.
>>> heads= 3
>>> arms= 2
>>> print('Has' + str(heads) + ' headsand' + str(arms) +'arms.')
Has3 headsand2arms.
>>> arms = 2
>>> heads = 3
>>> print('Has' + str(heads) + ' headsand' + str(arms) +'arms.')
Has3 headsand2arms.
>>> phrase = "the surprise is in here somwhere"
>>> phrase.find("surprise")
4
>>> phrase.find(today)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'today' is not defined
>>> phrase.find("today")
-1
>>> 
