# Functions returning more than one thing
def hello(a,b):
    return a,b

# All return value are wrapped in tuple
return_mix = hello(10,20)
print(type(return_mix))

# Return value seperated into variables
return1, return2 = hello(10,20)
print(return1)
print(return2)

# min() max() len() sum() in tuple
_tuple = tuple([1,2,3,4])
maximum = max(_tuple)
print("maximum",maximum)
manimum = min(_tuple)
print("manimum",manimum)
length = len(_tuple)
print("length",length)
sum = sum(_tuple)
print("sum",sum)