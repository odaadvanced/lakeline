import random

total_wins = 0

def vote(chance):
    global wins
    if random.randint(1,100) <= chance:
        wins = wins + 1

for x in range(1,10001):
    wins = 0
    vote(87)
    vote(65)
    vote(17)
    if wins >= 2:
        total_wins = total_wins + 1

average = total_wins / 100
print(total_wins)
print(f"Candidate A wins {average}% of electons")