# Creating class in python

class Car:
    def __init__(self, carname, carprice):
        self.carname = carname
        self.carprice = carprice
        self.car_price = carprice

car1 = Car("Venue","70000$")
print(car1.carname)
print(car1.carprice)
# We can also change name of variable
print(car1.car_price)