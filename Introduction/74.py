# Generator loop takes less memory space in hardware for example,

def our_generator(_number):
    for i in range(0,_number+1):
        yield i

_instruction = our_generator(10)

for i in _instruction:
    print(i)
for i in _instruction:
    print(i)
for i in _instruction:
    print(i)

# We have printed 0 to 10 three times but will only be printed once.

# Note: ==> We can reuse generator but cannot reuse generator object in this case _instruction