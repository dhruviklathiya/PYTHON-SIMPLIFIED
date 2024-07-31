# Class variables
    # Every particular object had their own value but if we want to build a class that has common value for all objects of that class we declare class variable

class Product:
    store_discount = 10
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price
    def apply_discount(self):
            return self.product_price - 0.01*self.store_discount*self.product_price

product1 = Product("Macbook Air M2",125000)
print("Price after default discount by store is:",product1.apply_discount())
print("This will not change actual price because we haven't assign it in our method")
print(product1.product_price)