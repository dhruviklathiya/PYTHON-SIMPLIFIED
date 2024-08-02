# Some variables that can help us guide ourselves
print(len.__doc__)
# Keep this code commented otherwise terminal will be stop on a single point
# print(help(len))

print(sum.__doc__)
# Keep this code commented otherwise terminal will be stop on a single point
# print(help(sum))

# Writing our custom doc string
def hello():
    '''This is details about function'''
    return "Hello world"
print(hello.__doc__)