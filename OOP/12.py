# Class task:
    # Create a class method that will return total number of instance made in this program

class Person:
    number_of_object = 0
    def __init__(self,name):
        self.name = name
        Person.number_of_object += 1
    def count_objects():
        return Person.number_of_object

p1 = Person("D")
p2 = Person("D CODER")
p3 = Person("Dhruvik lathiya")

print(Person.count_objects())