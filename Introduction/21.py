# Functions in python

# Define function
def hello():
    print("Hello world")

# Calling function
hello()

# Define function with return
def hello():
    return "Hello world"

# Calling function
result = hello()
print(f"This is returned from function => {result}")

# Define function with parameter
def hello(parameter1,parameter2):
    print(parameter1+parameter2)

# Calling functions with passed arguments
hello(10,100)

# Define function with parameter
def hello(parameter1,parameter2):
    return (parameter1+parameter2)

# Calling functions with passed arguments
result = hello(10,100)
print(f"This is returned from function => {result}")


# Define function with parameter along with default arguments
def hello(parameter1=10,parameter2=100):
    return (parameter1+parameter2)

# Calling functions with passed arguments
result = hello()
print(f"This is returned from function without passing arguments => {result}")

# Define function with parameter along with default arguments
def hello(parameter1=10,parameter2=100):
    return (parameter1+parameter2)

# Calling functions with passed arguments
result = hello(2000)
print(f"This is returned from function with passing one argument => {result}")