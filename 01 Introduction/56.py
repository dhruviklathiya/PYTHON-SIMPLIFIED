# Extra knowledge
    # Converting dictionary from tuple
_tuple = (('USER1',1),('USER2',2),('USER3',3),('USER4',4))
_dict = dict(_tuple)
print(_dict)

# Iterator and iterable

# Something that can be looped over is iterable such as list, tuple, sets
# Iterator: list_iterator,tuple_iterator,set_iterator,dict_keyiterator and others that can help us loop over are iterator

for i in [1,2,3,4,5]:
    print(i)

# How for in loop is working
    # iter() => returns a iterator
    # next() => Accepts iterator & returns value

print(type(iter([1,2,3,4])))
print(type(iter((1,2,3,4))))
print(type(iter({1,2,3,4})))
print(type(iter({1:1,2:1,3:1,4:1})))

_iterator = iter([1,2,3,4,5])

print(next(_iterator))
print(next(_iterator))
print(next(_iterator))
print(next(_iterator))