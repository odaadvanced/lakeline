string=("Hello, World")
>>> print(string)
Hello, World
>>> string=('Jonathan')
>>> print(string)
Jonathan
>>> print("""Hello, my name
... is Jonathan what is yours
... I do not know how to win a chess game.""")
Hello, my name
... is Jonathan what is yours
... I do not know how to win a chess game.
>>> long_string = "Hello, i am Jonathan \
How are you?"
>>> print(long_string)
Hello, i am Jonathan How are you?
>>> len(abc)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'abc' is not defined
>>> len('abc')
3
>>> string_1 = ('Peanut')
>>> string_2 = ('Butter')
>>> final_string = string_1 + string_2
>>> print(final_string)
PeanutButter
>>> string_1 = ('Hello')
>>> string_2 = ('world')
>>> final_string = string_1 + " " + string_2
>>> print(final_string)
Hello world
>>> flavor = 'bazinga'
>>> flavor[2:5]
'zin'
>>> flavor[2:6]
'zing'
>>> names = ("Animals", "Badger", "Honey Bee", "Honey Badger".)
  File "<pyshell>", line 1
    names = ("Animals", "Badger", "Honey Bee", "Honey Badger".)
                                                              ^
SyntaxError: invalid syntax
>>> name = "Animals, Badger, Honey Bee, Honey Badger"
>>> name = name.upper()
>>> name
'ANIMALS, BADGER, HONEY BEE, HONEY BADGER'
>>> name = name.lower()
>>> name
'animals, badger, honey bee, honey badger'
>>> string1 = "   Filet Mignon"
>>> string1.lstrip()
'Filet Mignon'
>>> string1
'   Filet Mignon'
>>> string2 = "Brisket    "
>>> string2.rstrip()
'Brisket'
>>> string3 = "     Cheeseburger    "
>>> string3.strip()
'Cheeseburger'
>>> starship = "Becomes"
>>> starship.startswith("be")
False
>>> starship = "becomes"
>>> starship.startswith("be")
True
>>> starship = "BEAR"
>>> starship.startswith("be")
False
>>> starship = "bEcomes"
>>> starship.startswith("be")
False
>>> input()
Hello, World!
'Hello, World!'
>>> input().lower()
Hello, World!
'hello, world!'
>>> input().len()
Hello, World!
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'str' object has no attribute 'len'
>>> input()
len(Hello, World!)
'len(Hello, World!)'
>>> string = ("12.0")
>>> innum = input("Enter a number to be doubled: ")
Enter a number to be doubled: 2
>>> doubled_num = float(innum) * 2
>>> print(doubled_num)
4.0
>>> num_Chess Pieces = 5
  File "<pyshell>", line 1
    num_Chess Pieces = 5
                   ^
SyntaxError: invalid syntax
>>> num_Chesspeices = 5
>>> "I am going to take " + str(5) + " ChessPeices."
'I am going to take 5 ChessPeices.'
>>> num = input("Enter two numbers to be multplied: ")
Enter two numbers to be multplied: 2 and 4
>>> multiplied_num = float(num) 
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: could not convert string to float: '2 and 4'
>>> num = 0.2
>>> float(num)
0.2
>>> animal = 'newt'
>>> weight_of_newt = float(num) + "kg is the weight of the" + animal
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> weight_of_newt = num + "kg is the weight of the" + animal
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> weight_of_newt = 'num' + "kg is the weight of the" + 'animal'
>>> weight_of_newt
'numkg is the weight of theanimal'
>>> weight_of_newt = '0.2 ' + "kg is the weight of the" + ' animal'
>>> weight_of_newt
'0.2 kg is the weight of the animal'
>>> weight_of_newt = '0.2 ' + "kg is the weight of the" + ' newt'
>>> weight_of_newt
'0.2 kg is the weight of the newt'
>>> " {} kg is the weight of {}".format(weight, name)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'weight' is not defined
>>> "AAA".find("a")
-1
>>> text = "Somebody said something to Samantha."
>>> new_text = text.replace("s", "x")
>>> new_text
'Somebody xaid xomething to Samantha.'
>>> input().find(h)
Hello, World!
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'h' is not defined
>>> input().find("h")
Hello, World!
-1
>>> Enter some text: Hey how ya dooooin, ya im doing good.
  File "<pyshell>", line 1
    Enter some text: Hey how ya dooooin, ya im doing good.
             ^
SyntaxError: invalid syntax
>>> text = "I like to eat green eggs and ham."
>>> new_text = text.replace("o", "0")
>>> new_text = text.replace("e", "3")
>>> new_text = text.replace("s", "2")
>>> new_text = text.replace("i", "1")
>>> new_text = text.replace("t", "7")
>>> new_text
'I like 7o ea7 green eggs and ham.'
>>> 