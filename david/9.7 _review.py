#1
captains = {}

#2
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"
print(captains)

#3
if "Enterprise" not in captains:
    captains["Enterprise"] = "Unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "Unknown"
print(captains)

#4
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")

#5
del captains["Discovery"]
print(captains)

#6
captains_2 = dict((("Enterprise", "Picard"), ("Voyager", "Janeway"), ("Defiant", "Sisko")))
print(captains_2)