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

# Reverse a list using function
def reverse_this_list(list):
    reversed_list = []
    for i in range(1,len(list)+1):
        reversed_list.append(list[len(list)-i])
    return reversed_list

print(reverse_this_list(_list))
# Reverse a list using in-built function
_list.reverse()
print(_list)

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