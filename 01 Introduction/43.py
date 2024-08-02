# Comprehension in nested list
_list = [[1,2,3],[4,5,6],[7,8,9]]

for i in _list:
    for j in i:
        print(j)

_nested = [[i for i in range(0,3)] for j in range(0,3)]
print(_nested)