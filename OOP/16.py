# Naming convention:
    # It is not necessary to follow convention but it's made by developer community for better understanding of code

# _name ===> Private method || Private name
# __name__ ===> Dunder || Double underscore method || Magic methods

# Remember there is nothing private in python but for letting other developer know that do not change specific method or variable value we define name in different naming convention

# One key point to remember:
# __name ===> This is not a naming convention but it will change name of variable

# Example:
class Person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.__age = age

person1 = Person("Dhruvik","Lathiya",9)
# Try to print __age attribute
# print(person1.__age)
# Python will throw error

print(person1.__dict__)
# Name of variable we defined is replcaed by _Person__age

# We can use:
print(person1._Person__age)