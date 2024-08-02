# Change value of variable in class

class Product:
    store_discount = 10
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price
    def apply_discount(self):
            return self.product_price - 0.01*self.store_discount*self.product_price

product1 = Product("Macbook Air M2",125000)
print("Price after old default discount by store is:",product1.apply_discount())

Product.store_discount = 25

print("Price after new default discount by store is:",product1.apply_discount())