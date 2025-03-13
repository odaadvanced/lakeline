import random
print("I'm thinking of a number between 1 and 10. Guess which one.")
B = int(input("Type in your guess: "))
A = random.randint(1, 10)
if B == A:
    print(f"You where right the number was {A} you win!")
else:
    print(f"You lose the number was {A}.")