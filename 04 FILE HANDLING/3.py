# Change position of cursor ==> .seek()

# Cursor position ==> .tell()

_file = open('file.txt')
print("Cursor position is before first read() ===> ", _file.tell())
_data1 = _file.read() # Cursor starts from line 1 character 1 till end of whole file
print(_data1)
print("Cursor position is after first read() ===> ", _file.tell())

# Resetting cursor
_file.seek(32)
print("Cursor position is before second read() ===> ", _file.tell())
_data2 = _file.read()
print("Cursor position is after second read() ===> ", _file.tell())
print(_data2)
# It's not necessary to close the file but it's good practice
_file.close()