# Short-hand syntax for decorating function

def first_class_function(_function):
    def inner_function():
        print("This is updated line")
        _function()
    return inner_function

@first_class_function
def function_1():
    print("Hello world")
# Now everytime function_1 will be called it will have extended functionality
function_1()

def first_class_function2(_function):
    def inner_function():
        print("This is updated line for function 2")
        _function()
    return inner_function

@first_class_function2
def function_2():
    print("Hello world")
function_2()

