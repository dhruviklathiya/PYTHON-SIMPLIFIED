# Create a function that takes n number of arguments and returns sum
    # Arguments can be anything string, number, list, set, tuple, dictionaries
        # But our function should only sum number
            # Create this task with help of decorator
def argument_checker(_function,*args):
    def inner_function(*args):
        valid = []
        for i in args:
            if isinstance(i,int):
                valid.append(i)
        return _function(*valid)
    return inner_function

@argument_checker
def sum_fun(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

# print(sum_fun(1,2,3,4,5))
print(sum_fun(1,2,3,4,5,[1,2,3],{1,2,3,4}))
