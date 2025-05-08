import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Arkansas": "Litlle Rock",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "California": "Sacramento",
    "Conneticut": "Hartford",
    "Colorado": "Denver",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Indiana": "Indianapolis",
    "Illinois": "Springfeild",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Lousiana": "Baton Rouge",
    "Massachusetts": "Boston",
    "Maryland": "Annapolis",
    "Maine": "Augusta",
    "Mississippi": "Jackson",
    "Minnesota": "Saint Paul",
    "Missouri": "Jefferson City",
    "Michigan": "Lansing",
    "Nebraska": "Lincoln",
    "New York": "New York City",
    "Nevada": "Carson City",
    "New Jersey": "Trenton",
    "New Hampshire": "Concord",
    "New Mexico": "Santa Fe",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Texas": "Austin",
    "Tennesee": "Nashville",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virgina": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisonsin": "Madison",
    "Wyoming": "Cheyenne",
    
    }
    
state, capital = random.choice(list(capitals_dict.items()))
    
while True:
        guess = input(f"What is the capital of '{state}'? ").lower()
        if guess == "exit":
            print(f"The capital of '{state} is '{capital}'.")
            print("Goodbye")
            break
        elif guess == capital.lower():
            print("Correct! Nice job.")
            break