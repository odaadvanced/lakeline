num1 = float(input("Give me a number: "))
num2 = float(input("Give me a second number: "))
num3 = num1 - num2
print(f"Is the difference between {num1} and {num2} an integer? \
{num3.is_integer()}")