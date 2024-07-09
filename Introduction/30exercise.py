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