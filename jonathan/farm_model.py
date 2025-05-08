class Animal:
    
    stuff_in_belly = 0
    position = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def talk(self, sound=None):
        """Return the string "<name> says <sound>"
        If 'sound' is left out, returns "Hello, I'm <name>"
        """
        if sound is None:
            return f"Hello. I'm {self.name}!"
        return f"{self.name} says {sound}"
    def walk(self, walk_increment):
        self.position = self.position + walk_increment
        return self.position
    def run(self, run_increment):
        self.position = self.position + run_increment
        return self.position
    def feed(self):
        self.stuff_in_belly = self.stuff_in_belly + 1
        if self.stuff_in_belly > 3:
            return self.poop()
        else:
            return f"{self.name} is eating."
    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"
    def poop(self):
        self.stuff_in_belly = 0
        return "Ate too much... need to find the bathroom"
class Dog(Animal):
    def talk(self, sound="Bark Bark!"):
        return super() .talk(sound)
    def fetch(self):
        return f"{self.name} is fetching."
class Sheep(Animal):
    def talk(self, sound="Baaa Baaa"):
        return super().talk(sound)
class Pig(Animal):
    def talk(self, sound="Oink Oink"):
        return super().talk(sound)