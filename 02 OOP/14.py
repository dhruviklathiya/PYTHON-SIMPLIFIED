# Static method in python
    # Static method is for both class and instance whereas,
    # Class method is only for class
    # Instance method is only for instance
class Person:
    def __init__(self,fname,lname,age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    @staticmethod
    def hello():
        print("Hello this is static method")

person1 = Person("Dhruvik","Lathiya",9)
person1.hello() # Instance using static method
Person.hello() # Class using static method