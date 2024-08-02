# Inheritance
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
print(child1.__dict__)
print(child1.all_in_one())
# Here we can notice that child is able to access methods of parent