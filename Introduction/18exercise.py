# Take input from user and print output of repetition in string
    # only use for loop

_string = input("Enter your name: ")
_container = ""


for i in range(len(_string)):
    if _string[i] not in _container:
        print(f"Character '{_string[i]}' is repeated {_string.count(_string[i])} times")
        _container += _string[i]
    else:
        pass