>>> captains = {}
>>> captains["Enterprise"] = "Picard"
>>> captains["Voyager"] = "Janeway"
>>> captains["Defiant"] = "Sisco"
>>> captains
{'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant': 'Sisco'}
>>> if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
    
>>> if "Discovery" not in captains:
    captains["Discovery"] = "unknown"
    
captains
{'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant': 'Sisco', 'Discovery': 'unknown'}for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")
    
The Enterprise is captained by Picard.
The Voyager is captained by Janeway.
The Defiant is captained by Sisco.
The Discovery is captained by unknown.
>>> del captains["Discovery"]
>>> captains
{'Enterprise': 'Picard', 'Voyager': 'Janeway', 'Defiant': 'Sisco'}
captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Vayoger", " Janeway"),
        ("Defiant", "Sisko"),
        ("Discovery", "unknown")
    ]
)
>>> captains
{'Enterprise': 'Picard', 'Vayoger': ' Janeway', 'Defiant': 'Sisko', 'Discovery': 'unknown'}