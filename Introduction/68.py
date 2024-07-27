# Arguments with decorator function

# def decorator_function(_function):
#     def inner_function():
#         print("This is extended line")
#         _function()
#     return inner_function

# @decorator_function
# def function_print(_para):
#     print(f"This function takes argument _para as {_para}")

# function_print(20) # Will throw error because we have passed parameter and not provided argument

def decorator_function(_function):
    def inner_function(*args,**kwargs):
        print("This is extended line")
        _function(*args,**kwargs)
    return inner_function

@decorator_function
def function_print(_para):
    print(f"This function takes argument _para as {_para}")

function_print(20)