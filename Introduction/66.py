# Changing function's block of code without changing function itself
def function_1():
    print("Hello world")

def function_2():
    print("Hello world")

# If we want to add new code into this line we can by creating a first-class function
def first_class_function(_function):
    def inner_function():
        print("This is updated line")
        _function()
    return inner_function

our_function = first_class_function(function_1)
our_function()