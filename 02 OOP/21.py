# Method resolution order:
    # If method is not found in child class then python will look for that method in parent class

# We can use help() for finding order of resolution
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Base class 2
class Bird:
    def fly(self):
        return f"{self.name} is flying."

# Derived class
class Parrot(Animal, Bird):
    def speak(self):
        return f"{self.name} says: Hello!"

# Instantiate the Parrot class
polly = Parrot("Polly")

print(help(Parrot))

# Method overriding:
    # Both terminology are same
    # If method is not found in child class then python will look for that method in parent class

# Method resolution order is a list that python go through for checking available methods
# Method overriding is a way how python runs method in inherited class