from random import random


def region(chance_A_wins):
    if random() < chance_A_wins:
        return "A"
    else:
        return "B"


def run_election(regional_wins):
    A_region_wins = 0
    for A_chance in regional_wins:
        if region(A_chance) == "A":
            A_region_wins += 1
    B_region_wins = len(regional_wins) - A_region_wins
    if A_region_wins > B_region_wins:
        return "A"
    else:
        return "B"


a_prob = [0.87, 0.65, 0.17]
NUM_TRIALS = 10_000


A_election_wins = 0
for trial in range(NUM_TRIALS):
    if run_election(a_prob) == "A":
        A_election_wins += 1


print(f"Probability A wins: {A_election_wins / NUM_TRIALS}\nProbability B wins: {1 - (A_election_wins / NUM_TRIALS)}")