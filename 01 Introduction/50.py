# lambda function
    # lambda is keyword that is used for making functions anonymous

# Simple function
def hello():
    print("Hello world !")
# Calling function
hello()
# Printing function
print(hello) # Output: returns memory location of function

# Define anonymous function
this_is_not_function = lambda a,b : a*b # Function takes 2 argument a&b and will return multiplication of both
print(this_is_not_function(10,20))

# Trying to print lambda function
print(this_is_not_function)
    # WILL RETURN A LAMDA IN MEMORY LOCATION