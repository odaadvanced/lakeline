def divide(num1, num2):
    num1 = input("Give a number: ")
    num2 = input("Give a number: ")
    try:
        print(num1 / num2)
    except TypeError:
        print("Bothe arguments must be numbers")
    except ZeroDivisionError:
        print("num2 must not be 0")
        