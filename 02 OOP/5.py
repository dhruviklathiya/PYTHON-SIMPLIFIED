# Class methods task
    # Create a class for product
        # Creae method for applying discount

class Product:
    def __init__(self,name,price):
        self.product_name = name
        self.product_price = price

    def apply_discount(self,percentage):
        return self.product_price - self.product_price*0.01*percentage

product1 = Product("Macbook Air M2",125000)
print(product1.apply_discount(10))
print("This will not change actual price because we haven't assign it in our method")
print(product1.product_price)
