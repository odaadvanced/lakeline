#1
data = ((1, 2), (3, 4))

#2
x = 0
for row in data:
    x = x + 1
    print(f"Row {x} sum: {row[0]+row[1]}")

#3
numbers = [4, 3, 2, 1]
print(numbers)

#4
numbers_copy = numbers[0:4]
print(numbers_copy)

#5
numbers.sort()
print(numbers)