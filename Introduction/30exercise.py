# INPUT of function => LIST || OUTPUT from function => LIST WITH ELEMENT OF SQUARE
_input = input("Enter value to be square [seperate by comma]: ").split(",")

def square_this_list(list):
    square_list = []
    for i in list:
        square_list.append(i*i)
    return square_list

_list = []
for i in _input:
    _list.append(int(i))
print(square_this_list(_list))


_result = []

# Method 1
# for i in range(0,len(_list)):
#     _result.append(_list[len(_list)-1-i])
# print(_result)

# Method 2
# for i in _list:
#     _result.insert(0,i)

# print(_result)

# Method 3
# _list.reverse()
# print(_list)

# Method 4
# _result = list(reversed(_list))
# print(_result)

# Method 4
# _result = _list[::-1]
# print(_result)

# Reversing nested elements inside a list
    # ['abc','def'] => ['cba','fed']

# _list = ['ABC','DEF','GHI']
# new_list = []
# for i in range(0,len(_list)):
#         new_list.append(_list[i][::-1])
# print(new_list)

# Solution:2
_list = ['ABC','DEF','GHI']
new_list = []
for i in _list:
        new_list.append(i[::-1])
print(new_list)