# Map function
    # Map will take 2 arguments => callback function & data
    # Map will return an object which can be converted into list,tuple,set

def square(a):
    return a*a

_output = list(map(square,[1,2,3,4]))

print(_output)

# Map + lambda

_result = list(map(lambda a:a**2,[1,2,3,4,5]))
print(_result)

# Note:- Map object are only iterable once, for multiple iteration we must convert map into list,tuple,set