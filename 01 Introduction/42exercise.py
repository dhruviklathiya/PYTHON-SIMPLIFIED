# Create seperate list according to data type of element in list
_list = [1,2.0,3,4,"Hello","Bello","Jello",[1,2,3]]
_numbers = []

for i in _list:
    if type(i) == int or type(i) == float:
        _numbers.append(i)

print(_numbers)