# Additional variable in objects and variable in class works and operates separately

# Applying class variable's discount

class Product:
    store_discount = 10
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price
    def apply_discount(self):
            return self.product_price - 0.01*self.store_discount*self.product_price

product1 = Product("Macbook Air M2",125000)
print("Price after default discount by store is:",product1.apply_discount())

# Applying object made discount
class Product:
    store_discount = 10
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price
    def apply_discount(self,outer_discount):
            return self.product_price - 0.01*outer_discount*self.product_price

product1 = Product("Macbook Air M2",125000)

product1.outer_discount = 20
print(f"Price after applying object specific discount: {product1.apply_discount(50)}")

# Applying both discount on same product
class Product:
    store_discount = 10
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price
    def apply_discount(self,outer_discount):
            return self.product_price - 0.01*outer_discount*self.product_price - 0.01*self.store_discount*self.product_price

product1 = Product("Macbook Air M2",125000)

product1.outer_discount = 20
print(f"Price after applying default and also object specific discount: {product1.apply_discount(50)}")