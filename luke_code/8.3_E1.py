A = input("Type something: ")

if len(A) < 5:
    print("Your input is less than 5 characters long.")
elif len(A) > 5:
    print("Your input is greater than 5 characters long.")
else:
    print("Your input is 5 characters long.")
