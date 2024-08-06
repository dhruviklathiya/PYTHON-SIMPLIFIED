# Python descriptor
    # They are not method nor function

# .name & .closed are descriptor

_file = open('file.txt')
print(_file.name) # Will return name of file
print(_file.closed) # Will return if file is opened or not at given point (moment)

_file.close()
print(_file.closed)