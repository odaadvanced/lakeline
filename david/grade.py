grade = int(input("input a grade:"))

if grade >= 90:
    if grade == 100:
        print("You passes the class with an A+")
    else:
        print("You passed the class with an A")
elif grade >= 80:
    print("you passes the class with a B")
elif grade >= 70:
    print("you passes the class with a C")
else:
    print("YOU FAILED")
print("thank you for attending") 