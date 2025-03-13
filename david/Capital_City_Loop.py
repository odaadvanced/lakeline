import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahasse',
    'Georgia': 'Atlanta'
}

def pick_state():
    state = random.choice(list(capitals_dict.keys()))
    capital = capitals_dict[state]
    while True:
        response = input(f"What is the capital of {state}?").lower()
        if response == "exit":
            print("Goodbye")
            quit()
        if response == capital.lower():
            print("Correct")
            quit()
        else:
            print("Incorrect")


try:
    pick_state()
except KeyboardInterrupt:
    print("Goodbye")