# function returning a function ==> First-class-function
def outer_function():
    def innner_function():
        print("This is function returned from another function")
    return innner_function

# Let us initialize function as our_function
our_function = outer_function()
# Now all the functionality contained by inner_function will be available in our_function
our_function()

# Now we will call our inner function while returning from outer_function
def outer_function():
    def innner_function():
        print("This is function returned from another function")
    return innner_function()

# Let us initialize function as our_function
our_function = outer_function()
# We do not have to call our_function because it is by default executing code inside function