import random

def simulation():
    flips = 0
    heads = False
    tails = False
    while True:
        flips = flips + 1
        if random.randint(0,1)  == 0:
            heads = True
        else:
            tails = True

        if heads == True and tails == True:
            break
    return flips

overall_flips = 0
for x in range(1,10001):
    overall_flips = overall_flips + simulation()

average = overall_flips/10000
print(average)

