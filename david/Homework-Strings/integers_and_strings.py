#1. Create a string containing an integer, then convert that string into an actual integer object using int().
#   Test that your new object is a number by multiplying it by another number and displaying the result.
number_string = "5"
number = int(number_string)
print(str(number * 5))

#2. Repeat the previous exercise, but usa a floating-point number and float()
number_string_float = "9.8"
number_float = float(number_string_float)
print(str(number_float* 3.7))

#3. Create a string object and integer object, then display them side by side with a single print function call using str().
sentence = "Number of Frogs: "
frogs = 3839210
print(sentence + str(frogs))

#4. Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, and displays the result.
print("Input Two Numbers to be Multiplied")
number_1 = input("Number 1: ")
number_2 = input("Number 2: ")
print("The Product of " + str(number_1) + " and " + str(number_2) + " is " + str(int(number_1) * int(number_2)))