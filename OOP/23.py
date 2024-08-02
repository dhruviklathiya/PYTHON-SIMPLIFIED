# Base class 1
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

# Access methods from both base classes
print(polly.speak())  # Output: Polly says: Hello!
print(polly.fly())    # Output: Polly is flying.

# Here we can observe that Parrot class can access property of Animal & Bird class