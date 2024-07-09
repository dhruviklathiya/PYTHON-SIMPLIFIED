# Python element delete from list methods
_list = [1,2,3,4,5,6,7,8,9,10]

_list.pop()
    # By default .pop method will remove last index of list
print(_list)

_list.pop(3)
    # Providing index will remove specific index from list
print(_list)

# del keyword for deleting specific index from list
del _list[3]
print(_list)

# remove method : when we do not know index to delete we will use value
_list.remove(7)
print(_list)

# Another method to declare list
new_list = list(range(1,100))
print(new_list)