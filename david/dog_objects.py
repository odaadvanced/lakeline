class Dog:
    species = "Canis familiarias"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Terrier(Dog):
    pass
class Collie(Dog):
     def speak(self, sound = 'bow wow'):
         return f"{self.name} always says {sound}"
class Bulldog(Dog):
    def describe(self):
        return f"{self.name} has short hair"
class Golden_Retriever(Dog):
    def speak(self, sound='BARK!'):
        return f"{self.name} always says {sound}"
my_rover = Dog('Rover', 942)

print(my_rover.__str__())

print(my_rover.speak("BARK!!!!!"))

print(my_rover)

bob = Terrier("bob", 8697)
billy = Collie("billy", 82)
bobert = Bulldog("bobert", 58783)

print(billy.speak())
print(bobert.describe())