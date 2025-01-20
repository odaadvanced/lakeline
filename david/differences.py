print("Input two numbers to see if the difference is an integer")

num1 = float(input("number 1 = "))
num2 = float(input("number 2 = "))

if (num1 - num2).is_integer() == True:
    print(f"The difference between {num1} and {num2} is an integer")
else:
    print(f"The difference between {num1} and {num2} is not an integer")
