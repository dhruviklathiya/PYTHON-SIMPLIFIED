# Generators:
    # They are same as iterator the only important difference is in memory management
        # While traditional iterator takes up bulk amount of space in memory for iteration, generator only takes up place of single element
    # Use: Not asking python to run full loop instead we get output in sequence as we want
        # Generator will not provide output unless we ask for it
import time

def our_generator(_number):
    for i in range(1,_number+1):
        yield i

print(our_generator(10)) # Generator

for i in our_generator(10):
    print(i)

# Let's comapre time taken by traditional loop and generator
t1 = time.time()
for i in range(0,11):
    print(i)
t2 = time.time()
print(f"Final time is for simple loop {t2-t1}")

# Generator time
t1 = time.time()
def our_generator(_number):
    for i in range(0,_number+1):
        yield i
for i in our_generator(11):
    print(i)
t2 = time.time()
print(f"Final time is for generator ==> {t2-t1}")