# Create list of every line in file

_file = open('file.txt')
_list = _file.readlines()
print(_list)

# Finding number of lines in file
print(len(_list))

_file.close()