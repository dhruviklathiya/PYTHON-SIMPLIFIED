# Polymorphism
    # Multiple forms
print(4+4)
print("ABC"+"XYZ")

# + sign works in 2 forms
    # for numbers it sums them into arithmetic
    # for string it concats them

# Operator overloading is an example of polymorphism
# Method overriding is also an example of polymorphism

# In short:
    # Method overriding: Child class will check for presence of method in itself if not found then will go to check in parent class
    # Method overloading: Same class will have method declared by same names but each method will take differnt number of parameters makeing them different from eachother
    # Operator overloading: Same operator performs different operation on different operand

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

person1 = Person("Dhruvik",9)
print(person1.add(10,20,30)) # Output: 60
print(person1.add(10,20)) # Expected output: 30 but instead will get error because python does not support method overloading