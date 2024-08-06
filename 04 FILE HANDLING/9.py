# write mode in python

    # For editing file in write mode we pass 'w' as second parameter
    # If file does not exist then python will automatically generate new file
with open('new_file.txt','w') as _file: # Check by changing name of file to something else
    _file.write("This is new file created by python")

_file = open('new_file.txt')
print(_file.read())

with open('new_file.txt','w') as _file:
    _file.write("Updated file\nThis is new line")

_file = open('new_file.txt')
print(_file.read())

# We can notice that write mode replace all content inside our file