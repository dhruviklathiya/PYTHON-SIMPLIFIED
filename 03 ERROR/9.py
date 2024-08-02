# Custom error generation in python

def calculation(a,b):
    if isinstance(a,int or float) and isinstance(b, int or float):
        return a+b
    raise TypeError("Please provide numeric input")
    # raise ValueError("Please provide numeric input")

print(calculation(10,20))
# Uncomment for raising custom error
# print(calculation(10,"20"))