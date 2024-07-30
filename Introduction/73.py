# Generators:
    # They are same as iterator the only important difference is in memory management
        # While traditional iterator takes up bulk amount of space in memory for iteration, generator only takes up place of single element
    # Use: Not asking python to run full loop instead we get output in sequence as we want
        # Generator will not provide output unless we ask for it

def our_generator(_number):
    for i in range(1,_number+1):
        yield i

print(our_generator(10)) # Generator

for i in our_generator(10):
    print(i)