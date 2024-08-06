# Solution of not replacing content but adding is append mode in python

# If file does not exist then python will automatically generate new file
with open('new_file.txt','a') as _file:
    _file.write("\nThis is new file created by python\nThis is new line")

_file = open('new_file.txt')
print(_file.read())

# We can notice that append mode did not replace all content inside our file but instead added