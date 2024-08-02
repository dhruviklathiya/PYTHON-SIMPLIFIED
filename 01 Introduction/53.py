# filter funtion in python
    # same as map function in python

_output = list(filter(lambda a:a>10,[1,2,3,4,5,6,10,20,30,40,50]))
print(_output)


def value_10(one):
    return one>10

_result = list(filter(value_10,[1,2,3,4,5,6,10,20,30,40,50]))
print(_result)