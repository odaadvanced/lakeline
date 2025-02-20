
grade = float (input("give grade :"))

   
if grade >= 90:
    if grade >= 100:
        print("You got a +A amazing job!")
    else:    
        print ("You got a A great job!")
elif grade >= 70:
    print("You passed the class!")
elif grade < 70:
    print("You failed the class")
    
print("Thank you for atteding")
