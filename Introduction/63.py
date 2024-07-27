# Defining custom map || Passing function as argument to another function
def cube(one):
    return one**3
def custom_map(cube,_list):
    _result = []
    for i in _list:
        _result.append(cube(i))
    return _result

print(custom_map(cube,[1,2,3,4,5,6,7]))