from random import randint

num_of_flips = 0

def trial():
    global num_of_flips
    heads_counter = 0
    tails_counter = 0
    if heads_counter < 1 or tails_counter < 1:
        if randint(0,1) == 1:
            heads_counter += 1
            num_of_flips += 1
        else:
            tails_counter += 1
            num_of_flips += 1
            
        

for iterations in range(10_000):
    trial()

print(f"The average number of flips to get both a heads and a tails is {num_of_flips/10000:.2f}")
    