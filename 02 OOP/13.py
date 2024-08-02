# Define and use method in class (class methods)

class Person:
    number_of_object = 0
    def __init__(self,name):
        self.name = name
        Person.number_of_object += 1
    # For creating method for class we will use decorator provided by python
    @classmethod
    # Like we define self in every object method, we must define argument in class method [we can provide any name except for keywords of python]
    def count_objects(argument):
        return print(f"THIS CLASS HAS {argument.number_of_object} instances")

p1 = Person("D")
p2 = Person("D CODER")
p3 = Person("Dhruvik lathiya")

Person.count_objects()