# Decorator function with arguments returning calculation
def decorator_function(_function):
    def inner_function(*args,**kwargs):
        print("This is extended line")
        # _function(*args,**kwargs) # This line is not valid because we must return the output
        return _function(*args,**kwargs)
    return inner_function

@decorator_function
def sum_calculation(_para1,_para2):
    print(f"This function takes argument _para as {_para1} & {_para2}")
    return _para1 + _para2

print(sum_calculation(20,3032))