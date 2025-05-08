data = ((1, 2), (3, 4))
>>> data[0]
(1, 2)
>>> data[1]
(3, 4)
>>> index = 1
>>> for row in data:
    print(f"Row {index} sum: {sum(row)}")
    index += 1
    
Row 1 sum: 3
Row 2 sum: 7
>>> numbers = [4, 3, 2, 1]
>>> exponents = numbers[:]
>>> exponents.append("5")
>>> exponents
[4, 3, 2, 1, '5']
>>> numbers
[4, 3, 2, 1]
>>> numbers.sort()
>>> numbers
[1, 2, 3, 4]