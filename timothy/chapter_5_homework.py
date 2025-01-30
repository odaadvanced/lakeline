#Chapter 5 Homework
#Section 5.1 Excercise 1
num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)
#Excercise 2
num = 1.75e5
#Excercise 3
smallest_exponent_inf = 2e308
'''Since we're using THONNY and not IDLE, I used the shell to find the smallest exponent that returned inf.'''
'''The section 5.3 excercise was done in class and should be in the github as exponent.py'''
#Section 5.5 Excercise 1
response1 = input("Enter a number: ")
print(f"{response1} rounded to 2 decimal places is {round(float(response1), 2)}")
#Excercise 2
response2 = input("Enter a number: ")
print(f"The absolute value of {response2} is {abs(float(response2))}")
#Excercise 3
response3 = input("Enter a number: ")
response4 = input("Enter another number: ")
print(f"The difference between {response3} and {response4} is an integer? {(float(response3) - float(response4)).is_integer()}!")
#Section 6.6 Excercise 1
print(f"The result of the calculation is {(3 ** .125):.3f}")
#Excercise 2
print(f"${150000:,.2f}")
#Excercise 3
print(f"{(2 / 10):.0%}")