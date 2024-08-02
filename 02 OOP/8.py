# Printing object
    # Once we have created object from a particular class but now we want to know what variables and data is contained by object then we must print that particular object

class Product:
    store_discount = 10
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price
    def apply_discount(self):
            return self.product_price - 0.01*self.store_discount*self.product_price

product1 = Product("Macbook Air M2",125000)
print(product1) # This will print memory location of our object
print(product1.__dict__) # This will print our actual object data