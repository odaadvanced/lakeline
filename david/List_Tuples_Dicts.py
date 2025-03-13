Python 3.7.3 (/usr/bin/python3)
>>> my_tuple = (1,2,3)
>>> my_tuple
(1, 2, 3)
>>> type (my_tuple)
<class 'tuple'>
>>> my_tuple = tuple ('123456789')
>>> my_tuple
('1', '2', '3', '4', '5', '6', '7', '8', '9')
>>> test_tuple = tuple (ghuhhi73y7yhydueddv)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'ghuhhi73y7yhydueddv' is not defined
>>> test_tuple = tuple ("jfijijvr37uuifh")
>>> test_tuple
('j', 'f', 'i', 'j', 'i', 'j', 'v', 'r', '3', '7', 'u', 'u', 'i', 'f', 'h')
>>> my_tuple = ("123456789")
>>> my_tuple
'123456789'
>>> my_tuple = (123456789)
>>> my_tuple
123456789
>>> my_tuple = (1,2,3,4,5,6,7,8,9)
>>> my_tuple = (1,2,3,4,5,6,7,8,9)
>>> my_tuple
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> my_tuple = tuple(1,2,3,4,5,6,7,8,9)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: tuple expected at most 1 arguments, got 9
>>> my_tuple = (1,2,3,4,5,6,7,8,9)
>>> my_tuple
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> dif_values = ("Del", 50, 'Austin', 78727)
>>> dif_values
('Del', 50, 'Austin', 78727)
>>> len(my_tuple)
9
>>> len(dif_values)
4
>>> my_tuple[2]
3
>>> my_str = ("Now is the time")
>>> my_str[2:4]
'w '
>>> my_tuple[2:4]
(3, 4)
>>> my_tuple[2,4]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: tuple indices must be integers or slices, not tuple
>>> 
>>> my_tuple[2] = 4
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> for number in my_tuple:
    print(number)
    
1
2
3
4
5
6
7
8
9
>>> new_tuple = 23.3, 45.6
>>> new_tuple
(23.3, 45.6)
>>> type(new_tuple)
<class 'tuple'>
>>> x, y = new_tuple
>>> new_tuple
(23.3, 45.6)
>>> x
23.3
>>> y
45.6
>>> first, middle, last = 'David', 'John', 'Kirkland'
>>> first
'David'
>>> middle
'John'
>>> last
'Kirkland'
>>> first, middle, last
('David', 'John', 'Kirkland')
>>> num1, num2, num3 = 1,2,3,4
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
ValueError: too many values to unpack (expected 3)
>>> vowels = ('a', 'e', 'i', 'o', 'u')
>>> 'o' in vowels
True
>>> def add_sub:
    return (a+b, a-b)

  File "<pyshell>", line 1
    def add_sub:
               ^
SyntaxError: invalid syntax
>>> def add_sub(a,b):
    return (a+b, a-b)

>>> add_sub(2,3)
(5, -1)
>>> x, y = add_sub(5,3)
>>> x
8
>>> y
2
>>> list('Python')
['P', 'y', 't', 'h', 'o', 'n']
>>> my_colors = "red, orange, blue, green"
>>> my_colors
'red, orange, blue, green'
>>> my_colors_list = my_colors.split(',')
>>> my_color_list
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'my_color_list' is not defined
>>> my_colors_list
['red', ' orange', ' blue', ' green']
>>> 'black' in my_colors_list
False
>>> 'red' in my_colors_list
True
>>> numbers = [1,2,3,4,5,6]
>>> for number in numbers:
    if number % 2==0:
        print(number)
        
2
4
6
>>> numbers[2] = 10
>>> numbers
[1, 2, 10, 4, 5, 6]
>>> numbers[2:4] = [30, 40, 50]
>>> numbers
[1, 2, 30, 40, 50, 5, 6]
>>> nummbers
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'nummbers' is not defined
>>> numbers.insert(3, 'not number')
>>> numbers
[1, 2, 30, 'not number', 40, 50, 5, 6]
>>> KeyboardInterrupt
>>> numbers
[1, 2, 30, 'not number', 40, 50, 5, 6]
>>> numbers.pop(3)
'not number'
>>> numbers
[1, 2, 30, 40, 50, 5, 6]
>>> numbers.insert(3, 'not number')
>>> numbers.pop('not number')
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> numbers.pop(3)
'not number'
>>> numbers.append(100)
>>> numbers
[1, 2, 30, 40, 50, 5, 6, 100]
>>> numbers.extend([200, 300, 400])
>>> numbers
[1, 2, 30, 40, 50, 5, 6, 100, 200, 300, 400]
>>> for number in numbers:
    total = total + number
    
Traceback (most recent call last):
  File "<pyshell>", line 2, in <module>
NameError: name 'total' is not defined
>>> total = 0
>>> for number in numbers:
    total = total + number
    
>>> total
1134
>>> nums = [20, 30, 1, 400, 30, 50, 60]
>>> min(nums)
1
>>> max(nums)
400
>>> numbers
[1, 2, 30, 40, 50, 5, 6, 100, 200, 300, 400]
>>> squares = [num**2 for num in numbers]
>>> squares
[1, 4, 900, 1600, 2500, 25, 36, 10000, 40000, 90000, 160000]
>>> nested_list = [[1,2], [3,4,5]]
>>> nested_list
[[1, 2], [3, 4, 5]]
>>> len(nested_list)
2
>>> len(nested_list[1])
3
>>> nested_list[1][1]
4
>>> list_1 = [1,2,3,4]
>>> list_2 = list_1
>>> list_1
[1, 2, 3, 4]
>>> list_2
[1, 2, 3, 4]
>>> list_2.append(5)
>>> list_2
[1, 2, 3, 4, 5]
>>> list_1
[1, 2, 3, 4, 5]
>>> list_2 = list_1[:]
>>> list_2.append(6)
>>> list_2
[1, 2, 3, 4, 5, 6]
>>> list_1
[1, 2, 3, 4, 5]
>>> matrix_1 = [[1,2], [3,4]]
>>> matrix_2 = matrix_2[:]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'matrix_2' is not defined
>>> matrix_2 = matrix_1[:]
>>> matrix_2[0] = [7,8]
>>> matrix_2
[[7, 8], [3, 4]]
>>> matrix_1
[[1, 2], [3, 4]]
>>> matriz[1][1] = 10
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'matriz' is not defined
>>> matrix_1[1][1] = 10
>>> matrix_1
[[1, 2], [3, 10]]
>>> matrix_2
[[7, 8], [3, 10]]
>>> import copy
>>> matrix_3 = copy.deepcopy(matrix_1)
>>> matrix_3
[[1, 2], [3, 10]]
>>> matrix_1[1][0] = 22
>>> matrix_3
[[1, 2], [3, 10]]
>>> matrix_1
[[1, 2], [22, 10]]
>>> numbers
[1, 2, 30, 40, 50, 5, 6, 100, 200, 300, 400]
>>> numbers.sort()
>>> numbers
[1, 2, 5, 6, 30, 40, 50, 100, 200, 300, 400]
>>> letters = ['z', 'ab', 'ba', 'x', 'c', 'r']
>>> letters
['z', 'ab', 'ba', 'x', 'c', 'r']
>>> letters.sort()
>>> letters
['ab', 'ba', 'c', 'r', 'x', 'z']
>>> KeyboardInterrupt
>>> letters = ['z', 'ab', 'ba', 'x', 'C', 'r']
>>> letters.sort()
>>> letters
['C', 'ab', 'ba', 'r', 'x', 'z']
>>> capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas: Austin"
    }
  File "<pyshell>", line 5
    }
    ^
SyntaxError: invalid syntax
>>> capitals = 
    {"California": "Sacramento",
    "New York": "Albany",
    "Texas: Austin",
    }
  File "<pyshell>", line 1
    capitals =
              ^
SyntaxError: invalid syntax
>>> capitals =   {"California": "Sacramento",
    "New York": "Albany",
    "Texas: Austin",
    }
  File "<pyshell>", line 3
    "Texas: Austin",
                   ^
SyntaxError: invalid syntax
>>> capitals =   {"California": "Sacramento",
    "New York": "Albany",
    "Texas: Austin"
    }
  File "<pyshell>", line 4
    }
    ^
SyntaxError: invalid syntax
>>> capitals =   {"California": "Sacramento",
    "New York": "Albany",
    "Texas: Austin"}
  File "<pyshell>", line 3
    "Texas: Austin"}
                   ^
SyntaxError: invalid syntax
>>> capitals =   {"California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"}
>>> capitals
{'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin'}
>>> type(capital)
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'capital' is not defined
>>> type(capitals)
<class 'dict'>
>>> capitals['Texas']
'Austin'
>>> capitals['Austin']
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'Austin'
>>> capitals["Colorado"] = "Denver"
>>> capitals
{'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin', 'Colorado': 'Denver'}
>>> capitals["Colorado"] = "Boulder"
>>> capitals
{'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin', 'Colorado': 'Boulder'}
>>> del capitals['Colorado']
>>> capitals
{'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin'}
>>> capitals["A"]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'A'
>>> for key in capitals:
    print (key)
    
California
New York
Texas
>>> for state in capitals:
    print( f"The capital of {state} is {capitals[state]}")
    
The capital of California is Sacramento
The capital of New York is Albany
The capital of Texas is Austin
>>> KeyboardInterrupt
>>> 
