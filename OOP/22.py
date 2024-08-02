#  isinstance() & issubclass()

# isinstance(_data_to_check, _class_to_check_with)
class Parent:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def all_in_one(self):
        return f"Firstname is {self.fname} Lastname is {self.lname} salary is {self.salary}"

class Child(Parent):
    def __init__(self, fname, lname, age, study_standard, salary):
        super().__init__(fname, lname, age)
        self.study_standard = study_standard
        self.salary = salary

child1 = Child("John","Doe",21,12, 120)

# isinstance returns boolean true if object we created belong to class we provided else false
print(isinstance(child1,Parent))

class Person:
    def __init__(self,age):
        self.age = age

print(isinstance(child1,Person))


# issubclass returns boolean true if a child class extends parent class else false
print(issubclass(Child,Parent))

print(issubclass(Child,Person))