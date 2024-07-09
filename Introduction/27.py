# list methods

# in keyword
_list = [1,2,3,4,5,3,6,3,7,3,8,3,3,9]
print(3 in _list)
print(10 in _list)

# count method
print(_list.count(3))

# sort method
_list.sort()
print(_list)
    # sort method changes list
        # solution: use sorted keyword
_list2 = [4,3,6,5,8,5,2,90]
print(sorted(_list2))
print(_list2)

# clear method => empty list
_list2.clear()
print(_list2)

# copy method
new_list = _list.copy()
print(new_list)