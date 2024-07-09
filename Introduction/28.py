_list1 = [1,2,3,4]
_list2 = [5,6,7,8]
_list3 = [1,2,3,4]
_list4 = _list1

# Double equals check value
print(_list1 == _list2)
print(_list1 == _list3)

# Tripple equal check memory location
print(_list1 is _list2)
print(_list1 is _list3)
print(_list1 is _list4) # True because of same memory location
