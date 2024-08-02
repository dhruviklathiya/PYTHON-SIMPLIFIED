# Raise NotImplemented error
# &
# Abstract method

class Animal():
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def sleep(self):
        print("Sleeping...")

# Derived Class
class Dog(Animal):
    pass # We must

# Derived Class
class Cat(Animal):

    def sound(self):
        return "Meow"

# Instantiate derived classes
dog = Dog()
cat = Cat()

# Every animal must have sound but cat and dog must have different sound for that reason we can not provide sound() method to be declared in parent class
    # If Dog class does not have sound() method then error will be raised by Animal class that it should have individual sound

print(cat.sound())  # Output: Meow
print(dog.sound())  # Output: Error
cat.sleep()         # Output: Sleeping...
dog.sleep()         # Output: Sleeping...