# * operator in zip function
# Extract 2 tuples using zip

_tuple = ((1,11),(2,22),(3,33),(4,44),(5,55))

_list1, _list2 = zip(*_tuple)

print(list(_list1))
print(list(_list2))