# Create list of numbers
    # If number is even double it and store in list
    # If number is odd store negative value of number
_list = [1,2,3,43,5,32,76,8]
_result = [i*2 if i%2==0 else -i for i in _list]
print(_result)