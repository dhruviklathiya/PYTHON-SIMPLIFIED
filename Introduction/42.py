# Comprehension in list

# Store square in list
_list = [i**2 for i in range(0,101)]
print(_list)
_list = [i*(-2) for i in range(0,101)]
print(_list)
_list = [-i for i in range(0,101)]
print(_list)

names = ["Hello","Bello","Jello"]
_list = [i[0] for i in names]
print(_list)

# Reverse element's value
_list = [i[::-1] for i in names]
print(_list)

# Even numbers only in list using comprehension
_list = [i for i in range(0,1001) if i%2==0]
print(_list)