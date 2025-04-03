class Dog:
    species = "canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
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
    def speak(self, sound = 'woof'):
        return f"{self.name} always says {sound}"
collie = Collie('lassie', 2)
bill = Bulldog('bill', 4)
print('the end')