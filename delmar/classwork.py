Python 3.7.3 (/usr/bin/python3)
>>> for item in ['a','b','c']:
    print (item)
    
a
b
c
>>> total = 0
>>> def mytotal (n, total):
    total = total + n
    return total

>>> def mytotal (n, total):
    total = total + n
    return total

>>> total
0
>>> myreturn = mytotal(3, total)
>>> myreturn
3
>>> total
0
>>> def mytotal (n, total):
    global total
    total = total + n
    return total

Traceback (most recent call last):
  File "<pyshell>", line 2
SyntaxError: name 'total' is parameter and global
>>> 
>>> def mytotal (n, total):
    total = total + n
    return total

>>> 
