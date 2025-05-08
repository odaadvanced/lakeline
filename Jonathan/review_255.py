food = ["rice", "beans"]
>>> food.append("broccoli")
>>> food
['rice', 'beans', 'broccoli']
>>> food.extend(["bread", "pizza"])
>>> food
['rice', 'beans', 'broccoli', 'bread', 'pizza']
>>> print(food[0:2])
['rice', 'beans']
>>> print(food[4])
pizza
>>> breakfast = "eggs, fruit, orange juice"
>>> breakfast_food = breakfast.split(", ")
>>> breakfast_food
['eggs', 'fruit', 'orange juice']
>>> len(breakfast_food)
3
>>> lengths = [len(item) for itemm in breakfast_food]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
  File "<pyshell>", line 1, in <listcomp>
NameError: name 'item' is not defined
>>> lengths = [len(item) for item in breakfast_food]
>>> print(lengths)
[4, 5, 12]