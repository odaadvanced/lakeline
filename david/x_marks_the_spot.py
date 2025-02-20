phrase = "it mXarks the spot"

for character in phrase:
    if character == "X":
        print("An 'X' has marked the spot")
        break
else:
    print("There was no 'X' in the phrase")