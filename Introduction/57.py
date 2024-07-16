# * operator in zip function
# Extract 2 tuples using zip

_tuple = ((1,11),(2,22),(3,33),(4,44),(5,55))

_list1, _list2 = list(zip(*_tuple))

print(_list1)
print(_list2)