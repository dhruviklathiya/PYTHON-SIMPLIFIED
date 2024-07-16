# filter funtion in python
    # same as map function in python

_output = list(filter(lambda a:a>10,[1,2,3,4,5,6,10,20,30,40,50]))
print(_output)

# Difference in map & filter
# ===> Map will return result as true or false in conditions
# ===> Filter will return actual value in conditions
_result = list(map(lambda a:a>10,[1,2,3,4,5,6,10,20,30,40,50]))
print(_result)