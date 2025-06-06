from random import random
num_times_A_wins = 0
num_times_B_wins = 0
num_trials = 10_000
for trial in range(0, num_trials):
    votes_for_A = 0
    votes_for_B = 0
    
    if random() < 0.87:
        votes_for_A = votes_for_A + 1
    else:
        votes_for_B = votes_for_B + 1
        
    if random() < 0.65:
        votes_for_A = votes_for_A + 1
    else:
        votes_for_B = votes_for_B + 1
        
    if votes_for_A > votes_for_B:
        num_times_A_wins = num_times_A_wins + 1
    else:
        num_times_B_wins + 1
        
print(f"Probability A wins: {num_times_A_wins / num_trials}")
print(f"Probability B wins: {num_times_B_wins / num_trials}")