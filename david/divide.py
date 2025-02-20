def divide (num1, num2):
    try:
        print(int(num1)/int(num2))
    except ValueError:
        print("Both arguments must be integers")
    except TypeError:
        print("Both arguments must be numbers")
    except ZeroDivisionError:
        print("num2 must not be 0")
        
divide(input(),input())