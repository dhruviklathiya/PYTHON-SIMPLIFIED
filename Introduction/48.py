# Passing list as *args
_list = [1,2,3,4,5,6,7,8]

def hello(*args):
    for i in args:
        print(i)

hello(_list) # Our list is passed as tuple

def hello(*args):
    for i in args:
        print(i)
hello(*_list) # This will unpack our list