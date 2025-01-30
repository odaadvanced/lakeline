Python 3.7.3 (/usr/bin/python3)
>>> type(len)
<class 'builtin_function_or_method'>
>>> num_letters = len("four")
>>> num_letters
4
>>> return_value = print("What do I return")
What do I return
>>> return_value
>>> def multiply(x, y):
    product = x * y
    return product

>>> multiply(4, 5)
20
>>> def multiply(x, y):
    product = x * y
    
>>> print("Where am I")
Where am I
>>> def multiply(x, y):
    product = x * y
print("Where am I")

Where am I
>>> def greet(name):
    print(f"Hello, {name}!")

>>> greet("bean")
Hello, bean!
>>> greet("David")
Hello, David!
>>> my_return = greet("David")
Hello, David!
>>> my_return
>>> print(my_return)
None
>>> def multiply(x, y):
    """Return the product of
two numbers x and y"""
    product = x * y
    return product

>>> help(multiply)
Help on function multiply in module __main__:

multiply(x, y)
    Return the product of
    two numbers x and y

>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

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
>>> for letter in "python":
    print(letter)

p
y
t
h
o
n
>>> type(while)
  File "<pyshell>", line 1
    type(while)
             ^
SyntaxError: invalid syntax
>>> type(for)
  File "<pyshell>", line 1
    type(for)
           ^
SyntaxError: invalid syntax
>>> help(help)
Help on _Helper in module _sitebuiltins object:

class _Helper(builtins.object)
 |  Define the builtin 'help'.
 |  
 |  This is a wrapper around pydoc.help that provides a helpful message
 |  when 'help' is typed at the Python interactive prompt.
 |  
 |  Calling help() at the Python prompt starts an interactive help session.
 |  Calling help(thing) prints help for the python object 'thing'.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |      Call self as a function.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> for n in range (3):
    print("Python")

Python
Python
Python
>>> for n in range (10, 15):
    print("n * n")
    
n * n
n * n
n * n
n * n
n * n
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
>>> x = "Hello, World"
>>> def my_function():
    x = 2
    
>>> my_function()
>>> def my_function():
    x = 2
    print(f"Inside 'func', x has the value {x}")
    
>>> my_function()
Inside 'func', x has the value 2
>>> x = 5
>>> def outer_func():
    y = 3
    def inner_func():
        z = x + y
        return z
    return inner_func()

>>> 
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
>>> def add_to_total(n):
    global total
    total = total + n
 
>>> add_to_total
<function add_to_total at 0xb482e108>
>>> add_to_total(5)
>>> print(total)
5
>>> total = 0
>>> def mytotal (n, total):
    total = total + n
    return total

>>> mytotal (3, total)
3
>>> mytotal (3, total)
3
>>> mytotal (3, total)
3
>>> total
0
>>> 

