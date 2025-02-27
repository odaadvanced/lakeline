import random
total = 0

def roll():
    return random.randint(1,6)

for x in range(1,10001):
    total = total + roll()
    average = total / 10000
    
print(average)
    

