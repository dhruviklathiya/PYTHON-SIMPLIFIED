# Cursor position ==> .tell()

_file = open('file.txt')
print("Cursor position is before first read() ===> ", _file.tell())
_data1 = _file.read() # Cursor starts from line 1 character 1 till end of whole file
print("Cursor position is after first read() ===> ", _file.tell())
_data2 = _file.read()
print("First time read data ==> ",_data1)
print("Second time read data ==> ",_data2) # Output will be blank because cursor is on last line - last character and file does not have anything to read after read once

# It's not necessary to close the file but it's good practice
_file.close()