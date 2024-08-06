# PYTHON FILE HANDLING
# Most important thing while reading file is to track where the cursor is,

_file = open('file.txt')
_data1 = _file.read() # Cursor starts from line 1 character 1 till end of whole file
_data2 = _file.read()
print("First time read data ==> ",_data1)
print("Second time read data ==> ",_data2) # Output will be blank because cursor is on last line - last character and file does not have anything to read after read once

# It's not necessary to close the file but it's good practice
_file.close()