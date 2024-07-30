# Generator task

def our_generator(_number):
    for i in range(0,_number+1):
        if i%2==0:
            yield i

_generator_object = our_generator(20)

for i in _generator_object:
    print(i)