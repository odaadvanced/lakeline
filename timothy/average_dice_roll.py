from random import randint
from time import sleep

one_tally = 0
two_tally = 0
three_tally = 0
four_tally = 0
five_tally = 0
six_tally = 0

def number():
    try:
        global n
        n = int(input("How many trials do you want the program to run?"))
    except ValueError:
        print("Please enter a whole number!")
        sleep(1.5)
        number()

number()

for trial in range(n):
    trial = randint(1,6)
    if trial == 1:
        one_tally += 1
    elif trial == 2:
        two_tally += 1
    elif trial == 3:
        three_tally += 1
    elif trial == 4:
        four_tally += 1
    elif trial == 5:
        five_tally += 1
    else:
        six_tally += 1
print(f"The average value of the dice roll is: {((one_tally + 2*two_tally + 3 * three_tally + 4 * four_tally + 5 * five_tally + 6 * six_tally)/n):.2f}.")