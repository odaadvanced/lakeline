Python 3.7.3 (/usr/bin/python3)
>>> type(len)
<class 'builtin_function_or_method'>
>>> num_letters = len("four")
>>> num_letters
4
>>> return_value = print("What do I return?")
What do I return?
>>> return_value
>>> def multiply(x, y):
    # Function Body
    product = x * y
    return product

>>> multipy (4, 5)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'multipy' is not defined
>>> multiply (4, 5)
20
>>> def multiply(x, y):
    # Function Body
    product = x * y
print("Where am I?")

Where am I?
>>> multiply (4, 5)
>>> def multiply(x, y):
    # Function Body
    product = x * y
    return product

>>> def greet(name):
    print(f"Hello, {name}!")
    
>>> greet("Timothy")
Hello, Timothy!
>>> my_return
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_return' is not defined
>>> print(my_return)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_return' is not defined
>>> my_return = greet("Timothy")
Hello, Timothy!
>>> my_return
>>> print(my_return)
None
>>> def multiply(x, y):
    '''Return the produt of two numbers x and y'''
    product = x * y
    return product

>>> help(multiply)
Help on function multiply in module __main__:

multiply(x, y)
    Return the produt of two numbers x and y

>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> n = 1
>>> while n < 5:
    print(n)
    n = n + 1
    
1
2
3
4
>>> for letter in "Python":
    print(letter)
    
P
y
t
h
o
n
>>> for n in range (3):
    print("Python")
    
Python
Python
Python
>>> for n in range (10, 15):
    print(n * n)
    
100
121
144
169
196
>>> for n in range(1, 3):
    for j in range (3, 6):
        print(f"n = {n} and j = {j}")
        
n = 1 and j = 3
n = 1 and j = 4
n = 1 and j = 5
n = 2 and j = 3
n = 2 and j = 4
n = 2 and j = 5
>>> def my_function():
    x = 2
    print(f"inside 'my_function', x has the value {x}")
    
>>> x = "Hello, World"
>>> my_function()
inside 'my_function', x has the value 2
>>> x = 5
>>> def outer_func():
    y = 3
    def inner_func():
        z = x + y
        return z
    return inner_func()

>>> outer_func()
8
>>> total = 0
>>> def add_to_total(n):
    total = total + n
    
>>> add_to_total(5)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
  File "<pyshell>", line 2, in add_to_total
UnboundLocalError: local variable 'total' referenced before assignment
>>> total = 0
>>> def add_to_total(n):
    global total #use the global total
    total = total + n
    
>>> add_to_total(5)
>>> print(total)
5
>>> total = 0
>>> def my_total(n, total):
    total = total + n
    return total

>>> mytotal (4, total)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'mytotal' is not defined
>>> my_total (4, total)
4
>>> 
