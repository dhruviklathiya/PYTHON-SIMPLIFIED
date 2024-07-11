def _dictionary_cube(n):
    _cube_dict = {}
    for i in range(1,n+1):
        # _cube_dict[i] = i*i*i
        _cube_dict[i] = i**3
            # Both are valid way to cube
    return _cube_dict

_parameter = int(input("Enter number: "))
result = _dictionary_cube(_parameter)
print(result)