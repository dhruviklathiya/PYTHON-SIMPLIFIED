# Price not negative logic
# Constructor all variable print and changes not implemented problem
    # solution 1: Method
    # solution 2: @property decorator

# Price not negative logic ===>
class Person:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = max(salary,0) # Minimum salary can be ZERO but it cannot be in negative

person1 = Person("Dhruvik","Lathiya",9999999)
print(person1.__dict__)

# Constructor all variable print and changes not implemented problem ===>
class Person:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = max(salary,0) # Minimum salary can be ZERO but it cannot be in negative
        self.all_combine = f"Firstname is {fname} Lastname is {lname} salary is {salary}"

person1 = Person("Dhruvik","Lathiya",9999999)
print(person1.all_combine)
person1.salary = 100000000
# We have changed salary which is also changed in our object but all_combine attribute it not changes because it got created when object got created and when we change object constructor does not run second time
print(person1.salary)
# We can see that salary is updated
print(person1.all_combine)

# Solution 1 ===> Creating method
class Person:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = max(salary,0) # Minimum salary can be ZERO but it cannot be in negative

    def all_combine(self):
        return f"Firstname is {self.fname} Lastname is {self.lname} salary is {self.salary}"

person1 = Person("Dhruvik","Lathiya",9999999)
print(person1.all_combine())
person1.salary = 100000000
print(person1.salary)
print(person1.all_combine())

# # Solution 2 ===> property in class
class Person:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = max(salary,0) # Minimum salary can be ZERO but it cannot be in negative

    @property
    def all_combine(self):
        return f"Firstname is {self.fname} Lastname is {self.lname} salary is {self.salary}"

person1 = Person("Dhruvik","Lathiya",9999999)
print(person1.all_combine)
person1.salary = 100000000
print(person1.salary)
print(person1.all_combine)