phrase = input("Write a phrase: ")
for character in phrase:
    if character == "X" or "x":
        print("X was in the phrase")
        break
    
else:
    print("There was no'X' in the phrase")