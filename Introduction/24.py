# List in python || Works like array

_list = [1,2,3,4,5,6]
print(_list)
print(_list[0])
print(_list[1])
print(_list[2])
print(_list[0:4])

_list_ = [1,2,"String",'Single quotwd string',3,5.4,4,5,6]
print(_list_)

# list is muttable

# breaking list
_list_[2:] = "HELLO"
print(_list_)
    # python will break "HELLO" into pieces and will replace them on index 2, rest of elements will be removed
_list_[2:] = [11,12,13,14,15]
print(_list_)
    # python will break list [11,12,13,14,15] and will replace them on index 2
