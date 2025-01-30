#1. In one line of code, display the result of trying to .find() the substring "a" in the string "AAA".
print("AAA".find("a"))

#2. Replace every occurrence of the character "s" with "x" in the sentence, "Somebody said something to Samantha".
sentence = "Sombody said something to Samantha"
print(sentence.lower().replace("s", "x"))

#3. Write a program that accepts user input with input() and displays the result of tring to .find() a particular letter
# in that input.
input = input("Write a message")
print(input.find("a"))