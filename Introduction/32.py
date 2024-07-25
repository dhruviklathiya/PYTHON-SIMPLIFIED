# TUPLE
    # Tuple are more advance than list
    # Tuple are immutable
    # Tuple cannot be changed
# Tuple does not have methods like pop, append, extend, insert like list
# Tuple have only 2 method: count, index

_tuple = (1,2,3,4,5,1,2,3,4,1,2,3,1,2,1)
print(_tuple.count(1))
    # count returns total repetition of element in tuple
print(_tuple.index(3))
    # returns first index containing element
print(_tuple.index(3,3))
    # returns first index containing element after skipping 3 index
print(_tuple[::-1])
    # [start slice: end slice: gap in between next slice]


# Unique note: We cannot create tuple with only one element
_tuple_try = (9)
print(type(_tuple_try)) # output => Integer
_tuple_try2 = (9,)
print(type(_tuple_try2)) # output => Tuple

# Unique note 2: Declaring tuple without paranthesis and tuple keyword is possible
_tuple_try3 = "hello","World","How_are_you"
print(type(_tuple_try3)) # output => Tuple

