# Define methods in class
# Default methods: For example lists

_list = [1,2,3,4,5]
_list.pop()
print(_list)

# Same as this we will define method
    # Method is nothing more than functions defined in a class

class Car:
    def __init__(this_object,name,year,price):
        this_object.car_name = name
        this_object.car_year = year
        this_object.car_price = price
    def sum_of_year_and_price(this_object):
        return this_object.car_price + this_object.car_year

object1 = Car("Range Rover",2000,90000)
_result = object1.sum_of_year_and_price()
print(_result)

class Person:
    def __init__(self,first_name,last_name,middle_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.middlename = middle_name
        self.age = age
    def full_name(self):
        return (self.first_name +" "+ self.middlename +" "+ self.last_name)

person1 = Person("John","Doe","Clay",20)
_result = person1.full_name()
print(_result)