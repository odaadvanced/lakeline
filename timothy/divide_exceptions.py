def divide(num1, num2):
    try:
        print(num1 /num2)
    except TypeError:
        print("Both arguments must be numbers.")
    except ZeroDivisionError:
        print("The second number must not be 0.")
        

divide(1e1000,0.1)
