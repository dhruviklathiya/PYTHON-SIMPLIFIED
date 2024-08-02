# Adding variables to object but from outside of class scope

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person("Dhruvik",9)
print(person1.__dict__)

person1.salary = "100K$/month"
print(person1.__dict__)
# We have added new variable in this object name ==> salary