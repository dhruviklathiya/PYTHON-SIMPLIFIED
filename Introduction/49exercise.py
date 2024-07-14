# Input multiple strings from user and create function that returns a list with all string having first letter capitalized
# _input = input("Enter name seperated by commas").split(",")

# def title_string(*args):
#     _list = []
#     for i in args:
#         _list.append(i.capitalize())
#     return _list

# _result = title_string(*_input)
# print(_result)

# If str_rev = True is passed then reverse string and then capitalize
_input = input("Enter name seperated by commas").split(",")

def title_string(*args,**kwargs):
    _list = []
    if kwargs["str_rev"]:
        for i in args:
            _list.append(i[::-1].capitalize())
    else:
        for i in args:
            _list.append(i.capitalize())
    return _list

print(title_string(*_input,str_rev=False))
# print(_result)