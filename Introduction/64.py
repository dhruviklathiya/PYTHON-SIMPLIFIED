# function returning a function
def outer_function():
    def innner_function():
        print("This is function returned from another function")
    return innner_function

# Let us initialize function as our_function
our_function = outer_function()
# Now all the functionality contained by inner_function will be available in our_function
our_function()