# Generators:
    # For understanding generators we first need to revise iterator and iterable from previous practices

# Iterable:
    # Data that can be looped over is iterable data
    # Example: _list = [1,2,3,4,5]
        # list can be looped making it iterable

# Iterator:
    # When the loop will start running iter() function of python is called
                                        # iter() function takes a single argument which is iterable and will return an iterator

    # Example: iter(_list) ==> This will return iterator

# next()
    # Next is function that propogate our iterations next() function takes a single argument which is our iterator returned by iter() function

_list = [1,2,3,4,5]
_iterator = iter(_list)
print(_iterator)

print(next(_iterator))
print(next(_iterator))
print(next(_iterator))