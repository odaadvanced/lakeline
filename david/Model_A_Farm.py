import random


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} ate {random.randint(1, 26)} lbs of food"

class Cow(Animal):

    def sound(self, noice = "MOOO"):
        return f"{self.name} Says {noice}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Sheep(Animal):

    def sound(self, noice = "BAAA"):
        return f"{self.name} Says {noice}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Chicken(Animal):

    def sound(self, noice = "BOCK BOCK"):
        return f"{self.name} Says {noice}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def threat(self):
        return f"{self.name.upper()} IS COMING FOR YOU"

Bessie = Cow("Bessie", 15)
Billy = Sheep("Billy", 4)
Gorlock_Destoryer_of_Worlds = Chicken("Gorlock Destroyer of Worlds", 9736)
print(Bessie.sound())
print(Billy.sound())
print(Gorlock_Destoryer_of_Worlds.sound())

print(Bessie.eat())
print(Billy.eat())
print(Gorlock_Destoryer_of_Worlds.eat())

print(Bessie)
print(Billy)
print(Gorlock_Destoryer_of_Worlds)

print(Gorlock_Destoryer_of_Worlds.threat())
