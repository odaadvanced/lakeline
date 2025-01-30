Python 3.7.3 (/usr/bin/python3)
>>> a=6
>>> u=9
>>> a+u
15
>>> type(len)
<class 'builtin_function_or_method'>
>>> a=u+b
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'b' is not defined
>>> b=8
>>> a=u+b
>>> a
17
>>> a-b
9
>>> num_letters=len('four')
>>> num_letters
4
>>> num_letters=len('two')
>>> num_letters
3
>>> return_value = print('what do i return')
what do i return
>>> return_value = print('what do I return')
what do I return
>>> return_value = print('what do I return?')
what do I return?
>>> return_value
>>> 
>>> def multiply(x, y):
 product = x * y
 return product
<put in two returns>

  File "<pyshell>", line 4
    <put in two returns>
    ^
SyntaxError: invalid syntax
>>> def multiply(x, y):
 product = x * y
print ('where am I?')

where am I?
>>> def greet(name)

  File "<pyshell>", line 1
    def greet(name)
                  ^
SyntaxError: invalid syntax
>>> def greet(name):
print (f'hello, {name}!')

  File "<pyshell>", line 2
    print (f'hello, {name}!')
        ^
IndentationError: expected an indented block
>>> def greet(name):
print (f'hello, {name}!')

  File "<pyshell>", line 2
    print (f'hello, {name}!')
        ^
IndentationError: expected an indented block
>>> def greet(name):
print (f'Hello, {name}!')

  File "<pyshell>", line 2
    print (f'Hello, {name}!')
        ^
IndentationError: expected an indented block
>>> greet ('luke')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'greet' is not defined
>>> greet('luke')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'greet' is not defined
>>> def greet('name'):
print (f'Hello, {name}!')

  File "<pyshell>", line 1
    def greet('name'):
                   ^
SyntaxError: invalid syntax
>>> greet('luke')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'greet' is not defined
>>> def multiply(x, y )
"""Return the product of
two numbers x and y"""
product = x *y
return product

  File "<pyshell>", line 1
    def multiply(x, y )
                      ^
SyntaxError: invalid syntax
>>> return (multiply)
Traceback (most recent call last):
  File "<pyshell>", line 1
SyntaxError: 'return' outside function
>>> def multiply(x, y )
 """Return the product of 
two numbers x and y"""
product = x *y
return product

  File "<pyshell>", line 1
    def multiply(x, y )
                      ^
SyntaxError: invalid syntax
>>> n = 1
>>> while n < 5:
 print(n)
 n = n + 1
 
1
2
3
4
>>> while True n < 5:
 print(n)
 n = n + 1
 
  File "<pyshell>", line 1
    while True n < 5:
               ^
SyntaxError: invalid syntax
>>> for letter in "Python":
    print (letter)
 
P
y
t
h
o
n
>>> for letter in "Py1thon":
    print (letter)
    
P
y
1
t
h
o
n
>>> for letter in "Py1thon":
    print (letter)
    
P
y
1
t
h
o
n
>>> for letter in "Python":
    print (letter)
    
P
y
t
h
o
n
>>> 
>>> 
>>> for item in ['a','b','c']:
    print(item)
    
a
b
c
>>> for item in ['att','btt','c']:
    print(item)
    
att
btt
c
>>> for item in ['a','b','c']:
    print(item)
    
a
b
c
>>> a=4
>>> for item in ['a','b','c']:
    print(item)
    
a
b
c
>>> for n in range (3):
    print('Python')
    
Python
Python
Python
>>> for n in range(10, 15):
    print(n * n)
    
100
121
144
169
196
>>> for n in range(, 3):
    for j in range (3,6):
        print(f"n = {n} and j = {j}")
        
  File "<pyshell>", line 1
    for n in range(, 3):
                   ^
SyntaxError: invalid syntax
>>> for n in range(1, 3):
    for j in range (3,6):
        print(f"n = {n} and j = {j}")
        
n = 1 and j = 3
n = 1 and j = 4
n = 1 and j = 5
n = 2 and j = 3
n = 2 and j = 4
n = 2 and j = 5
>>> 
>>> x = "Hello, World"
>>> x
'Hello, World'
>>> def my_function():
    x=2
    
>>> x
'Hello, World'
>>> def my_function():
x=2
print(f"Inside ' func' , x has the value {x}")

  File "<pyshell>", line 2
    x=2
    ^
IndentationError: expected an indented block
>>> def my_function():
x = 2
print(f"Inside ' func' , x has the value {x}")

  File "<pyshell>", line 2
    x = 2
    ^
IndentationError: expected an indented block
>>> func()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'func' is not defined
>>> def func():
x = 2
print(f"Inside ' func' , x has the value {x}")

  File "<pyshell>", line 2
    x = 2
    ^
IndentationError: expected an indented block
>>> func()
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'func' is not defined
>>> x = 5
>>> def outer_func():
y = 3
def inner_func():
    z = x+y
    return z
return inner_func()

  File "<pyshell>", line 2
    y = 3
    ^
IndentationError: expected an indented block
>>> def outer_func():
    y = 3
    def inner_func():
        z = x+y
        return z
    return inner_func()

>>> outer_func()
8
>>> total=0
>>> def add_to_total(n):
total = total + n

  File "<pyshell>", line 2
    total = total + n
        ^
IndentationError: expected an indented block
>>> def add_to_total(n):
total = total + n

  File "<pyshell>", line 2
    total = total + n
        ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total
total = total + n

  File "<pyshell>", line 2
    global total
         ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total
total = total + n

  File "<pyshell>", line 2
    global total
         ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total = total + n

  File "<pyshell>", line 2
    global total = total + n
         ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total = total + n

  File "<pyshell>", line 2
    global total = total + n
         ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total
total = total + n

  File "<pyshell>", line 2
    global total
         ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total #use the global total
total = total + n

  File "<pyshell>", line 2
    global total #use the global total
         ^
IndentationError: expected an indented block
>>> def add_to_total(n):
global total #use the global total
total = total + n

  File "<pyshell>", line 2
    global total #use the global total
         ^
IndentationError: expected an indented block
>>> total = 0
>>> def add_to_total(n):
global total #use the global total
total = total + n

  File "<pyshell>", line 2
    global total #use the global total
         ^
IndentationError: expected an indented block
>>> def add_to_total(n, total):
global total #use the global total
total = total + n

  File "<pyshell>", line 2
    global total #use the global total
         ^
IndentationError: expected an indented block
>>> def mytotal (n, total):
    total = total + n
    return total

>>> total
0
>>> myreturn=mytotal
>>> myreturn=mytotal(3,total)
>>> myreturn
3
>>> total
0
>>> 
